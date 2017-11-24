__author__ = "Riccardo Tesselli"
__date__ = "17/gen/2015"
__credits__ = ["Riccardo Tesselli"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer = "Riccardo Tesselli"
__email__ = "riccardo.tesselli@gmail.com"
__status__ = "Production"

import nose
import nose.tools as nt
import networkx as nx
from ..GraphTools import generateDAG

class TestGraphTools(nose.case.unittest.TestCase):
    def testGenerateDAGisDAG(self):
        G=nx.random_regular_graph(10,60)
        for u in G.nodes():
            G.node[u]['label']='a'
        (DAG,maxlevel) = generateDAG(G, 0, 4)
        nt.assert_true(nx.is_directed_acyclic_graph(DAG), "Not DAG")

    def testGenerateDAGDiamondGraph(self):
        G=nx.diamond_graph()
        for u in G.nodes():
            G.node[u]['label']='a'
        (DAG,maxlevel)=generateDAG(G, 0, 4)
        DAG_test=nx.DiGraph()
        DAG_test.add_node(0,label='a')
        DAG_test.add_node(1,label='a')
        DAG_test.add_node(2,label='a')
        DAG_test.add_node(3,label='a')
        DAG_test.add_edge(0, 1)
        DAG_test.add_edge(0, 2)
        DAG_test.add_edge(1, 3)
        DAG_test.add_edge(2, 3)
        nt.assert_true(nx.is_isomorphic(DAG,DAG_test), "Not correct")

