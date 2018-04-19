# -*-coding:utf-8-*-
from NetWork.Node import *
from NetWork.ConstNode import *


class Layer(object):
    def __init__(self, node_count, layer_index):
        """
        init the layer and the node of this layer
        :param node_count:
        :param layer_index:
        """
        self.layer_index = layer_index
        self.nodes = []
        for i in range(node_count):
            self.nodes.append(Node(i, layer_index))
        self.nodes.append(ConstNode(node_count, layer_index))

    def set_output(self, data):
        """
        if this layer is input layer
        this function will be needed
        :param data:
        :return:
        """
        for i in range(len(data)):
            self.nodes[i].set_output(data[i])

    def calculate_output(self):
        """
        calculate the node output
        :return:
        """
        for node in self.nodes:
            node.calculate_output()

    def display_layer_information(self):
        """
        print the node information of this layer
        :return:
        """
        for node in self.nodes:
            print(node)
