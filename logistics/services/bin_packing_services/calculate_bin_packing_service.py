from copy import deepcopy
from tabulate import tabulate

from logistics.services.bin_packing_services.fitnesscalc_service import FitnessCalc
from logistics.services.bin_packing_services.mutation_service import Mutation
from logistics.services.bin_packing_services.nsga2_service import Nsga2
from logistics.services.bin_packing_services.population_service import PopulationService
from logistics.services.bin_packing_services.recombination_service import Recombination
from logistics.services.bin_packing_services.survivor_selection_service import SurvivorSelection
from logistics.services.bin_packing_services.visualize_plotly_service import VisualizePlotlyService


class CalculateBinPackingService:
    
    @staticmethod
    def calculate_bin_packing():
        NUM_OF_ITERATIONS = 1
        NUM_OF_INDIVIDUALS = 36
        NUM_OF_GENERATIONS = 200
        PC = int(0.8 * NUM_OF_INDIVIDUALS)
        PM1 = 0.2
        PM2 = 0.02
        K = 2
        ROTATIONS = 2  # 1 or 2 or 6
        
        print("Running Problem Set")
        print(tabulate([['Generations', NUM_OF_GENERATIONS], ['Individuals', NUM_OF_INDIVIDUALS],
                            ['Rotations', ROTATIONS], ['Crossover Prob.', PC], ['Mutation Prob1', PM1],
                            ['Mutation Prob2', PM2], ['Tournament Size', K]], headers=['Parameter', 'Value'],
                        tablefmt="github"))
        # final_boxes,packages = p_p.calculate_box_informations(products,pallets) burada final boxes lazim
        
        # Extracting inputs from the excel file
        data = {} #burada datayi benzet ## truck.TruckData(truck_dimension=[1198,235,120],number=len(final_boxes),boxes=final_boxes,solution=[],total_value=1800)
        truck_dimension = data.truck_dimension
        packages = data.solution
        boxes = data.boxes
        total_value = data.total_value
        box_count = data.number
        box_params = {}
        
        for index in range(len(boxes)):
            box_params[index] = boxes[index]
        
            # Storing the average values over every single iteration
        average_vol = []
        average_num = []
        average_value = []
        
        for i in range(NUM_OF_ITERATIONS):
            population = PopulationService.generate_pop(box_params, NUM_OF_INDIVIDUALS, ROTATIONS)
            
            gen = 0
            average_fitness = []
            
            while gen < NUM_OF_GENERATIONS:
                population, fitness = FitnessCalc.evaluate(population, truck_dimension, box_params, total_value)
                population = Nsga2.rank(population, fitness)
                offsprings = Recombination.crossover(deepcopy(population), PC, k=K)
                offsprings = Mutation.mutate(offsprings, PM1, PM2, ROTATIONS)
                population = SurvivorSelection.select(population, offsprings, truck_dimension, box_params, total_value,
                                        NUM_OF_INDIVIDUALS)
                average_fitness.append(CalculateBinPackingService.calc_average_fitness(population))
                gen += 1    
            results = []

        # Storing the final Rank 1 solutions
            for key, value in population.items(): 
                if value['Rank'] == 1:
                    results.append(value['result'])

            # Plot using plotly
            #color_index = vis.draw_solution(pieces=packages)
            color_index = VisualizePlotlyService.draw_solution(pieces=results[0],truck_dimension=truck_dimension)
            
            VisualizePlotlyService.draw(results, color_index)
            
            print(tabulate(
            [['Problem Set', 0], ['Runs', NUM_OF_ITERATIONS], ['Avg. Volume%', sum(average_vol) / len(average_vol)],
                ['Avg. Number%', sum(average_num) / len(average_num)],
                ['Avg. Value%', sum(average_value) / len(average_value)]],
            headers=['Parameter', 'Value'], tablefmt="github"))
            
        

    @staticmethod
    def calc_average_fitness(individuals):
        fitness_sum = [0.0, 0.0, 0.0]
        count = 0
        for key, value in individuals.items():
            if value['Rank'] == 1:
                count += 1
                fitness_sum[0] += value['fitness'][0]
                fitness_sum[1] += value['fitness'][1]
                fitness_sum[2] += value['fitness'][2]
        average = [number / count for number in fitness_sum]
        return average