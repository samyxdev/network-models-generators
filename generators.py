from abc import ABC, abstractmethod

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random as rd

class ModelGenerator(ABC):
    G = nx.Graph()

    N = 0

    """
    Network initialization
    Paramater checks
    """
    def __init__(self, N):
        self.G.add_nodes_from(range(N))

        self.N = int(N)

    def get_graph(self):
        return self.G

class ErdosRenyi(ModelGenerator):
    K = 0

    def __init__(self, N, K):
        assert 0 <= K <= N*(N-1)/2

        super().__init__(N)

        self.K = int(K)

        for i in range(self.K):
            valid = False
            n1, n2 = None, None
            while not valid:
                n1, n2 = np.random.choice(self.G.nodes()), np.random.choice(self.G.nodes())

                if n2 != n1 and not self.G.has_edge(n1, n2):
                    valid = True

            self.G.add_edge(n1, n2)


class WattsStrogatz(ModelGenerator):
    k = 0
    p = 0

    def __init__(self, N, k, p):
        assert 0 <= k < N and k%2 == 0

        super().__init__(N)

        self.k = int(k)
        self.p = p

        # Initial generation of the regular ring lttice
        print(nx.number_of_nodes(self.G))
        for i in range(self.N):
            for j in range(i + 1, (i + self.k//2 + 1)):
                #print("C", i, j%self.N)
                if(not self.G.has_edge(i, j%self.N)):
                    self.G.add_edge(i, j%self.N)

        # Rewirings
        for i in range(self.N):
            for nei in range(i + 1, (i + self.k//2 + 1)):
                if np.random.choice([False, True], p=[1 - self.p, self.p]):
                    #print("Rewriting ", i, nei%self.N)
                    # If rewiring needed, first remove the rewired edge
                    self.G.remove_edge(i, nei%self.N)

                    # Then adds an edge with a random node which we are not neighbors with (yet)
                    #print(list(nx.non_neighbors(self.G, i)))
                    new_nei = np.random.choice(list(nx.non_neighbors(self.G, i)))
                    #print("New nei:", new_nei)
                    self.G.add_edge(i, new_nei)

"""
g1 = ErdosRenyi(50, 50)
nx.draw(g1.get_graph())
plt.show()
"""

g2 = WattsStrogatz(10, 4, 0.4)
nx.draw_circular(g2.get_graph(), with_labels=True)
plt.show()


