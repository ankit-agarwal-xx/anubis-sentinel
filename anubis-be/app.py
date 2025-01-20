import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS 
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

st.title("ANUBIS-SENTINAL")

llm=ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)

def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        st.session_state.loader=PyPDFDirectoryLoader("./us_census")
        st.session_state.docs=st.session_state.loader.load()
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:20]) #[:20]
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)


prompt1=st.text_input("Enter Your Question From the Company Doduments")


if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB Is Ready")

import time 

if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    
    start=time.process_time()
    response=retrieval_chain.invoke({'input':prompt1})
    print("Response time :",time.process_time()-start)
    st.write(response['answer'])

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")

        


# import os
# import streamlit as st
# import json
# from langchain_groq import ChatGroq
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.chains import create_retrieval_chain
# from langchain_community.vectorstores import FAISS
# from langchain_community.document_loaders import PyPDFDirectoryLoader
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv
# import subprocess

# # Load environment variables
# load_dotenv()

# groq_api_key = os.getenv('GROQ_API_KEY')
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# # App title
# st.title("ANUBIS-SENTINAL")

# # Initialize the LLM
# llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# # Define the prompt
# prompt = ChatPromptTemplate.from_template("""
# You are a corporate intranet chat assistant. The user has asked the following:

# <QUERY>
# {{ question }}
# </QUERY>

# You have retrieved some documents to assist in your response:

# <DOCUMENTS>
# {{ context }}
# </DOCUMENTS>

# Think carefully and respond to the user concisely and accurately.
# """)

# # Vector embedding function
# def vector_embedding():
#     if "vectors" not in st.session_state:
#         # Load documents from the specified folder
#         st.session_state.loader = PyPDFDirectoryLoader("./us_census")
#         st.session_state.docs = st.session_state.loader.load()

#         # Split the documents into chunks
#         st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#         st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])  # Limit to the first 20 docs

#         # Create embeddings and vector store
#         st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

# # Function to run `retrieve_docs.py` and get the documents context
# def get_documents_context():
#     # Run the retrieve_docs.py script to get the document context
#     result = subprocess.run(['python', 'retrieve_docs.py'], stdout=subprocess.PIPE)
#     return json.loads(result.stdout.decode('utf-8'))

# # Input for user questions
# prompt1 = st.text_input("Enter Your Question From the Company Documents")

# # Button to generate embeddings
# if st.button("Documents Embedding"):
#     vector_embedding()
#     st.write("Vector Store DB Is Ready")

# # Process the query and retrieve results
# import time
# if prompt1:
#     # Ensure embeddings are ready
#     vector_embedding()

#     # Get the document context from `retrieve_docs.py`
#     document_context = get_documents_context()

#     # Create document chain and retriever
#     document_chain = create_stuff_documents_chain(llm, prompt)
#     retriever = st.session_state.vectors.as_retriever()
#     retrieval_chain = create_retrieval_chain(retriever, document_chain)

#     # Measure response time
#     start = time.process_time()
#     response = retrieval_chain.invoke({'question': prompt1, 'context': document_context})
#     st.write("Response time:", time.process_time() - start)
#     st.write(response['output'])

#     # Display document similarity search results
#     with st.expander("Document Similarity Search"):
#         for doc in response.get("context", []):
#             st.write(doc['text'])
#             st.write("--------------------------------")

