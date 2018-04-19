# -*-coding:utf-8-*-
import random


class Connection(object):
    """
    init a connection
    include a upstream node and a downstream node
    init the weight with a very small random value
    """
    def __init__(self, upstream_node, downstream_node):
        self.upstream_node = upstream_node
        self.downstream_node = downstream_node
        self.weight = random.uniform(-0.1, 0.1)
        self.gradient = 0.0

    def calculate_gradient(self):
        """
        calculate the gradient
        :return:
        """
        self.gradient = self.upstream_node.output * self.downstream_node.delta

    def get_gradient(self):
        """
        :return the gradient
        :return:
        """
        return self.gradient

    def update_weight(self, rate):
        """
        update the weight
        :param rate:
        :return:
        """
        self.calculate_gradient()
        self.weight += rate * self.gradient

    def __str__(self):
        """
        print the connection information
        :return:
        """
        return '(%u-%u) -> (%u-%u) = %f' % (
            self.upstream_node.layer_index,
            self.upstream_node.node_index,
            self.downstream_node.layer_index,
            self.downstream_node.node_index,
            self.weight)