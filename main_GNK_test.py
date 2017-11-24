from Myutils import load_dataset
from load_graph_datasets import dispatch
from WLVectorizer import WLVectorizer
import sys, os
if __name__=='__main__':
    if len(sys.argv)<4:
        sys.exit("python main_netkit.py dataset iterations")
    dataset = sys.argv[1]
    iter= int(sys.argv[2])

    G,node_order=load_dataset(dataset)
    print("Node order (same order as target, same order of nodes in kernel computation)")

    print node_order
    print("Computing WL node kernel..")
    #r is the number of iterations
    WLvect= WLVectorizer(r=iter)
    #[G] is a list with just one graph inside
    features= WLvect.transform([G])
    # Returns: a list of length r (number of iterations) of lists of length n_graphs of matrices of size n_vertices x n_features
    #E.g. for r=3, iterations from 0 to 3 included
    for i in xrange(3+1):
        print("ieration",i)
        print features[i][0]
