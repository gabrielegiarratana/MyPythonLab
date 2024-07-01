from abc import ABC, abstractmethod
import psycopg2


class DatabaseConnection(ABC):

    def __init__(self, host: str, port: str, database: str, user: str, password: str):
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password
        self._connection = None

    def get_host(self):
        return self._host

    def get_port(self):
        return self._port

    def get_database(self):
        return self._database

    def get_user(self):
        return self._user

    def get_password(self):
        return self._password

    def get_connection(self):
        if self._connection is None:
            cn = self.connect()
            self.set_connection(cn)
        return self._connection

    def set_connection(self, connection):
        self._connection = connection

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def extract_records(self, query: str):
        pass


class PostgresConnection(DatabaseConnection):
    def __init__(self, host: str, database: str, user: str, password: str):
        super().__init__(host, "5432", database, user, password)

    def disconnect(self):
        self.get_connection().close()
        self.set_connection(None)

    def connect(self):
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
        )
        self.set_connection(conn)
        return conn

    def extract_records(self, query: str):
        cur = self.get_connection().cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        self.disconnect()
        return rows
