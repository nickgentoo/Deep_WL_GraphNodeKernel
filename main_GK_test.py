from Myutils import load_dataset
from load_graph_datasets import dispatch
from WLVectorizer import WLVectorizer
import sys, os
if __name__=='__main__':
    if len(sys.argv)<4:
        sys.exit("python main_netkit.py dataset kernel beta")
    dataset = sys.argv[1]
    kernel = sys.argv[2]
    beta= sys.argv[3]

    G_list=dispatch(dataset)

    node_order=G_list.graphs[0].graph['node_order']
    print node_order
    y=G_list.target
    print y

    print node_order
    print("Computing WL node kernel..")
    WLvect= WLVectorizer(r=3)
    features= WLvect.transform(G_list.graphs)
    #print features[0]
    print features[1][0]