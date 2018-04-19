# -*-coding:utf-8-*-
import random
from numpy import *
from functools import reduce


def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))


class Node(object):
    def __init__(self, node_index, layer_index):
        """
        create the node object
        record the node index and the layer index
        :param node_index:
        :param layer_index:
        """
        self.node_index = node_index
        self.layer_index = layer_index
        self.downstream = []
        self.upstream = []
        self.output = 0.0
        self.delta = 0.0

    def set_output(self, output):
        """
        set the output of this node , if this node belongs to input layer, this function will be used.
        :param output:
        :return:
        """
        self.output = output

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

    def calculate_output(self):
        """
        calculate the output of this node
        :return:
        """
        output = reduce(lambda ret, conn: ret + conn.upstream_node.output * conn.weight, self.upstream, 0.0)

        self.output = sigmoid(output)

    def calculate_hidden_layer_delta(self):
        """
        calculate hidden layer delta
        :return:
        """
        downstream_delta = reduce(lambda ret, conn: ret + conn.downstream_node.delta * conn.weight, self.downstream, 0.0)
        self.delta = self.output * (1 - self.output) * downstream_delta

    def calculate_output_layer_delta(self, label):
        """
        calculate output layer delta
        :param label:
        :return:
        """
        self.delta = self.output * (1 - self.output) * (label - self.output)

    def __str__(self):
        """
        print node information
        :return:
        """
        node_str = '%u-%u: output: %f delta: %f' % (self.layer_index, self.node_index, self.output, self.delta)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.downstream, '')
        upstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.upstream, '')
        return node_str + '\n\tdownstream:' + downstream_str + '\n\tupstream:' + upstream_str