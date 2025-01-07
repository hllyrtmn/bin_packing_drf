import plotly.graph_objects as go
import numpy as np
import plotly.colors
from plotly.subplots import make_subplots

class VisualizePlotlyService:
    
    pallete = ['darkgreen', 'tomato', 'yellow', 'darkblue', 'darkviolet', 'indianred', 'yellowgreen', 'mediumblue', 'cyan',
            'black', 'indigo', 'pink', 'lime', 'sienna', 'plum', 'deepskyblue', 'forestgreen', 'fuchsia', 'brown',
            'turquoise', 'aliceblue', 'blueviolet', 'rosybrown', 'powderblue', 'lightblue', 'skyblue', 'lightskyblue',
            'steelblue', 'dodgerblue', 'lightslategray', 'lightslategrey', 'slategray',
            'slategrey', 'lightsteelblue', 'cornflowerblue', 'royalblue', 'ghostwhite', 'lavender',
            'midnightblue', 'navy', 'darkblue', 'blue', 'slateblue', 'darkslateblue',
            'mediumslateblue', 'mediumpurple', 'rebeccapurple', 'darkorchid',
            'darkviolet', 'mediumorchid']
    color_pallete = ['lightcoral', 'firebrick', 'maroon', 'darkred', 'red',
                    'salmon', 'darksalmon', 'coral', 'orangered', 'lightsalmon', 'chocolate',
                    'saddlebrown',
                    'sandybrown', 'olive', 'olivedrab', 'darkolivegreen', 'greenyellow',
                    'chartreuse', 'lawngreen',
                    'darkseagreen', 'palegreen', 'lightgreen', 'limegreen',
                    'green', 'seagreen', 'mediumseagreen', 'springgreen', 'mediumspringgreen',
                    'mediumaquamarine', 'aquamarine', 'lightseagreen', 'mediumturquoise',
                    'lightcyan', 'paleturquoise', 'darkslategray', 'darkslategrey', 'teal', 'darkcyan', 'aqua', 'cyan',
                    'darkturquoise', 'cadetblue', 'thistle', 'violet', 'purple', 'darkmagenta',
                    'magenta', 'orchid', 'mediumvioletred', 'deeppink', 'hotpink', 'lavenderblush', 'palevioletred',
                    'crimson', 'lightpink']

    @staticmethod
    def cube_data(position3d, size=(1, 1, 1)):
        # position3d - 3-list or array of shape (3,) that represents the point of coords (x, y, 0), where a bar is placed
        # size = a 3-tuple whose elements are used to scale a unit cube to get a paralelipipedic bar
        # returns - an array of shape(8,3) representing the 8 vertices of  a bar at position3d

        cube = np.array([[0, 0, 0],
                        [1, 0, 0],
                        [1, 1, 0],
                        [0, 1, 0],
                        [0, 0, 1],
                        [1, 0, 1],
                        [1, 1, 1],
                        [0, 1, 1]], dtype=float)  # the vertices of the unit cube

        cube *= np.asarray(size)  # scale the cube to get the vertices of a parallelipipedic bar
        cube += np.asarray(position3d)  # translate each  bar on the directio OP, with P=position3d
        return cube

    @staticmethod
    def triangulate_cube_faces(positions, sizes=None):
        # positions - array of shape (N, 3) that contains all positions in the plane z=0, where a histogram bar is placed
        # sizes -  array of shape (N,3); each row represents the sizes to scale a unit cube to get a bar
        # returns the array of unique vertices, and the lists i, j, k to be used in instantiating the go.Mesh3d class

        if sizes is None:
            sizes = [(1, 1, 1)] * len(positions)
        else:
            if isinstance(sizes, (list, np.ndarray)) and len(sizes) != len(positions):
                raise ValueError('Your positions and sizes lists/arrays do not have the same length')

        all_cubes = [VisualizePlotlyService.cube_data(pos, size) for pos, size in zip(positions, sizes) if size[2] != 0]
        p, q, r = np.array(all_cubes).shape

        # extract unique vertices from the list of all bar vertices
        vertices, ixr = np.unique(np.array(all_cubes).reshape(p * q, r), return_inverse=True, axis=0)
        # for each bar, derive the sublists of indices i, j, k assocated to its chosen  triangulation
        I = []
        J = []
        K = []

        for k in range(len(all_cubes)):
            I.extend(np.take(ixr, [8 * k, 8 * k + 2, 8 * k, 8 * k + 5, 8 * k, 8 * k + 7, 8 * k + 5, 8 * k + 2, 8 * k + 3,
                                8 * k + 6, 8 * k + 7, 8 * k + 5]))
            J.extend(np.take(ixr, [8 * k + 1, 8 * k + 3, 8 * k + 4, 8 * k + 1, 8 * k + 3, 8 * k + 4, 8 * k + 1, 8 * k + 6,
                                8 * k + 7, 8 * k + 2, 8 * k + 4, 8 * k + 6]))
            K.extend(np.take(ixr, [8 * k + 2, 8 * k, 8 * k + 5, 8 * k, 8 * k + 7, 8 * k, 8 * k + 2, 8 * k + 5, 8 * k + 6,
                                8 * k + 3, 8 * k + 5, 8 * k + 7]))

        return vertices, I, J, K  # triangulation vertices and I, J, K for mesh3d
    
    @staticmethod
    def draw_test(data):
        fig = go.Figure()

        for item in data:
            x, y, z, dx, dy, dz = item
            fig.add_trace(go.Mesh3d(
                x=[x, x + dx, x + dx, x, x, x + dx, x + dx, x],
                y=[y, y, y + dy, y + dy, y, y, y + dy, y + dy],
                z=[z, z, z, z, z + dz, z + dz, z + dz, z + dz],
                i=[0, 0, 0, 1, 1, 2, 2, 3],
                j=[1, 2, 3, 2, 3, 3, 0, 0],
                k=[2, 3, 0, 3, 0, 0, 1, 1],
                opacity=0.5
            ))

        fig.update_layout(scene=dict(
            xaxis=dict(title='X Ekseni', range=[0, 1200]),
            yaxis=dict(title='Y Ekseni', range=[0, 250]),
            zaxis=dict(title='Z Ekseni', range=[0, 150]),
            aspectratio=dict(x=4, y=1, z=1)
        ))

        fig.show()

    @staticmethod
    def draw_solution(pieces,truck_dimension):
        positions = []
        sizes = []
        colors = []
        sorted_size = []
        texts = []
        for i, each in enumerate( pieces):
            positions.append(each[0:3])
            sizes.append(each[3:6])
            sorted_size.append(set(each[3:6]))
            
            texts.append(f'Palet {each[6]}<br>Ağırlık: {each[7]} kg<br>X: {each[3]} <br>Y: {each[4]}<br>Z: {each[5]}')

        colors =  plotly.colors.qualitative.Pastel1 + plotly.colors.qualitative.Pastel2 + plotly.colors.qualitative.Set3
        color_index = [sorted_size, colors]
        vertices, I, J, K = VisualizePlotlyService.triangulate_cube_faces(positions, sizes=sizes)
        
        hovertexts_expanded = []
        for text in texts:
            hovertexts_expanded.extend([text] * 12)  # Her kutu için 12 yüz
            
        X, Y, Z = vertices.T
        colors2 = [val for val in colors for _ in range(12)]
        mesh3d = go.Mesh3d(
        x=X, y=Y, z=Z, i=I, j=J, k=K,
        facecolor=colors2,
        flatshading=True,
        opacity=1,
        hovertext=hovertexts_expanded,
        hovertemplate='<b>%{hovertext}</b><br>' +
                            '<extra></extra>')
       
        annotations = []
        for pos, size, text in zip(positions, sizes, texts):
            annotations.append(go.Scatter3d(
                x=[pos[0] + size[0] / 2],  # X ekseninde kutunun merkezine hizala
                y=[pos[1] + size[1] / 2],  # Y ekseninde kutunun merkezine hizala
                z=[pos[2] + size[2]],  # Z ekseninde kutunun tam üst yüzeyine hizala
                mode='text',
                text=[text],
                textposition="middle center",
                name=f'{text}',  # Sağ panelde görülecek isim
                showlegend=True,  # Sağ tarafta gösterilsin
                marker=dict(size=6, color='black', symbol='circle')
            ))
        
        x_range = [min(X), truck_dimension[0]]
        y_range = [min(Y), truck_dimension[1]]
        z_range = [min(Z), truck_dimension[2]]
        
        max_range = max(truck_dimension[0], truck_dimension[1], truck_dimension[2])
        aspect_ratio = {
            'x': truck_dimension[0] / max_range,
            'y': truck_dimension[1] / max_range,
            'z': truck_dimension[2] / max_range,
        }
        
        layout = go.Layout(autosize=True,
                           margin=dict(l=0,r=0,b=0,t=40),
                            title_text='Truck Loading True Solution',
                            title_x=0.5,
                            scene=dict(
                            xaxis=dict(title='X Ekseni '+ str(int(truck_dimension[0])), range=x_range,showticklabels=False,showgrid=False,zeroline=False),
                            yaxis=dict(title='Y Ekseni '+ str(int(truck_dimension[1])), range=y_range,showticklabels=False,showgrid=False,zeroline=False),
                            zaxis=dict(title='Z Ekseni '+ str(int(truck_dimension[2])), range=z_range,showticklabels=False,showgrid=False,zeroline=False),
                            aspectratio=aspect_ratio,
                            camera=dict(eye=dict(x=0, y=0, z=0.7),up=dict(x=0, y=-1, z=0))  # 90 derece sola döndür
        ))
        fig = go.Figure(data=[mesh3d] + annotations, layout=layout)
        fig.show(config={'responsive':True,'displayModeBar':True,'scrollZoom': False,'staticPlot': False ,'modeBarButtonsToRemove': [
        'zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d',
        'autoScale2d', 'resetScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian',
        'orbitRotation', 'tableRotation', 'resetCameraDefault3d', 'resetCameraLastSave3d'
        ],  # İstenmeyen tüm butonları kaldır
        'modeBarButtonsToAdd': ['toImage'],  # Sadece PNG indirme butonunu ekle
        'toImageButtonOptions': {
            'format': 'png',  # PNG formatı
            'filename': 'truck_loading_solution'
        }})
        return color_index

    @staticmethod
    def draw(results, color_index):
        mesh = []
        clr = color_index[1]
        sorted_pieces = color_index[0]
        for pieces in results:
            positions = []
            sizes = []
            colors = []
            for each in pieces:
                positions.append(each[0:3])
                sizes.append(each[3:6])
                for i in range(len(sorted_pieces)):
                    if set(each[3:6]) == sorted_pieces[i]:
                        colors.append(clr[i])

            vertices, I, J, K = VisualizePlotlyService.triangulate_cube_faces(positions, sizes=sizes)

            X, Y, Z = vertices.T
            colors2 = [val for val in colors for _ in range(12)]
            mesh.append(go.Mesh3d(x=X, y=Y, z=Z, i=I, j=J, k=K, facecolor=colors2, flatshading=True))
        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{'type': 'surface'}, {'type': 'surface'}],
                [{'type': 'surface'}, {'type': 'surface'}]])

        # Visualize 4 Rank 1 solutions

        fig.add_trace(mesh[0],
                    row=1, col=1)

        fig.add_trace(mesh[1],
                    row=1, col=2)

        fig.add_trace(mesh[2],
                    row=2, col=1)

        fig.add_trace(mesh[3],
                    row=2, col=2)


        fig.update_layout(
            title_text='Rank 1 Solutions',
            autosize=True,
            height=1500,
            width=1500,
            title_x=0.5,
            scene=dict(
                camera_eye_x=-1.25,
                camera_eye_y=1.25,
                camera_eye_z=1.25)

        )

        fig.show()
        return color_index
