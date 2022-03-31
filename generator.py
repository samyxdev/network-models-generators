from abc import ABC, abstractmethod

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class ModelGenerator(ABC):
    G = nx.Graph()

    """
    Network initialization
    Paramater checks
    """
    def __init__(self, N):
        self.G.add_nodes_from(range(N))

    def get_graph(self):
        return self.G

class ErdosRenyi(ModelGenerator):
    N = 0
    K = 0

    def __init__(self, N, K):
        assert 0 <= K <= N*(N-1)/2

        super().__init__(int(N))

        self.N = int(N)
        self.K = int(K)

        for i in range(self.K):
            valid = False
            n1, n2 = None, None
            while not valid:
                n1, n2 = np.random.choice(self.G.nodes()), np.random.choice(self.G.nodes())

                if n2 != n1 and not self.G.has_edge(n1, n2):
                    valid = True

            self.G.add_edge(n1, n2)

g1 = ErdosRenyi(50, 50)
nx.draw(g1.get_graph())
plt.show()



