from app.src.algorithm.max_flow.ford_fulkerson_algorithm import FordFulkersonAlgorithm


class TestFordFulkersonAlgorithm:

    def test_max_flow_ex_1(self, ex_graph_1):
        inst = FordFulkersonAlgorithm(graph=ex_graph_1, source=1, sink=3)
        assert inst.find_max_flow()[0] == 5
        print(inst.find_max_flow()[1])

    def test_max_flow_ex_2(self, ex_graph_2):
        inst = FordFulkersonAlgorithm(graph=ex_graph_2, source=1, sink=3)
        assert inst.find_max_flow()[0] == 0

    def test_max_flow_ex_3(self, ex_graph_3):
        inst = FordFulkersonAlgorithm(graph=ex_graph_3, source=1, sink=3)
        assert inst.find_max_flow()[0] == 1

    def test_max_flow_ex_4(self, ex_graph_4):
        inst = FordFulkersonAlgorithm(graph=ex_graph_4, source=0, sink=3)
        assert inst.find_max_flow()[0] == 3

    def test_max_flow_ex_5(self, ex_graph_5):
        inst = FordFulkersonAlgorithm(graph=ex_graph_5, source=0, sink=3)
        assert inst.find_max_flow()[0] == 5

    def test_max_flow_ex_6(self, ex_graph_6):
        inst = FordFulkersonAlgorithm(graph=ex_graph_6, source=0, sink=3)
        assert inst.find_max_flow()[0] == 1

    def test_max_flow_ex_7(self, ex_graph_7):
        inst = FordFulkersonAlgorithm(graph=ex_graph_7, source=0, sink=2)
        assert inst.find_max_flow()[0] == 0

    def test_max_flow_ex_8(self, ex_graph_8):
        inst = FordFulkersonAlgorithm(graph=ex_graph_8, source=0, sink=1)
        assert inst.find_max_flow()[0] == 3

    def test_max_flow_ex_9(self, ex_graph_9):
        inst = FordFulkersonAlgorithm(graph=ex_graph_9, source=0, sink=2)
        assert inst.find_max_flow()[0] == 4.5

    def test_max_flow_ex_10(self, ex_graph_10):
        inst = FordFulkersonAlgorithm(graph=ex_graph_10, source=0, sink=3)
        assert inst.find_max_flow()[0] == 2

        inst = FordFulkersonAlgorithm(graph=ex_graph_10, source=0, sink=4)
        assert inst.find_max_flow()[0] == 2

    def test_max_flow_ex_11(self, ex_graph_11):
        inst = FordFulkersonAlgorithm(graph=ex_graph_11, source=0, sink=3)
        assert inst.find_max_flow()[0] == 9

        inst = FordFulkersonAlgorithm(graph=ex_graph_11, source=0, sink=4)
        assert inst.find_max_flow()[0] == 9

    def test_max_flow_ex_12(self, ex_graph_12):
        inst = FordFulkersonAlgorithm(graph=ex_graph_12, source=0, sink=999)
        assert inst.find_max_flow()[0] == 1
