# -*-coding:utf-8-*-
from functools import reduce
class Perceptron(object):
    def __init__(self, input_number, activator):
        """
        init the perceptron and set the number of parameters and the active function
        the type of the active function is double -> double
        :param input_number:
        :param activator:
        """
        self.activator = activator
        """
        init the weight vector to zero
        """
        self.weights = [0.0 for _ in range(input_number)]
        """
        set the bias term to zero
        """
        self.bias = 0.0

    def __str__(self):
        """
        print the learned weight and bias
        :return:
        """
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    def predic(self, input_vector):
        """
        input vector then output the result of the perceptron
        :param input_vector:
        :return:
        """
        """
        pack the input_vector[x1, x2, x3,...] and weights[w1, w2, w3, ...] together
        then turn it into [(x1,w1),(x2, w2),...]
        the use map function to calculate [x1 * w1, x2 * w2, ...]
        at last use the reduce function to make the sum
        """
        return self.activator(
            reduce(lambda a, b: a + b, map(lambda x_w: x_w[0] * x_w[1], zip(input_vector, self.weights)), 0.0) + self.bias
        )

    def train(self, input_vectors, labels, iteration, rate):
        """
        input train set : a group of vectors and labels correspond to it ana train times and learn rate
        :param input_vectors:
        :param lbaels:
        :param iteration:
        :param rate:
        :return:
        """
        for i in range(iteration):
            self._one_iteration(input_vectors, labels, rate)


    def _one_iteration(self, input_vectors, labels, rate):
        samples = zip(input_vectors, labels)

        for (input_vector, label) in samples:

            output = self.predic(input_vector)

            self._update_weights(input_vector, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
