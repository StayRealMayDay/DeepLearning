# -*-coding:utf-8-*-
from functools import reduce

class ConstNode(object):
    def __init__(self, node_index, layer_index):
        self.layer_index = layer_index
        self.node_index = node_index
        self.upstream = []
        self.downstream = []
        self.output = 1
        self.delta = 0.0

    def append_downstream_connection(self, conn):
        """
        add a connection to the downstream connection
        :param conn:
        :return:
        """
        self.downstream.append(conn)

    def append_upstream_connection(self, conn):
        """
        add a connection to the upstream connection
        :param conn:
        :return:
        """
        self.upstream.append(conn)

    def calculate_hidden_layer_delta(self):
        """
        :return:
        """
        downstream_delta = reduce(lambda ret, conn: ret + conn.downstream_node.delta * conn.weight, self.downstream, 0.0)

        self.delta = self.output * (1 - self.output) * downstream_delta

    def __str__(self):
        """
        print the node information
        :return:
        """
        node_str = '%u-%u: output: 1' % (self.layer_index, self.node_index)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.downstream, '')
        return node_str + '\n\tdownstream:' + downstream_str