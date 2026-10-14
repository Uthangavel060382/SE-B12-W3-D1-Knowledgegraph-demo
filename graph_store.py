
import os
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

load_dotenv()

def get_graph():
    graph = Neo4jGraph(
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
        database=os.getenv("NEO4J_DATABASE", "neo4j")
    )

    return graph


if __name__ == "__main__":
    graph = get_graph()
    print("Connected to Neo4j successfully!")
