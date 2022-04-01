from generators import *

"""
g1 = ErdosRenyi(50, 50)
nx.draw(g1.get_graph())
plt.show()
"""

"""
g2 = WattsStrogatz(10, 4, 0.4)
nx.draw_circular(g2.get_graph(), with_labels=True)
plt.show()
"""

g3 = ConfigurationModel(10, np.random.poisson, 5)
nx.draw(g3.get_graph())
plt.show()
