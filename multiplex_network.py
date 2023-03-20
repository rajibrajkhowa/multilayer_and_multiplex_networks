from pymnet import *
import matplotlib.pyplot as plt
%matplotlib inline

# Define the network
G = MultiplexNetwork(couplings='none')
G.add_node("Andy")
G.add_node("Carol")
G.add_node("Tyler")
G.add_layer("Family")
G.add_layer("Work")

# Define connections
G["Andy","Carol","Family","Family"] = 1
G["Andy","Tyler","Work","Work"] = 1

# Plot the network 
fig = draw(G,layerColorDict={"Family":"y", "Work":"c"},defaultEdgeColor="red", layout="spring", layergap=2, defaultLayerLabelLoc= (0,1), figsize=(10,10))