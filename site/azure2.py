#https://diagrams.mingrammer.com/
from diagrams import Cluster, Diagram, Edge, Dict, Digraph
from diagrams.azure.devops import Pipelines, Repos
from diagrams.onprem.iac import Terraform
from diagrams.generic.blank import Blank
from diagrams.aws.database import RDSPostgresqlInstance

with Diagram(name="Fluxo Arquetype - Terraform",  show=False, filename="../blueprint"):
    
    with Cluster(""):

        with Cluster("Provisioner"):
            arquetype = Terraform("Arquetype")
            module = Terraform("Module")
            arquetype >> module 

        with Cluster("Azure Devops"):
            
            pipeline = Pipelines("Azure Pipeline")
            repo = Repos("Azure Repo")
            pipeline - Edge(color="brown", style="dashed") - repo
            repo >> arquetype
    
    RDS1 = RDSPostgresqlInstance("RDS PostgreSQL")
    RDS2 = RDSPostgresqlInstance("RDS PostgreSQL")
    pipeline >> Edge(color="darkblue" ) >> RDS1
    pipeline >> Edge(color="darkblue" ) >> RDS2