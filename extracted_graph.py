
from graph_store import get_graph
from extract_entity import extract_entities


def store_knowledge_graph():

    # Step 1: Connect to Neo4j
    graph = get_graph()
    print("Connected to Neo4j")

    # Step 2: Extract nodes and relationships
    graph_documents = extract_entities()

    print("Graph documents:", len(graph_documents))

    # Step 3: Store graph documents in Neo4j
    graph.add_graph_documents(
        graph_documents,
        include_source=True
    )

    print("Knowledge Graph stored successfully!")

    # Step 4: Verify stored relationships
    results = graph.query("""
        MATCH (a)-[r]->(b)
        RETURN a.id AS source,
               type(r) AS relationship,
               b.id AS target
        LIMIT 20
    """)

    for record in results:
        print(record)


if __name__ == "__main__":
    store_knowledge_graph()
