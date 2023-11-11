from core.utils import my_import


class HeuristicFactory:
    heuristics_algorithms = {
        'LIMIT': "src.solvers.max_matching.heuristics.min_degree.limit.Limit",
        'STATIC': "src.solvers.max_matching.heuristics.min_degree.static.Static",
        'DYNAMIC': "src.solvers.max_matching.heuristics.min_degree.dynamic.Dynamic",

        'RED12': "src.solvers.max_matching.heuristics.random_greedy.red12.RED12",
        'MIN_GREEDY': "src.solvers.max_matching.heuristics.random_greedy.min_greedy.MinGreedy",
        'MONTE_CARLO': "src.solvers.max_matching.heuristics.random_greedy.monte_carlo.MonteCarlo",
        'SIMPLE_GREEDY': "src.solvers.max_matching.heuristics.random_greedy.simple_greedy.SimpleGreedy",

        'MODIFIED_GREEDY': "src.solvers.max_matching.heuristics.modified_greedy.ModifiedGreedy",
    }

    @staticmethod
    def get_algo_inst_by_name(algo_name):
        instance = my_import(HeuristicFactory.heuristics_algorithms[algo_name.upper()])
        return instance
