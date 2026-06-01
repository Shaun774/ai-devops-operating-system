from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title : str
    completed : bool = False
    
fakedb = {
    1:{"name":"shaun","price":99},
    2:{"name":"Felix","price":100},
}
    

@app.get("/tasks/{taskid}")
def get_task(taskid:int):
    if taskid not in fakedb:
        print("item not found")
    else :
        return fakedb[taskid]

@app.delete

@app.post("/tasks")
def add_tasks(task:Task):
    return {"message":"Task  created sucessfully","data":task}
        

