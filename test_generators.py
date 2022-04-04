from cmath import exp
from generators import *

import sys
print(sys.version)
import networkx as nx
print(nx.__version__)

from network_utils import *


"""g1 = ErdosRenyi(20, 5)
nx.draw(g1, alpha=.5, node_size=20)
plt.show()"""

g1 = ErdosRenyi(1e3, 5)
p = 2 * 5 / (1e3 * (1e3 - 1))
plot_distrib_lin(g1, fit_binom_p=p, expct_lo=1, expct_hi=10)
plt.show()


"""

g2 = WattsStrogatz(10, 4, 0.4)
nx.draw_circular(g2, with_labels=True)
plt.show()

"""
"""
g3 = ConfigurationModel(10, np.random.poisson, 5)
#g3 = ConfigurationModel(10, np.random.power, 5)

print("Estimated power:", get_mle_poisson(g3.get_deg_list()), "Real power:", 3)

nx.draw(g3)
plt.show()

"""