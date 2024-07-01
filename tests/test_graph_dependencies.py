from abc import ABC
import unittest
import networkx as nx
from attr.validators import disabled

from graph_dependencies.database import DatabaseConnection
from graph_dependencies.job import JobDependencies


class MockedConnection(DatabaseConnection):

    def extract_records(self, query: str):
        return [("7", "6"), ("6", "5"), ("6", "4")]


class TestJobDependencies(unittest.TestCase):


    def setUp(self):
        self.mocked_connection = MockedConnection
        self.job_dependencies = JobDependencies(self.mocked_connection)

    def test_get_dependency_graph(self):
        actual_graph = self.job_dependencies.get_dependency_graph()

        # Assert the expected result
        expected_graph = nx.MultiDiGraph()
        expected_graph.add_node("7")
        expected_graph.add_node("6")
        expected_graph.add_node("5")
        expected_graph.add_node("4")
        expected_graph.add_edge("7", "6", label="7 depends on 6")
        expected_graph.add_edge("6", "5", label="6 depends on 5")
        expected_graph.add_edge("6", "4", label="6 depends on 4")
        self.assertEqual(actual_graph.nodes, expected_graph.nodes)
        self.assertEqual(actual_graph.edges, expected_graph.edges)

    def test_create_job_list(self):
        actual_job_list = self.job_dependencies.create_job_list()
        # Assert the expected result
        expected_job_list = ["5", "4", "6", "7"]
        self.assertEqual(expected_job_list,actual_job_list)

    @unittest.skip("test temporary disabled")
    def test_draw_dependencies(self):
        self.job_dependencies.draw_dependencies()
        assert True


if __name__ == "__main__":
    unittest.main()
