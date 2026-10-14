
from langchain_neo4j import LLMGraphTransformer

# Import reusable functions
from analysis import get_llm
from split_chunk import get_chunks


def extract_entities():

    # Step 1: Initialize LLM
    llm = get_llm()
    print("LLM initialized")

    # Step 2: Load document chunks
    chunks = get_chunks()
    print("Total chunks:", len(chunks))

    # Step 3: Initialize graph transformer
    transformer = LLMGraphTransformer(
        llm=llm,
        allowed_nodes=[
            "Person",
            "Organization",
            "Technology",
            "Team",
            "Service"
        ],
        allowed_relationships=[
            "WORKS_FOR",
            "DEVELOPS",
            "MANAGES",
            "USES",
            "PROVIDES",
            "INTEGRATES_WITH"
        ]
    )

    # Step 4: Extract graph documents
    graph_documents = (
        transformer.convert_to_graph_documents(chunks)
    )

    # Step 5: Print extracted entities
    for graph_doc in graph_documents:

        print("\n===== ENTITIES =====")

        for node in graph_doc.nodes:
            print(
                f"Entity: {node.id} | Type: {node.type}"
            )

        print("\n===== RELATIONSHIPS =====")

        for rel in graph_doc.relationships:
            print(
                f"{rel.source.id} "
                f"--[{rel.type}]--> "
                f"{rel.target.id}"
            )

    return graph_documents


if __name__ == "__main__":
    extract_entities()
