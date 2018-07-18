import sys
import random
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def graph_gen(name, nv, ne):
    df = pd.DataFrame(dtype='int',columns=['u','v'])
    #print("#M N Dir Wt")
    #print(nv, ne, 0, 0)
    for i in range(0, int(ne)):
        u = random.randrange(1, int(nv))
        v = random.randrange(1, int(nv))
        #print(u, v)
        df.loc[i] = [u, v]
        #print(i,": adding edge",u,v)
    return df


print("#Debug len is ",len(sys.argv))
## todo later: edge weights 
## dodo later: directed graphs

if len(sys.argv) < 3:
    g_name = input("Enter graph name <Enter for none>: ")
    g_num_v = input("Enter |V| ")
    g_num_e = input("Enter |E| ")
    print("#Graph", g_name, "has ", g_num_v, "vertices,", g_num_e, "edges")
else:
    [g_name, g_num_v, g_num_e] = sys.argv[1:4]
    print("#Graph", g_name, "has ", g_num_v, "vertices,", g_num_e, "edges")

df = graph_gen(g_name, g_num_v, g_num_e)
print(df)

# Plot it
G=nx.from_pandas_edgelist(df, 'u', 'v')
nx.draw(G, with_labels=True)
plt.show()

#constructive generator for classic graphs
lollipop = nx.lollipop_graph(10, 20)
nx.draw(lollipop, with_labels=True)
plt.show()

K_5 = nx.complete_graph(5)
nx.draw(K_5, with_labels=True)
plt.show()

K_3_5 = nx.complete_bipartite_graph(3, 5)
nx.draw(K_3_5, with_labels=True)
plt.show()

barbell = nx.barbell_graph(10, 10)
nx.draw(barbell, with_labels=True)
plt.show()

#stochastic graph generators
er = nx.erdos_renyi_graph(100, 0.15)
nx.draw(er, with_labels=True)
plt.show()

ws = nx.watts_strogatz_graph(30, 3, 0.1)
nx.draw(ws, with_labels=True)
plt.show()

ba = nx.barabasi_albert_graph(100, 5)
nx.draw(ba, with_labels=True)
plt.show()

red = nx.random_lobster(100, 0.9, 0.9)
nx.draw(red, with_labels=True)
plt.show()

