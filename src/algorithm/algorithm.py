from abc import abstractmethod


class Algorithm:
    @abstractmethod
    def run(self):
        print('Run')
