from diagrams import Cluster, Diagram
# from diagrams.k8s.infra import ETCD
# from diagrams.k8s.rbac import User
from diagrams.k8s.podconfig import Secret
# from diagrams.k8s.network import Service
from diagrams.onprem.network import Etcd 
from diagrams.onprem.compute import Server 
from diagrams.onprem.client import Client, Users
from diagrams.generic.blank import Blank

graph_attr = { 
	 "splines": "curved",
}

with Diagram("Trousseau MVP1 - Simple Credentials", show=False, direction="LR", graph_attr=graph_attr):
    user = Users("user")
    cli = Client("client")
    secret1 = Secret("secret")
    secret2 = Secret("secret")
    server = Server("server")
    keyvalue = Server("key-value store")

    user >> secret1 >> cli 
    cli >> server >> secret2 >> keyvalue
    keyvalue << server << cli << user

