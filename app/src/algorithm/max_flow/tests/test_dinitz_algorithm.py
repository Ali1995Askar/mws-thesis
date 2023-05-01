from app.src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm


class TestDinitzAlgorithm:

    def test_solver(self,
                    ex_graph_1,
                    ex_graph_2,
                    ex_graph_3,
                    ex_graph_4,
                    ex_graph_5,
                    ex_graph_6,
                    ex_graph_7,
                    ex_graph_8,
                    ex_graph_9,
                    ex_graph_10,
                    ):
        inst = DinitzAlgorithm(graph=ex_graph_1, source=1, sink=3)
        assert inst.find_max_flow()[0] == 5

        inst = DinitzAlgorithm(graph=ex_graph_2, source=1, sink=3)
        assert inst.find_max_flow()[0] == 0

        inst = DinitzAlgorithm(graph=ex_graph_3, source=0, sink=3)
        assert inst.find_max_flow()[0] == 1

        inst = DinitzAlgorithm(graph=ex_graph_4, source=0, sink=3)
        assert inst.find_max_flow()[0] == 3
        #
        # inst = DinitzAlgorithm(graph=ex_graph_5, source=1, sink=3)
        # assert inst.find_max_flow()[0] == 5
        #
        # inst = DinitzAlgorithm(graph=ex_graph_6, source=1, sink=3)
        # assert inst.find_max_flow()[0] == 5
        #
        # inst = DinitzAlgorithm(graph=ex_graph_7, source=1, sink=3)
        # assert inst.find_max_flow()[0] == 5
        #
        # inst = DinitzAlgorithm(graph=ex_graph_8, source=1, sink=3)
        # assert inst.find_max_flow()[0] == 5
        #
        # inst = DinitzAlgorithm(graph=ex_graph_9, source=1, sink=3)
        # assert inst.find_max_flow()[0] == 5
        #
        # inst = DinitzAlgorithm(graph=ex_graph_10, source=1, sink=3)
        # assert inst.find_max_flow()[0] == 5
