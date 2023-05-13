import time
from app.utils.utils import create_csv
from networkx.algorithms.flow import edmonds_karp
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_matching.max_matching import MaxMatching
from app.src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from app.src.algorithm.max_flow.edmond_karp_algorithm import EdmondKarpAlgorithm
from app.src.algorithm.max_flow.ford_fulkerson_algorithm import FordFulkersonAlgorithm

columns_name = [
    'NUM OF NODES',
    'Density',
    'Ford-Fulkerson Result',
    'Ford-Fulkerson Execution Time',
    'Edmond-Karp Result',
    'Edmond-Karp Execution Time',
    'Dinitz Result',
    'Dinitz Execution Time',
    'Max Matching Value'
]
nodes_range = [
    # 500,
    # 1000,
    # 1500,
    # 2000,
    # 2500,
    # 3000,
    3500,
    4000,
    4500,
    5000,
    5500,
    6000,
    6500,
    7000,
    7500,
    8000,
    8500,
    9000,
    9500,
    1000
]

density_range = [
    0.0001,
    0.0002,
    0.0004,
    0.0007,
    0.001,
    0.003,
    0.005,
    0.008,
    0.01,
    0.05,
    0.1,
    0.18,
    0.25,
    0.36,
    0.42,
    0.48,
    0.56,
    0.62,
    0.68,
    0.72,
    0.78,
    0.82,
    0.88,
    0.92,
    0.98,
    1
]

if __name__ == '__main__':
    bipartite_graph = BipartiteGraph()
    max_matching = MaxMatching()

    for node in nodes_range:
        rows = []
        num_of_nodes = node
        for density in density_range:
            bipartite_graph.random_build(num_of_nodes=num_of_nodes, density=density)
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)

            # FordFulkerson Algorithm
            max_matching.set_algorithm(algorithm=FordFulkersonAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            ford_fulkerson_algorithm_execution_time = end_time - start_time
            ford_fulkerson_algorithm_value = max_matching.max_matching_value

            # EdmondKarp Algorithm
            max_matching.set_algorithm(algorithm=EdmondKarpAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            edmond_algorithm_execution_time = end_time - start_time
            edmond_algorithm_value = max_matching.max_matching_value

            # Dinitz Algorithm
            max_matching.set_algorithm(algorithm=DinitzAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            dinitz_algorithm_execution_time = end_time - start_time
            dinitz_algorithm_value = max_matching.max_matching_value

            R = edmonds_karp(max_matching.get_temp_graph(), 'source', 'sink')

            row = [
                num_of_nodes,
                density,
                ford_fulkerson_algorithm_value,
                ford_fulkerson_algorithm_execution_time,
                edmond_algorithm_value,
                edmond_algorithm_execution_time,
                dinitz_algorithm_value,
                dinitz_algorithm_execution_time,
                R.graph['flow_value']
            ]
            print(row)
            rows.append(row)
        create_csv(f'{num_of_nodes}_max_flow.csv', columns=columns_name, data=rows)

# [3500, 0.0001, 266, 0.19679784774780273, 266, 0.3451104164123535, 266, 0.47365283966064453, 266]
# [3500, 0.0002, 459, 0.6568560600280762, 459, 1.4021203517913818, 459, 1.9348835945129395, 459]
# [3500, 0.0004, 771, 1.072566032409668, 771, 2.1075758934020996, 771, 2.3316490650177, 771]
# [3500, 0.0007, 1084, 3.0500597953796387, 1084, 11.347726583480835, 1084, 5.654896259307861, 1084]
# [3500, 0.001, 1297, 1.692505121231079, 1297, 5.416130542755127, 1297, 4.240129709243774, 1297]
# [3500, 0.003, 1742, 2.164966583251953, 1742, 13.551060676574707, 1742, 7.86016321182251, 1742]
# [3500, 0.005, 1750, 1.5824611186981201, 1750, 13.975114822387695, 1750, 9.98743224143982, 1750]
# [3500, 0.008, 1750, 1.7491803169250488, 1750, 16.35775637626648, 1750, 12.541161298751831, 1750]
# [3500, 0.01, 1750, 1.714315414428711, 1750, 16.163049936294556, 1750, 16.375901460647583, 1750]
# [3500, 0.05, 1750, 4.1810102462768555, 1750, 85.32566213607788, 1750, 84.47599124908447, 1750]
# [3500, 0.1, 1750, 7.320935487747192, 1750, 99.1957619190216, 1750, 149.17749285697937, 1750]
# [3500, 0.18, 1750, 11.895135879516602, 1750, 152.3448269367218, 1750, 229.32651662826538, 1750]
# [3500, 0.25, 1750, 16.4937584400177, 1750, 204.04728364944458, 1750, 351.3894317150116, 1750]
# [3500, 0.36, 1750, 23.27471947669983, 1750, 270.00716066360474, 1750, 438.0278010368347, 1750]
# [3500, 0.42, 1750, 17.111949682235718, 1750, 287.4039418697357, 1750, 401.62602972984314, 1750]