from pymnet import *
import matplotlib.pyplot as plt
%matplotlib inline

G = MultilayerNetwork(aspects=1)

# Layer-A represent CAB transport network
G.add_layer('A')
G.add_node(1,layer='A')
G.add_node(2,layer='A')
G[1,2,'A','A'] = 1

# Layer-B represent AIR transport network
G.add_layer('B')
G.add_node(2,layer='B')
G.add_node(3,layer='B')
G[2,'A'][2,'B'] = 1
G[2,'B'][3,'B'] = 1


# Layer-C represent RAILWAY transport network
G.add_layer('C')
G.add_node(3,layer='C')
G.add_node(4,layer='C')
G[3,'B'][3,'C'] = 1
G[3,'C'][4,'C'] = 1


# Layer-D represent BUS transport network
G.add_layer('D')
G.add_node(4,layer='D')
G.add_node(5,layer='D')
G[4,'C'][4,'D'] = 1
G[4,'D'][5,'D'] = 1


# Layer-E represent WATER transport network
G.add_layer('E')
G.add_node(5,layer='E')
G.add_node(6,layer='E')
G[5,'D'][5,'E'] = 1
G[5,'E'][6,'E'] = 1


# Plot the multi-layer network
fig = draw(G,layerColorDict={'A':"y", 'B':"m", 'C': "c", 'D': "g", 'E':"r"},defaultEdgeColor="black", layout="spring", layergap=0.7, defaultLayerLabelLoc= (0,0), figsize=(10,10))