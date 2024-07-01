from typing import List
import networkx as nx
import matplotlib.pyplot as plt

from graph_dependencies.database import DatabaseConnection, PostgresConnection

DEPENDENCY_QUERY = """
                    select j.job_id, d.dep_job_id
                    from job j
                    left join job_dependencies d
                    on j.job_id = d.job_id
                    """


class JobDependencies:

    _dependency_graph: nx.DiGraph = None

    def __init__(self, db_connection: DatabaseConnection):
        self._db_connection = db_connection
        self._dependency_graph: nx.DiGraph = None

    # def get_connection(self):
    #     return self._db_connection

    def get_dependency_graph(self) -> nx.DiGraph:
        if self._dependency_graph is None:
            self._dependency_graph = self._build_dependency_graph_from_db()
        return self._dependency_graph

    def _build_dependency_graph_from_db(self) -> nx.DiGraph:
        rows = self._db_connection.extract_records(self, DEPENDENCY_QUERY)
        gr = nx.MultiDiGraph()
        for row in rows:
            job_id = row[0]
            dependency_id = row[1]
            gr.add_node(job_id)
            if dependency_id is not None:
                gr.add_edge(
                    job_id, dependency_id, label=f"{job_id} depends on {dependency_id}"
                )
        return gr

    def create_job_list(self) -> List[str]:
        job_lst = []
        leaf_nodes = [
            node
            for node in self.get_dependency_graph().nodes()
            if self.get_dependency_graph().out_degree(node) == 0
        ]

        while leaf_nodes:
            leaf = leaf_nodes.pop(0)
            job_lst.append(leaf)

            predecessors = list(self.get_dependency_graph().predecessors(leaf))
            self.get_dependency_graph().remove_node(leaf)

            for predecessor in predecessors:
                if self.get_dependency_graph().out_degree(predecessor) == 0:
                    leaf_nodes.append(predecessor)

        return job_lst

    def draw_dependencies(self):
        nx.draw(
            self.get_dependency_graph(),
            with_labels=True,
            font_weight="bold",
            # arrowstyle="->",
            edge_color="grey",
            node_color="red",
        )
        plt.show()


if __name__ == "__main__":
    postgresConnection = PostgresConnection(
        database="postgres", user="postgres", password="postgres", host="localhost"
    )
    jd = JobDependencies(postgresConnection)
    jd.draw_dependencies()
    job_list = jd.create_job_list()
    print(f"job list: {job_list}")
