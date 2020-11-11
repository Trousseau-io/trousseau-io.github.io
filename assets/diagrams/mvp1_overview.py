from diagrams import Cluster, Diagram
# from diagrams.k8s.infra import ETCD
# from diagrams.k8s.rbac import User
# from diagrams.k8s.podconfig import Secret
# from diagrams.k8s.network import Service
from diagrams.onprem.network import Etcd 
from diagrams.onprem.compute import Server 
from diagrams.onprem.client import Client, Users
from diagrams.generic.blank import Blank

graph_attr = { 
	 "splines": "curved"
}

with Diagram("Trousseau MVP1 - Overview", show=False, direction="LR", graph_attr=graph_attr):
    cli = Client("clectl")
    server = Server("trousseaud")
    keyvalue = Server("key-value store")

    cli >> server >> keyvalue 
    keyvalue << server << cli
