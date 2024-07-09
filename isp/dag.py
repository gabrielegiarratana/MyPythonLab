from typing import List
import networkx as nx
import matplotlib.pyplot as plt

from isp import database


class Job:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return f"{self._name}"

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        if isinstance(other, Job):
            return self._name == other._name
        return False


class DAG:

    def __init__(self, dependency_graph: nx.DiGraph):
        self._dependency_graph: nx.DiGraph = dependency_graph

    @staticmethod
    def from_db(db_connection: database.DatabaseConnection):
        dependency_query = """
                                    select j.job_id, d.dep_job_id
                                    from job j
                                    left join job_dependencies d
                                    on j.job_id = d.job_id
                                    """
        rows = db_connection.extract_records(dependency_query)
        gr = nx.MultiDiGraph()
        for row in rows:
            job_id: str = row[0]
            job: Job = Job(job_id)
            job_dep_id: str = row[1]
            gr.add_node(job)
            if job_dep_id is not None:
                job_dep: Job = Job(job_dep_id)
                gr.add_edge(job, job_dep, label=f"{job_id} depends on {job_dep_id}")
        return DAG(gr)

    @property
    def dependency_graph(
        self,
    ) -> nx.DiGraph:
        return self._dependency_graph

    @dependency_graph.setter
    def dependency_graph(self, dependency_graph):
        self._dependency_graph = dependency_graph

    def node_list(self) -> List[str]:
        job_lst = []
        leaf_nodes = [
            node
            for node in self._dependency_graph.nodes()
            if self._dependency_graph.out_degree(node) == 0
        ]

        while leaf_nodes:
            leaf = leaf_nodes.pop(0)
            job_lst.append(leaf)

            predecessors = list(self._dependency_graph.predecessors(leaf))
            self._dependency_graph.remove_node(leaf)

            for predecessor in predecessors:
                if self._dependency_graph.out_degree(predecessor) == 0:
                    leaf_nodes.append(predecessor)

        return job_lst

    def draw_dependencies(self):
        nx.draw(
            self._dependency_graph,
            with_labels=True,
            font_weight="bold",
            # arrowstyle="->",
            edge_color="grey",
            node_color="red",
        )
        plt.show()


if __name__ == "__main__":
    postgresConnection = database.PostgresConnection(
        database="postgres", user="postgres", password="postgres", host="localhost"
    )
    jd = DAG.from_db(postgresConnection)
    jd.draw_dependencies()
    job_list = jd.node_list()
    print(f"job list: {job_list}")
