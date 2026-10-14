
from graph_store import get_graph
from analysis import get_llm
from langchain_core.prompts import ChatPromptTemplate


def answer_from_graph(question):

    # Step 1: Connect to Neo4j
    graph = get_graph()
    print("Connected to Neo4j successfully!")

    # Step 2: Retrieve graph relationships
    facts = graph.query("""
        MATCH (a)-[r]->(b)
        WHERE a.id IS NOT NULL
          AND b.id IS NOT NULL
        RETURN
            a.id AS source,
            type(r) AS relationship,
            b.id AS target
        LIMIT 100
    """)

    print("\n===== RETRIEVED GRAPH FACTS =====")

    for fact in facts:
        print(
            f"{fact['source']} "
            f"--[{fact['relationship']}]--> "
            f"{fact['target']}"
        )

    # Step 3: Initialize LLM
    llm = get_llm()

    # Step 4: Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a Knowledge Graph assistant. "
            "Answer questions using only the graph facts provided. "
            "If the answer is not present, say "
            "'I don't know based on the available graph facts.'"
        ),
        (
            "human",
            "Question: {question}\n\n"
            "Graph facts:\n{facts}"
        )
    ])

    # Step 5: Create LangChain pipeline
    chain = prompt | llm

    # Step 6: Generate answer
    response = chain.invoke({
        "question": question,
        "facts": facts
    })

    return response.content


if __name__ == "__main__":

    question = input("Ask a question: ")

    answer = answer_from_graph(question)

    print("\n===== AI ANSWER =====")
    print(answer)
