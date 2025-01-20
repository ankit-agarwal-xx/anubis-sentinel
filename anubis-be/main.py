# from fastapi import FastAPI, HTTPException
# import subprocess
# import os
# import logging

# # Initialize FastAPI app
# app = FastAPI()

# # Set up logging for better visibility into errors
# logging.basicConfig(level=logging.INFO)

# @app.post("/fetch-metrics")
# async def fetch_metrics():
#     try:
#         # Log that the endpoint was hit
#         logging.info("Fetching metrics...")

#         # Specify the absolute paths to the Python scripts (ensure they are correct)
#         script1 = "C:/Personal Projects/anubis/promptfoo_test.py"
#         script2 = "C:/Personal Projects/anubis/data_security_analysis.py"
#         promptfoo_eval_command = "C:/Personal Projects/anubis/promptfooconfig.yaml"  # Replace with the correct path to promptfoo

#         # Run the Python scripts
#         result1 = subprocess.run([r"C:\Python311\python.exe", script1], capture_output=True, text=True)
#         result2 = subprocess.run([r"C:\Python311\python.exe", script2], capture_output=True, text=True)

#         # Run the promptfoo eval command
#         result3 = subprocess.run(promptfoo_eval_command, capture_output=True, text=True, shell=True)

#         # Log the outputs or errors for debugging
#         if result1.returncode != 0:
#             logging.error(f"Error in script 1: {result1.stderr}")
#         if result2.returncode != 0:
#             logging.error(f"Error in script 2: {result2.stderr}")
#         if result3.returncode != 0:
#             logging.error(f"Error in promptfoo eval command: {result3.stderr}")

#         # Raise an exception if any script fails
#         if result1.returncode != 0 or result2.returncode != 0 or result3.returncode != 0:
#             raise HTTPException(status_code=500, detail="One or more scripts failed.")

#         # Combine the results
#         combined_result = {
#             "result1": result1.stdout,
#             "result2": result2.stdout,
#             "result3": result3.stdout,
#         }

#         # Log successful result
#         logging.info("Metrics fetched successfully.")
#         return combined_result

#     except Exception as e:
#         logging.error(f"An error occurred: {str(e)}")
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


import subprocess
import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.post("/fetch-metrics")
async def fetch_metrics():
    try:
        # Run promptfoo_test.py
        logging.info("Running promptfoo_test.py script")
        result1 = subprocess.run(['python', 'promptfoo_test.py'], capture_output=True, text=True, shell=True, encoding='utf-8')
        if result1.returncode != 0:
            logging.error(f"Error in promptfoo_test.py: {result1.stderr}")
            return JSONResponse(status_code=500, content={"message": "Error running promptfoo_test.py"})
        logging.info(f"promptfoo_test.py Output: {result1.stdout}")

        # Run data_security_analysis.py
        logging.info("Running data_security_analysis.py script")
        result2 = subprocess.run(['python', 'data_security_analysis.py'], capture_output=True, text=True, shell=True, encoding='utf-8')
        if result2.returncode != 0:
            logging.error(f"Error in data_security_analysis.py: {result2.stderr}")
            return JSONResponse(status_code=500, content={"message": "Error running data_security_analysis.py"})
        logging.info(f"data_security_analysis.py Output: {result2.stdout}")

        # Run promptfoo eval command
        promptfoo_eval_command = 'promptfoo eval -c "C:/Personal Projects/anubis/promptfooconfig.yaml"'
        logging.info(f"Running promptfoo eval command: {promptfoo_eval_command}")
        result3 = subprocess.run(promptfoo_eval_command, capture_output=True, text=True, shell=True, encoding='utf-8')

        if result3.returncode != 0:
            logging.error(f"Error in promptfoo eval: {result3.stderr}")
            return JSONResponse(status_code=500, content={"message": "Error running promptfoo eval"})
        
        logging.info(f"Promptfoo Eval Output: {result3.stdout}")
        return {"message": "Metrics fetched successfully", "data": {"promptfoo_test": result1.stdout, "data_security_analysis": result2.stdout, "promptfoo_eval": result3.stdout}}

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return JSONResponse(status_code=500, content={"message": f"An error occurred: {str(e)}"})


