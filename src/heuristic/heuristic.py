from abc import abstractmethod


class Heuristic:
    @abstractmethod
    def find_matching(self):
        pass
