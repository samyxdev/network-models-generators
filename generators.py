from abc import ABC, abstractmethod

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random as rd

get_mle_power = lambda deg_list, max_pow : 1/(np.log(max_pow) - 1/len(deg_list)*sum(np.log(deg_list))) - 1
get_mle_poisson = lambda deg_list : 1/len(deg_list)*sum(deg_list)

def init_graph(N):
    G = nx.Graph()
    G.add_nodes_from(range(N))

    return G

def ErdosRenyi(N, K):
    N = int(N) # For exposant writtings : 1e3 is a float for python
    G = init_graph(N)

    assert 0 <= K <= N*(N-1)/2

    for i in range(K):
        valid = False
        n1, n2 = None, None
        while not valid:
            n1, n2 = np.random.randint(N), np.random.randint(N)

            if n2 != n1 and not G.has_edge(n1, n2):
                valid = True

        #print("Adding edge:", n1, n2)
        G.add_edge(n1, n2)

    return G


def WattsStrogatz(N, k, p):
    N = int(N) # For exposant writtings : 1e3 is a float for python
    G = init_graph(N)

    assert 0 <= k < N and k%2 == 0

    k = int(k)
    p = p

    # Initial generation of the regular ring lttice
    for i in range(N):
        for j in range(i + 1, (i + k//2 + 1)):
            #print("C", i, j%N)
            if(not G.has_edge(i, j%N)):
                G.add_edge(i, j%N)

    # Rewirings
    for i in range(N):
        for nei in range(i + 1, (i + k//2 + 1)):
            if np.random.choice([False, True], p=[1 - p, p]):
                #print("Rewriting ", i, nei%N)
                # If rewiring needed, first remove the rewired edge
                G.remove_edge(i, nei%N)

                # Then adds an edge with a random node which we are not neighbors with (yet)
                #print(list(nx.non_neighbors(G, i)))
                new_nei = np.random.choice(list(nx.non_neighbors(G, i)))
                #print("New nei:", new_nei)
                G.add_edge(i, new_nei)

    return G

"""
class ConfigurationModel(ModelGenerator):

    # N: Number of nodes
    # deg_dist: Function of the degree distribution. Must have arguments as (law_param, size)
    # law_param: Parameter of the degree distribution
    def __init__(self, N, deg_dist, law_param):
        super().__init__(N)

        assert callable(deg_dist)

        # Generate a valid list of degrees (total sum of degrees must be even)
        valid = False
        degs = []
        while not valid:
            degs = deg_dist(law_param, N)

            if sum(degs)%2 == 0:
                valid = True
            else:
                print("Generated invalid degree list...")

        #print(degs)

        # Generate slot list
        slots = []
        for i in range(N):
            slots += [i for _ in range(degs[i])]

        #print(slots)

        # Shuffle and add edges
        np.random.shuffle(slots)

        #print(slots)

        for i in range(0, len(slots), 2):
            self.G.add_edge(slots[i], slots[i+1])
"""