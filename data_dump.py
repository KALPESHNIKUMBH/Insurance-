import pymongo # pip install pymongo
import pandas as pd
import json

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kalpnik8:knik@cluster0.azgxu7o.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)


DATA_FILE_PATH = (r"C:\Users\kalpe\Desktop\Projects\Insurance-\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)