

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
