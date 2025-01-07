from copy import deepcopy
from decimal import Decimal
import json
from tabulate import tabulate

from logistics.services.bin_packing_services.fitnesscalc_service import FitnessCalculateService
from logistics.services.bin_packing_services.mutation_service import MutationService
from logistics.services.bin_packing_services.nsga2_service import Nsga2Service
from logistics.services.bin_packing_services.population_service import PopulationService
from logistics.services.bin_packing_services.recombination_service import RecombinationService
from logistics.services.bin_packing_services.survivor_selection_service import SurvivorSelectionService
from logistics.services.bin_packing_services.visualize_plotly_service import VisualizePlotlyService
from logistics.models import PackageDetail
from orders.models import OrderResult

class CalculateBinPackingService:
    
    @staticmethod
    def update_order_result(order_result_id,updated_data):
        try:
            order_result = OrderResult.objects.get(id=order_result_id)
            for key, value in updated_data.items():
                setattr(order_result, key, value)
            order_result.save()
            return order_result
        except OrderResult.DoesNotExist:
            raise ValueError("order result not found")
    
    @staticmethod
    def calculate_bin_packing(packages,truck):
        NUM_OF_ITERATIONS = 1
        NUM_OF_INDIVIDUALS = 100
        NUM_OF_GENERATIONS = 1
        PC = int(0.8 * NUM_OF_INDIVIDUALS)
        PM1 = 0.2
        PM2 = 0.02
        K = 2
        ROTATIONS = 2  # 1 or 2 or 6
        
        # print("Running Problem Set")
        # print(tabulate([['Generations', NUM_OF_GENERATIONS], ['Individuals', NUM_OF_INDIVIDUALS],
        #                     ['Rotations', ROTATIONS], ['Crossover Prob.', PC], ['Mutation Prob1', PM1],
        #                     ['Mutation Prob2', PM2], ['Tournament Size', K]], headers=['Parameter', 'Value'],
        #                 tablefmt="github"))
        # final_boxes,packages = p_p.calculate_box_informations(products,pallets) burada final boxes lazim
        pallets = []
        for package in packages:
            package_detail = PackageDetail.objects.filter(package__id = package.id)
            total_weight = package.pallet.weight
            for p_detail in package_detail:
                total_weight += p_detail.count * p_detail.product.weight_type.std
            pallets.append([package.pallet.dimension.width,package.pallet.dimension.depth,package.pallet.dimension.height,package.pallet.dimension.volume,total_weight])
        
        order_result = OrderResult.objects.create(order = packages[0].order)
        
        truck_dimension = [truck.dimension.width,truck.dimension.depth,truck.dimension.height]
        boxes =  pallets
        total_value = sum(pallet[4] for pallet in pallets)
        
        box_params = {}
        
        for index in range(len(boxes)):
            # Storing the average values over every single iteration
            box_params[index] = boxes[index]
        
        average_vol = []
        average_num = []
        average_value = []
        
        for i in range(NUM_OF_ITERATIONS):
            population = PopulationService.generate_pop(box_params, NUM_OF_INDIVIDUALS, ROTATIONS)
            
            gen = 0
            progress = 0
            average_fitness = []
            step = int(100 / NUM_OF_ITERATIONS)
            while gen < NUM_OF_GENERATIONS:
                population, fitness = FitnessCalculateService.evaluate(population, truck_dimension, box_params, total_value)
                population = Nsga2Service.rank(population, fitness)
                offsprings = RecombinationService.crossover(deepcopy(population), PC, k=K)
                offsprings = MutationService.mutate(offsprings, PM1, PM2, ROTATIONS)
                population = SurvivorSelectionService.select(population, offsprings, truck_dimension, box_params, total_value,
                                        NUM_OF_INDIVIDUALS)
                average_fitness.append(CalculateBinPackingService.calc_average_fitness(population))
                gen += 1
                progress += step
                updated_data = {
                    "progress": progress
                }    
                CalculateBinPackingService.update_order_result(order_result.id,updated_data)
            results = []

        # Storing the final Rank 1 solutions
            updated_results = []
            for key, value in population.items(): 
                if value['Rank'] == 1:
                    results.append(value['result'])
            for res,order_val in zip(results[0],population[0]['order']):
                updated_res = res + [order_val,box_params[order_val][4]]
                updated_results.append(updated_res)
            converted_data = CalculateBinPackingService.convert_decimals_to_int(updated_results)
            # Plot using plotly
            #color_index = vis.draw_solution(pieces=packages)
            
            updated_data = {
                "progress": 100,
                "success": True,
                "result": converted_data
            }
            CalculateBinPackingService.update_order_result(order_result.id,updated_data)
            order_result = OrderResult.objects.get(id=order_result.id)
            data = json.loads(order_result.result)
            color_index = VisualizePlotlyService.draw_solution(pieces=data,truck_dimension=truck_dimension)
            
            # VisualizePlotlyService.draw(converted_data, color_index) # Burasi 4 tane sonuc veriyor
            
            print(tabulate(
            [['Problem Set', 0], ['Runs', NUM_OF_ITERATIONS], ['Avg. Volume%', sum(average_vol) / len(average_vol)],
                ['Avg. Number%', sum(average_num) / len(average_num)],
                ['Avg. Value%', sum(average_value) / len(average_value)]],
            headers=['Parameter', 'Value'], tablefmt="github"))
            
    @staticmethod
    def convert_decimals_to_int(data):
        if isinstance(data, list):
            return [CalculateBinPackingService.convert_decimals_to_int(item) for item in data]
        elif isinstance(data, Decimal):
            return int(data)
        else:
            return data  

    @staticmethod
    def calc_average_fitness(individuals):
        fitness_sum = [Decimal(0.0), Decimal(0.0), Decimal(0.0)]
        count = 0
        for key, value in individuals.items():
            if value['Rank'] == 1:
                count += 1
                fitness_sum[0] += Decimal(value['fitness'][0])
                fitness_sum[1] += Decimal(value['fitness'][1])
                fitness_sum[2] += Decimal(value['fitness'][2])
        if count == 0:  # Bölme hatası olmaması için kontrol
            count = 1
        
        average = [number / Decimal(count) for number in fitness_sum]
        return average