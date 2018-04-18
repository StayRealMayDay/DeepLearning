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

    def predict(self, input_vector):
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
            reduce(lambda a, b: a + b, map(lambda x_w: x_w[0] * x_w[1], zip(input_vector, self.weights)),
                   0.0) + self.bias
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
        """
        iterate once to use the whole data
        :param input_vectors:
        :param labels:
        :param rate:
        :return:
        """
        """
        packing the input and the correct result together
        the label is the correct result of the output
        """
        samples = zip(input_vectors, labels)
        """
        use the rule of perceptron to renew the weight for every sample
        """
        for (input_vector, label) in samples:
            """
            calculate the output under the current weight
            """
            output = self.predict(input_vector)
            """
            renew the weight
            """
            self._update_weights(input_vector, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        """
        renew the weight
        :param input_vec:
        :param output:
        :param label:
        :param rate:
        :return:
        """
        delata = label - output
        self.weights = list(map(lambda x_w: x_w[1] + x_w[0] * delata * rate, zip(input_vec, self.weights)))
        self.bias += delata * rate



def f(x):
    """
    define the active function
    :param x:
    :return:
    """
    return 1 if x > 0 else 0


def get_training_dataset():
    """
    build the train set based on the "and" true value table
    :return:
    """
    """
    input vector list
    """
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    """
    the result list
    """
    labels = [1, 0, 0, 0]
    return input_vecs, labels

def train_and_perceptron():
    """

    :return:
    """
    """
    create perceptron and the number of input parameter is 2
    """
    p = Perceptron(2, f)
    """
    train and the rate is 0.1 ,train 10 times
    """
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    """
    :return the perceptron
    """
    return p


if __name__ == '__main__':
    """
    train the perceptron
    """
    and_perception = train_and_perceptron()
    print(and_perception)
    """
    test
    """
    print('1 and 1 = %d' % and_perception.predict([1, 1]))
    print('0 and 1 = %d' % and_perception.predict([0, 1]))
    print('1 and 0 = %d' % and_perception.predict([1, 0]))
    print('0 and 0 = %d' % and_perception.predict([0, 0]))
