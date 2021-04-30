from diagrams import Diagram, Cluster
from diagrams.azure.compute import VMWindows, VMLinux
from diagrams.azure.network import VirtualNetworks, LoadBalancers, Firewall, NetworkSecurityGroupsClassic
from diagrams.azure.database import SQLDatabases
from diagrams.azure.web import AppServices


with Diagram("Esquema 01 - Azure", show=False, filename="../blueprint2"):
    with Cluster ("Azure Cloud"):
      fw2 = Firewall("f2")
      lb2 = LoadBalancers("lb2")
      app1 = AppServices("Cloud Services")

    fw1 = Firewall("fw1")

    with Cluster("Rede Interna"):
            sql1 = SQLDatabases("SQL")
            lb1 = LoadBalancers("LB")   
            rede = VirtualNetworks("Vnet")
            vm1 = VMWindows("vm 1")
            vm1 - VMWindows("vm 2")
    app1 >> lb2 >> fw2 >> fw1 >> lb1 >> rede >> vm1
    sql1 >> rede
      
    