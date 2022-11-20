class Solver:
    graph = None
    strategy = None
    heuristic = None

    def get_heuristic(self):
        pass

    def set_heuristic(self):
        pass

    def get_strategy(self):
        pass

    def set_strategy(self):
        pass

    def _direct_graph(self):
        pass

    def _add_src_sink(self):
        pass

    def _reduce(self):
        pass

    def execute(self):
        self._reduce()
        print('Execute')
