from graphviz import Digraph


class ClassToDot:
    def __init__(self):
        self.my_class = dict

    def __set_class(self, new_class):
        self.my_class = new_class

    def create_dot(self, new_class):
        self.__set_class(new_class)

    def test(self):
        dot = Digraph
        dot.node('A', 'First')

