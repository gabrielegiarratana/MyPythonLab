import unittest
from abc import ABC

import networkx as nx

from isp.dag import DAG, Job
from isp.database import DatabaseConnection


class MockedConnection(DatabaseConnection):

    def __init__(self):
        super().__init__("", "", "", "", "")

    def extract_records(self, query: str):
        return [("7", "6"), ("6", "5"), ("6", "4")]

    def connect(self):
        pass

    def disconnect(self):
        pass


class TestDAG(unittest.TestCase):

    job7 = Job("7")
    job6 = Job("6")
    job5 = Job("5")
    job4 = Job("4")

    def setUp(self):
        mocked_connection = MockedConnection()
        self.test_dag: DAG = DAG.from_db(mocked_connection)

    def test_get_dependency_graph(self):
        actual_graph: nx.DiGraph = self.test_dag.dependency_graph
        # Assert the expected result
        expected_graph = nx.MultiDiGraph()

        jobs = [self.job7, self.job6, self.job5, self.job4]
        map(lambda j: expected_graph.add_node(j), jobs)
        expected_graph.add_edge(self.job7, self.job6, label="7 depends on 6")
        expected_graph.add_edge(self.job6, self.job5, label="6 depends on 5")
        expected_graph.add_edge(self.job6, self.job4, label="6 depends on 4")
        self.assertEqual(actual_graph.nodes, expected_graph.nodes)
        self.assertEqual(actual_graph.edges, expected_graph.edges)

    def test_node_list(self):
        actual_job_list = self.test_dag.node_list()
        # Assert the expected result
        expected_job_list = [self.job5, self.job4, self.job6, self.job7]
        self.assertEqual(expected_job_list, actual_job_list)

    @unittest.skip("test temporary disabled")
    def test_draw_dependencies(self):
        self.test_dag.draw_dependencies()
        assert True


if __name__ == "__main__":
    unittest.main()
