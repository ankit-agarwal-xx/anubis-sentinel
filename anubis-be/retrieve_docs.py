# import argparse
# from langchain_community.document_loaders import PyPDFDirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.schema import Document

# def retrieve_documents(pdf_directory: str):
#     """
#     Loads PDF files from a specified directory, splits them into chunks, and returns a list of Document objects.
#     """
#     print(f"Loading PDFs from {pdf_directory}...")  # Debug log

#     # Load PDF documents from the specified directory
#     pdf_loader = PyPDFDirectoryLoader(pdf_directory)
#     documents = pdf_loader.load()

#     # Check if documents were loaded
#     if not documents:
#         print("No documents found.")  # Debug log
#     else:
#         print(f"Loaded {len(documents)} documents.")  # Debug log

#     # Split documents into manageable chunks
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
#     split_documents = text_splitter.split_documents(documents)

#     # Check if documents were split
#     if not split_documents:
#         print("No documents split.")  # Debug log
#     else:
#         print(f"Split into {len(split_documents)} chunks.")  # Debug log

#     return split_documents

# def get_var(*args):
#     """
#     A sample function to handle variable arguments.
#     """
#     print(f"Arguments received: {args}")

#     if len(args) == 1:
#         return f"Processed single argument: {args[0]}"
#     elif len(args) > 1:
#         return f"Processed multiple arguments: {', '.join(map(str, args))}"
#     else:
#         return "No arguments provided"

# if __name__ == "__main__":
#     # Testing the get_var function
#     result = get_var("context", "question", "additional_argument")
#     print(result)

#     #location
#     pdf_directory = "C:/Personal Projects/anubis/us_census"

#     # Parse command-line arguments
#     parser = argparse.ArgumentParser(description="Retrieve and split documents from PDF files.")
#     parser.add_argument("pdf_directory", type=str, help="Path to the directory containing PDF files.")
#     args = parser.parse_args()

#     # Process the PDFs and retrieve split documents
#     try:
#         docs = retrieve_documents(args.pdf_directory)
#         if docs:
#             for doc in docs:
#                 print(f"Document Metadata: {doc.metadata}")
#                 print(f"Document Text: {doc.page_content[:500]}...\n")  # Print the first 500 characters
#         else:
#             print("No documents to display.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

import argparse
import json
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def retrieve_documents(pdf_directory: str):
    """
    Loads PDF files from a specified directory, splits them into chunks, and returns a list of Document objects.
    """
    # Load PDF documents from the specified directory
    pdf_loader = PyPDFDirectoryLoader(pdf_directory)
    documents = pdf_loader.load()

    if not documents:
        print("No documents found.")  # Debug log
        return []

    # Split documents into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    split_documents = text_splitter.split_documents(documents)

    if not split_documents:
        print("No documents split.")  # Debug log
        return []

    # Prepare the output as a list of dictionaries
    output = [{"metadata": doc.metadata, "text": doc.page_content} for doc in split_documents]

    # Output JSON data
    return json.dumps(output)

def main(pdf_directory):
    """
    The main entry point of the script.
    This function will be executed when `retrieve_docs.py` is run from `promptfoo`.
    """
    try:
        # Retrieve documents and print as JSON
        result = retrieve_documents(pdf_directory)
        print(result)  # Output the result so promptfoo can capture it
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_directory = "C:/Personal Projects/anubis/us_census"
    main(pdf_directory)
