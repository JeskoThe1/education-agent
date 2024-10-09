from langchain_community.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import GraphCypherQAChain
from ..config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD, OPENAI_API_KEY

def setup_graph_database():
    graph = Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD
    )
    return graph

def create_graph_documents(documents):
    graph_llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)

    graph_transformer = LLMGraphTransformer(
        llm=graph_llm,
        allowed_nodes=[
            "Document",
            "Country",
            "EducationSystem",
            "EducationLevel",
            "Policy"
        ],
        node_properties=[
            "title",
            "content",
            "year",
            "isCompulsory",
            "ISCEDLevel"
        ],
        allowed_relationships=[
            "DESCRIBES",
            "HAS_SYSTEM",
            "INCLUDES_LEVEL",
            "IMPLEMENTS"
        ],
    )

    graph_documents = graph_transformer.convert_to_graph_documents(documents)
    return graph_documents

def add_graph_documents(graph, documents):
    graph_documents = create_graph_documents(documents)
    graph.add_graph_documents(graph_documents)
    print(f"Graph documents: {len(graph_documents)}")
    if graph_documents:
        print(f"Nodes from 1st graph doc:{graph_documents[0].nodes}")
        print(f"Relationships from 1st graph doc:{graph_documents[0].relationships}")

def create_graph_rag_chain(graph):
    cypher_prompt = PromptTemplate(
        template="""You are an expert at generating Cypher queries for Neo4j.
        Use the following schema to generate a Cypher query that answers the given question.
        Make the query flexible by using case-insensitive matching and partial string matching where appropriate.
        Focus on searching document contents and education system properties as they contain the most relevant information.
        
        If you need to use UNION, ensure that all subqueries in the UNION have the same return column names.
        Use aliases (AS) to standardize column names across all subqueries.
        
        Schema:
        {schema}
        
        Question: {question}
        
        Cypher Query:""",
        input_variables=["schema", "question"],
    )

    qa_prompt = PromptTemplate(
        template="""You are an assistant for question-answering tasks about education systems. 
        Use the following Cypher query results to answer the question. If you don't know the answer, just say that you don't know. 
        Use three sentences maximum and keep the answer concise. If specific information is not available, focus on the general education system characteristics.
        
        Question: {question} 
        Cypher Query: {query}
        Query Results: {context} 
        
        Answer:""",
        input_variables=["question", "query", "context"],
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)

    graph_rag_chain = GraphCypherQAChain.from_llm(
        cypher_llm=llm,
        qa_llm=llm,
        validate_cypher=True,
        graph=graph,
        verbose=True,
        return_intermediate_steps=True,
        return_direct=True,
        cypher_prompt=cypher_prompt,
        qa_prompt=qa_prompt,
        allow_dangerous_requests=True
    )

    return graph_rag_chain
