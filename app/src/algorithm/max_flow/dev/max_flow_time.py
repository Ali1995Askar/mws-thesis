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
    # 3500,
    # 4000,
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

# [4000, 0.0001, 342, 0.08230352401733398, 342, 0.16146016120910645, 342, 0.18039822578430176, 342]
# [4000, 0.0002, 583, 0.2240467071533203, 583, 0.4852111339569092, 583, 0.5631170272827148, 583]
# [4000, 0.0004, 958, 0.657888650894165, 958, 1.6346704959869385, 958, 1.6788127422332764, 958]
# [4000, 0.0007, 1325, 1.3173110485076904, 1325, 4.314401388168335, 1325, 3.268646001815796, 1325]
# [4000, 0.001, 1569, 1.8316013813018799, 1569, 7.281604766845703, 1569, 4.9266133308410645, 1569]
# [4000, 0.003, 1991, 1.9558789730072021, 1991, 15.86857795715332, 1991, 10.952312469482422, 1991]
# [4000, 0.005, 2000, 3.4280471801757812, 2000, 18.96335244178772, 2000, 13.303032159805298, 2000]
# [4000, 0.008, 2000, 2.1037440299987793, 2000, 21.854512214660645, 2000, 17.65818738937378, 2000]
# [4000, 0.01, 2000, 2.2700860500335693, 2000, 23.223795175552368, 2000, 20.747437477111816, 2000]
# [4000, 0.05, 2000, 3.986605167388916, 2000, 59.92794680595398, 2000, 78.65480470657349, 2000]
# [4000, 0.1, 2000, 6.552388906478882, 2000, 99.45560717582703, 2000, 151.01916122436523, 2000]
# [4000, 0.18, 2000, 11.054867267608643, 2000, 163.41168069839478, 2000, 264.8463788032532, 2000]
# [4000, 0.25, 2000, 15.44071912765503, 2000, 219.86014676094055, 2000, 362.04367780685425, 2000]
# [4000, 0.36, 2000, 19.704140424728394, 2000, 305.97892904281616, 2000, 517.4761500358582, 2000]
# [4000, 0.42, 2000, 25.39500594139099, 2000, 353.4492313861847, 2000, 663.0425453186035, 2000]
# [4000, 0.48, 2000, 30.491372108459473, 2000, 395.68132853507996, 2000, 687.1493966579437, 2000]
