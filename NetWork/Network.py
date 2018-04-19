# -*-coding:utf-8-*-

from NetWork.Connections import *
from NetWork.Layer import *
from NetWork.Connection import *


class Network(object):
    def __init__(self, layers):
        """
        init a network
        layers describe the numbers of node in each layer
        :param layers:
        """
        self.connections = Connections()
        self.layers = []
        layer_count = len(layers)
        node_count = 0
        for i in range(layer_count):
            self.layers.append(Layer(i, layers[i]))
        for layer in range(layer_count - 1):
            connections = [Connection(upstream_node, downstream_node) for upstream_node in self.layers[layer].nodes
                           for downstream_node in self.layers[layer + 1].nodes[:-1]]
            for conn in connections:
                self.connections.add_connection(conn)
                conn.upstream_node.append_downstream_connection(conn)
                conn.downstream_node.append_upstream_connection(conn)

    def train(self, labels, data_set, rate, iteration):
        """
        train the network
        labels is a list ,contain the correct output of each train set
        data_set is a two-dimensional array , each element is a feature of the sample
        :param labels:
        :param data_set:
        :param rate:
        :param iteration:
        :return:
        """
        for i in range(iteration):
            for d in range(len(data_set)):
                self.train_one_sample(labels[d], data_set[d], rate)

    def train_one_sample(self, label, sample, rate):

        self.predict(sample)
        self.calculate_delta(label)
        self.update_weight(rate)

    def predict(self, sample):
        """
        calculate the output of the network
        :param sample:
        :return:
        """
        self.layers[0].set_output(sample)
        for i in range(1, len(self.layers)):
            self.layers[i].calculate_output()
        return list(map(lambda node: node.output, self.layers[-1].nodes[:-1]))

    def calculate_delta(self, label):
        """
        calculate the delta for all node in the network
        :param label:
        :return:
        """
        output_node = self.layers[-1].nodes
        for i in range(label):
            output_node[i].calculate_output_layer_delta(label)
        for layer in self.layers[-2::-1]:
            for node in layer.nodes:
                node.calculate_hidden_layer_delta()

    def update_weight(self, rate):
        """
        renew weight of all connection
        :param rate:
        :return:
        """
        for connection in self.connections.connections:
            connection.update_weight(rate)

    def calculate_gradient(self):
        """
        calculate gradient
        :return:
        """
        for conn in self.connections.connections:
            conn.calculate_gradient()

    def get_gradient(self, label, sample):
        """
        get the network's gradient in every connection under one sample
        :param label:
        :param sample:
        :return:
        """
        self.predict(sample)
        self.calculate_delta(label)
        self.calculate_gradient()

    def gradient_check(self, sample_feature, sample_label):
        """
        calculate the network error
        :param sample_feature:
        :param sample_label:
        :return:
        """
        """
        calculate the network error under each weight
        """
        newwork_error = lambda vec1, vec2: 0.5 * reduce(lambda a, b: a + b, list(
            map(lambda v: (v[0] - v[1]) * (v[0] - v[1]), zip(vec1, vec2))))
        """
        calculate the gradient with the sample date
        """
        self.get_gradient(sample_feature, sample_label)
        for conn in self.connections.connections:
            """
            get the gradient of each connection
            """
            actual_gradient = conn.get_gradient()
            """
            change a small value of the weight
            """
            epsilon = 0.0001
            conn.weight += epsilon
            """
            calculate the error
            """
            error1 = newwork_error(self.predict(sample_feature), sample_label)
            """
            again
            """
            conn.weight -= 2 * epsilon
            error2 = newwork_error(self.predict(sample_feature), sample_label)
            """
            calculate the gradient
            """
            expected_gradient = (error2 - error1) / (2 * epsilon)

            print('expected gradient: \t%f\n actual gradient: \t%f' % (
                expected_gradient, actual_gradient))
