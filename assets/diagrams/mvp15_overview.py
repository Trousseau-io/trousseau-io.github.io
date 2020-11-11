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

with Diagram("Trousseau MVP1.5 - Overview", show=False, direction="LR", graph_attr=graph_attr):
    cli = Client("clectl")
    lb = Server("loadbalancer")

    with Cluster("HA key-value store"):
        server = Server("trousseaud")
        server - [ Server("KV1"),
                   Server("KV2"),
                   Server("KV3")]

    cli >> lb >> server
    cli << lb << server
    