import numpy as np
#from graphkernels import adjacencyListFromGraph,computeNodeApproxWeightWLMinHashFromGraph,computeNodeWeightedWLMinHashFromGraph,computeMDK_UUkernel,computeRLK_UUkernel,computeMEDK_UUkernel,computeLEDK_UUkernel,create_nx_graph_from_netkit, computeNodeWLMinHashFromGraph
#from sklearn.cross_validation import train_test_split
#from numpy.linalg import eig, eigh
def create_nx_graph_from_A(path_to_node_labels="graph_datasets/imdb_prodco/imdb_prodco.csv",
                                path_to_A="graph_datasets/imdb_prodco/imdb_prodco_300.rn"):
    import networkx as nx
    A=np.loadtxt(path_to_A)[:100,:100]
    nl=np.loadtxt(path_to_node_labels)[:100]
    print A
    G = nx.from_numpy_matrix(A)
    print G.node
    dl={}
    for i in xrange(len(G.node)):
        print(G.node[i],nl[i])
        dl[i]=nl[i]
    nx.set_node_attributes(G, 'label',dl)
    print G.node
    G.graph['node_order'] = range(len(G.node))
    print "Graph created"
    return G




def create_nx_graph_from_netkit(path_to_csv="graph_datasets/imdb_prodco/imdb_prodco.csv",
                                path_to_edges="graph_datasets/imdb_prodco/imdb_prodco_300.rn"):
    import networkx as nx

    G = nx.Graph()
    labels = {}
    labels_list = []
    node_order = []
    for line in open(path_to_csv, "r"):
        a = [x.strip() for x in line.split(',')]
        G.add_node(a[0],label=a[0])
        labels[a[0]] = a[1]
        node_order.append(a[0])
        labels_list.append(a[1])
    for line in open(path_to_edges, "r"):
        a = [x.strip() for x in line.split(',')]
        G.add_edge(a[0], a[1], weight=a[2])
    # normalize labels
    i = 0
    labels_to_ids = {}
    print "Number of classes:", len(np.unique(labels_list))
    for l in np.unique(labels_list):
        labels_to_ids[l] = i
        i = i + 1
    labels_ids = []
    for j in labels_list:
        labels_ids.append(labels_to_ids[j])
    # print labels_ids

    G.graph['node_order'] = node_order
    G.graph['target'] = labels_ids
    print "Graph created"
    return G

def load_dataset(dataset):
    if dataset == "HPRD":
        path_to_node_labels = "graph_datasets/HPRD/label.txt"
        path_to_A = "graph_datasets/HPRD/HPRD.txt.bz2"
        G=create_nx_graph_from_A(path_to_node_labels,path_to_A)
        return G, G.graph['node_order']
    elif dataset == "BioGPS":
        path_to_node_labels = "graph_datasets/BioGPS/label.txt"
        path_to_A = "graph_datasets/BioGPS/BioGPS.txt.bz2"
        G=create_nx_graph_from_A(path_to_node_labels,path_to_A)
        return G, G.graph['node_order']
    elif dataset == "Pathways":
        path_to_node_labels = "graph_datasets/Pathways/label.txt"
        path_to_A = "graph_datasets/Pathways/Pathways.txt.bz2"
        G=create_nx_graph_from_A(path_to_node_labels,path_to_A)
        return G, G.graph['node_order']
    elif dataset == "IMDB":
          path_to_node_labels="graph_datasets/imdb/imdb_prodco/imdb_prodco.csv"
          path_to_edges="graph_datasets/imdb/imdb_prodco/imdb_prodco.rn"
    elif dataset == "IMDB_ALL":
          path_to_node_labels="graph_datasets/imdb/imdb_all/imdb_all.csv"
          path_to_edges="graph_datasets/imdb/imdb_all/imdb_all.rn"
    elif dataset == "IMDB_SMALL":
          path_to_node_labels="graph_datasets/imdb/imdb_prodco/imdb_prodco.csv"
          path_to_edges="graph_datasets/imdb/imdb_prodco/imdb_prodco_300.rn"
    elif dataset == "INDUSTRY_YH":
          path_to_node_labels="graph_datasets/industry/industry-yh/industry-yh.csv"
          path_to_edges="graph_datasets/industry/industry-yh/industry-yh.rn"
    elif dataset == "INDUSTRY_PR":
          path_to_node_labels="graph_datasets/industry/industry-pr/industry-pr.csv"
          path_to_edges="graph_datasets/industry/industry-pr/industry-pr.rn"
    elif dataset == "WEBKB_CORNELL":
          path_to_node_labels="graph_datasets/webkb/webkb_cornell_cocite/WebKB-cornell-cocite.csv"
          path_to_edges="graph_datasets/webkb/webkb_cornell_cocite/WebKB-cornell-cocite.rn"
    elif dataset == "WEBKB_TEXAS":
          path_to_node_labels="graph_datasets/webkb/webkb_texas_cocite/WebKB-texas-cocite.csv"
          path_to_edges="graph_datasets/webkb/webkb_texas_cocite/WebKB-texas-cocite.rn"
    elif dataset == "WEBKB_WASHINGTON":
          path_to_node_labels="graph_datasets/webkb/webkb_washington_cocite/WebKB-washington-cocite.csv"
          path_to_edges="graph_datasets/webkb/webkb_washington_cocite/WebKB-washington-cocite.rn"
    elif dataset == "WEBKB_WISCONSIN":
          path_to_node_labels="graph_datasets/webkb/webkb_wisconsin_cocite/WebKB-wisconsin-cocite.csv"
          path_to_edges="graph_datasets/webkb/webkb_wisconsin_cocite/WebKB-wisconsin-cocite.rn"
    elif dataset == "CORA":
          path_to_node_labels="graph_datasets/cora/cora_cite/cora_cite.csv"
          path_to_edges="graph_datasets/cora/cora_cite/cora_cite.rn"

    G=create_nx_graph_from_netkit(path_to_node_labels,path_to_edges)
    #returns the graph, the labels associated to each node and the node ordering
    return G, G.graph['target'], G.graph['node_order']