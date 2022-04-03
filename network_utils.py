import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import poisson

# Plotting auxiliary function
def plot_distrib_log(graph, colour='#40a6d1', alpha=.8, fit_line=False, expct_lo=1, expct_hi=10, expct_const=1):

    plt.close()
    num_nodes = graph.number_of_nodes()

    # Calculate the maximum degree to know the range of x-axis
    max_degree = np.max([val for key,val in graph.degree()])

    # X-axis and y-axis values
    x = []
    y_tmp = []

    # Loop over all degrees until the maximum to compute the portion of nodes for that degree
    for i in range(max_degree + 1):
        x.append(i) # build x list
        y_tmp.append(0) # build y list

        for n in graph.nodes():
            if graph.degree(n) == i:
                y_tmp[i] += 1
        y = [i / num_nodes for i in y_tmp]

    plt.xscale('log')
    plt.yscale('log')
    plt.title('Degree distribution (log-log scale)')
    plt.ylabel('log(P(k))')
    plt.xlabel('log(k)')
    plt.plot(x, y, linewidth = 0, marker = 'o', markersize = 8, color = colour, alpha = alpha)

    if fit_line:
        # Add theoretical distribution line k^-3
        # Note that you need to parametrize it manually
        w = [a for a in range(expct_lo,expct_hi)]
        z = []
        for i in w:
            x = (i**-3) * expct_const # set line's length and fit intercept
            z.append(x)

        plt.plot(w, z, 'k-', color='#7f7f7f')

    plt.show()

def plot_distrib_lin(graph, colour='#40a6d1', alpha=.8, fit_poisson=False, fit_lambda=None, expct_lo=1, expct_hi=10, expct_const=1):
    plt.close()
    num_nodes = graph.number_of_nodes()

    # Calculate the maximum degree to know the range of x-axis
    max_degree = np.max([val for key,val in graph.degree()])

    # X-axis and y-axis values
    x = []
    y_tmp = []

    # Loop over all degrees until the maximum to compute the portion of nodes for that degree
    for i in range(max_degree + 1):
        x.append(i) # build x list
        y_tmp.append(0) # build y list

        for n in graph.nodes():
            if graph.degree(n) == i:
                y_tmp[i] += 1
        y = [i / num_nodes for i in y_tmp]

    plt.plot(x, y, linewidth = 1, marker = 'o', markersize = 8, color = colour, alpha = alpha)
    plt.title('Degree distribution (linear scale)')
    plt.ylabel('P(k)')
    plt.xlabel('k')

    if fit_poisson:
        # Add theoretical distribution poisson line
        w = [a for a in np.arange(expct_lo,expct_hi)]
        z = []

        #for i in w:
        #   x = ((lamb**i) * math.exp(-lamb)) / math.factorial(i) # poisson pmf
        #    z.append(x)

        #create an array with Poisson probability values
        z = poisson.pmf(w, mu=fit_lambda)
        plt.plot(w, z, 'k-', color='#7f7f7f')

    plt.legend(["Real degrees", f"Poisson model (lambda={fit_lambda})"])

    plt.show()