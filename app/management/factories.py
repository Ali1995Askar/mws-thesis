class HeuristicsFactory:
    algorithms = {
        'STATIC_MIN_DEGREE': 'STATIC_MIN_DEGREE',
        'DYNAMIC_MIN_DEGREE': 'DYNAMIC_MIN_DEGREE',
        'LIMIT_MIN_DEGREE': 'LIMIT_MIN_DEGREE',
        'SIMPLE_GREEDY': 'SIMPLE_GREEDY',
        'MONTE_CARLO': 'MONTE_CARLO',
        'RANDOMIZED_ROUNDING': 'RANDOMIZED_ROUNDING',
        'MODIFIED_GREEDY': 'MODIFIED_GREEDY',
    }

    @staticmethod
    def get_algorithms(algorithm_name: str):
        return HeuristicsFactory.algorithms[algorithm_name]
