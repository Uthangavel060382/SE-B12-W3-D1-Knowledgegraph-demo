
# Import Neo4j connection function
from graph_store import get_graph


def query_knowledge_graph():

    # Step 1: Connect to Neo4j
    graph = get_graph()

    print("Connected to Neo4j successfully!")

    # Step 2: Execute Cypher query
    result = graph.query("""
        MATCH (a)-[r]->(b)
        RETURN
            a.id AS source,
            type(r) AS relationship,
            b.id AS target
        LIMIT 20
    """)

    # Step 3: Display results
    print("\n===== KNOWLEDGE GRAPH RESULTS =====")

    for record in result:
        print(
            f"{record['source']} "
            f"--[{record['relationship']}]--> "
            f"{record['target']}"
        )

    return result


if __name__ == "__main__":
    query_knowledge_graph()
