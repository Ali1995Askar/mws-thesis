from src.solvers.max_matching.heuristics.modified_greedy import ModifiedGreedy
from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic
from src.solvers.max_matching.heuristics.min_degree.limit import LimitMinDegreeHeuristic
from src.solvers.max_matching.heuristics.min_degree.static import StaticMinDegreeHeuristic
from src.solvers.max_matching.heuristics.min_degree.dynamic import DynamicMinDegreeHeuristic

from src.solvers.max_matching.heuristics.random_greedy.monte_carlo import MonteCarloHeuristic
from src.solvers.max_matching.heuristics.random_greedy.simple_greedy import SimpleGreedyHeuristic
from src.solvers.max_matching.heuristics.random_greedy.randomized_rounding import RandomizedRoundingHeuristic


class HeuristicsFactory:
    algorithms = {
        'STATIC_MIN_DEGREE': StaticMinDegreeHeuristic,
        'DYNAMIC_MIN_DEGREE': DynamicMinDegreeHeuristic,
        'LIMIT_MIN_DEGREE': LimitMinDegreeHeuristic,
        'SIMPLE_GREEDY': SimpleGreedyHeuristic,
        'MONTE_CARLO': MonteCarloHeuristic,
        'RANDOMIZED_ROUNDING': RandomizedRoundingHeuristic,
        'MODIFIED_GREEDY': ModifiedGreedy,
    }

    @staticmethod
    def get_algorithms(algorithm_name: str) -> AbstractHeuristic:
        return HeuristicsFactory.algorithms[algorithm_name]
