from fastapi import FastAPI
from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data

app = FastAPI()

@app.get("/")
def run_pipeline():

    data = extract_data()
    clean = transform_data(data)
    load_data(clean)

    return {"status": "Pipeline executed successfully"}