<img src="anubis-fe/src/assets/Anubis-Sen.svg" alt="Anubis Logo" width="70"  align="left" />
# Anubis Sentinel

Anubis Sentinel is a comprehensive red teaming solution designed to enhance security for Retrieval-Augmented Generation (RAG) systems. This project empowers enterprises to safeguard their AI implementations through robust testing, evaluation, and analysis of vulnerabilities, ensuring resilient and secure AI systems.

![Preview](anubis-fe/src/assets/preview.png)

---

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Back-end Setup](#back-end-setup)
  - [Front-end Setup](#front-end-setup)
- [Usage Guide](#usage-guide)
- [Tech Stack](#tech-stack)

---

## Introduction

Anubis Sentinel enables developers and organizations to:
- Analyze RAG systems for vulnerabilities such as prompt injection and hallucinations.
- Evaluate data security and generate detailed metrics and logs.
- Visualize and interact with system performance via a user-friendly interface.

---

## Project Structure

The project is organized as follows:
```
anubis/
├── anubis-be/    # Back-end folder (Python-based APIs and scripts)
└── anubis-fe/    # Front-end folder (React + TailwindCSS)
```

---

## Features
- Streamlit-based interface for document embedding and vector database initialization.
- Comprehensive red teaming tests using **Promptfoo** and custom scripts.
- Data security analysis with shareable metrics.
- REST APIs for secure communication and metrics fetching.
- Modular, extensible front-end powered by React and TailwindCSS.

---

## Setup Instructions

### Back-end Setup

1. Navigate to the `anubis-be` folder:
   ```bash
   cd anubis/anubis-be
   ```

2. Install all dependencies using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the Streamlit interface:
   ```bash
   streamlit run app.py
   ```

4. Initialize the vector database for document embedding.

5. Run the following custom scripts as needed:

   Prompt Injection and Hallucination Tests:
   ```bash
   python promptfoo_test.py
   ```

   Data Security Analysis:
   ```bash
   python data_security_analysis.py
   ```

   Promptfoo Metrics Evaluation:
   ```bash
   promptfoo eval -c ./promptfooconfig.yaml
   ```

   To view detailed logs:
   ```bash
   promptfoo view
   ```

6. Test the FastAPI endpoint:

   Start the API server:
   ```bash
   uvicorn main:app --reload
   ```

   Use a tool like Postman to send a POST request to:
   ```
   http://127.0.0.1:8000/fetch-metrics
   ```
   You'll receive the results in JSON format.

### Front-end Setup

1. Navigate to the anubis-fe folder:
   ```bash
   cd anubis/anubis-fe
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Usage Guide

### Streamlit Interface
- Use the interface to upload and vector embed documents.
- Run direct prompts via the prompt interface to analyze results.

### Testing Tools
- Promptfoo: Evaluate vulnerabilities and generate red teaming metrics.
- Custom Scripts: Perform specific analyses like hallucination and security checks.

### REST API
- Test the /fetch-metrics endpoint for real-time JSON results.

## Tech Stack
- Back-end: Python, Streamlit, FastAPI, Promptfoo
- Front-end: React, TailwindCSS
- Database: Vector embedding with FAISS

