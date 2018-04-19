# -*-coding:utf-8-*-


class Connection(object):
    def __init__(self):
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def display_all_connections(self):
        for conn in self.connections:
            print(conn)
