from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data

def run_pipeline():
    data = extract_data()
    clean = transform_data(data)
    load_data(clean)

if __name__ == "__main__":
    run_pipeline()