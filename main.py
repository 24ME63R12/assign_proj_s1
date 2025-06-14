from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

# Read the Excel file once when the app starts
try:
    df = pd.read_excel("C:/Users/91799/Desktop/vs/capbudg.xlsx")

    tables = {
        "INITIAL INVESTMENT": df.iloc[2:9, 0:3].dropna(how="all", axis=1),
        "CASHFLOW DETAILS": df.iloc[2:6, 4:7].dropna(how="all", axis=1),
        "DISCOUNT RATE": df.iloc[2:11, 8:11].dropna(how="all", axis=1),
        "WORKING CAPITAL": df.iloc[11:14, 0:3].dropna(how="all", axis=1),
        "GROWTH RATES": df.iloc[16:19, 0:12].dropna(how="all", axis=1),
        "INITIAL INVESTMENT2": df.iloc[21:30, 0:2].dropna(how="all", axis=1),
        "SALVAGE VALUE": df.iloc[32:34, 0:11].dropna(how="all", axis=1),
        "OPERATING CASHFLOWS": df.iloc[36:49, 0:11].dropna(how="all", axis=1),
        "Investment Measures": df.iloc[52:55, 1:3].dropna(how="all", axis=1),
        "BOOK VALUE & DEPRECIATION": df.iloc[58:61, 0:11].dropna(how="all", axis=1),
    }

except Exception as e:
    print(f"Error loading Excel file: {e}")
    tables = {}


#name=[key for key in tables]
# print(name)
#rows=[key for key in tables["CASHFLOW DETAILS"].iloc[:,0]]
#print(rows)  

@app.get("/")
def root():
    return "Hi"

@app.get("/list_tables")
def list_tables():
    return {"tables": list(tables.keys())}

@app.get("/get_table_details")
def get_table_details(table_name: str):
    rows=[key for key in tables[table_name].iloc[:,0]]
    return {"table_name":table_name,"row_names":rows}

@app.get("/row_sum")
def row_sum(table_nam: str, row_nam: str):
    return {"table_name":table_nam,"row_name":row_nam}
