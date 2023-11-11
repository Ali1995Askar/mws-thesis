from typing import Type
from src.solvers.max_matching.heuristics.modified_greedy import ModifiedGreedy
from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic
from src.solvers.max_matching.heuristics.min_degree.limit import Limit
from src.solvers.max_matching.heuristics.min_degree.static import Static
from src.solvers.max_matching.heuristics.min_degree.dynamic import Dynamic
from src.solvers.max_matching.heuristics.random_greedy.monte_carlo import MonteCarlo
from src.solvers.max_matching.heuristics.random_greedy.simple_greedy import SimpleGreedy


class Factory:
    algorithms = {
        'STATIC_MIN_DEGREE': Static,
        'DYNAMIC_MIN_DEGREE': Dynamic,
        'LIMIT_MIN_DEGREE': Limit,
        'SIMPLE_GREEDY': SimpleGreedy,
        'MONTE_CARLO': MonteCarlo,
        'MODIFIED_GREEDY': ModifiedGreedy,
    }

    @staticmethod
    def get_algorithms(algorithm_name: str) -> Type[AbstractHeuristic]:
        return Factory.algorithms[algorithm_name.upper()]
