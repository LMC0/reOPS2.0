from fastapi import FastAPI, Query
from pydantic import BaseModel 
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORSミドルウェアを追加し、許可するオリジンを設定します
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンを許可する場合は"*"を使用します。必要に応じて適切なオリジンを設定します。
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # 許可するHTTPメソッドを指定します
    allow_headers=["*"],  # すべてのヘッダーを許可する場合は"*"を使用します。必要に応じて適切なヘッダーを設定します。
)

class DataType(BaseModel):
    key: str
    name: str
    status: int
    department: str

employee_data: List[DataType] = [
    {
        "key": "1",
        "name": "John Brown",
        "status": 1,
        "department": "New York No. 1 Lake Park",
    },
    {
        "key": "2",
        "name": "Jim Green",
        "status": 3,
        "department": "London No. 1 Lake Park",
    },
    {
        "key": "3",
        "name": "Joe Black",
        "status": 2,
        "department": "Sydney No. 1 Lake Park",
    },
    {
        "key": "4",
        "name": "Disabled User",
        "status": 2,
        "department": "Sydney No. 1 Lake Park",
    },
        {
        "key": "4",
        "name": "Disabled User",
        "status": 2,
        "department": "Sydney No. 1 Lake Park",
    },
        {
        "key": "4",
        "name": "Disabled User",
        "status": 2,
        "department": "Sydney No. 1 Lake Park",
    },

]

@app.get("/employee")
def employee():
    return employee_data

@app.get("/employee/detail")
def employee_one(key: str = Query(...)):
    for employee in employee_data:
        if employee["key"] == key:
            return employee
    return {"message": "Employee not found"}