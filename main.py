from fastapi import FastAPI
from pydantic import BaseModel
import random 
import csv
from fastapi.responses import FileResponse


app = FastAPI()

class goal_p_info(BaseModel):
    name: str
    description: str
    start_d: str
    end_d: str
    deadline: str

goall = []

@app.post('/post')
def post_g(goal : goal_p_info):

    goal_dict = goal.dict()
    goal_dict["Goal_id"] = random.randint(10000 , 12345678934)
    
    goall.append(goal_dict)

    return {"Status" : "Successfully added" , "goal" : goal_dict} 

@app.get('/goals')
def getgoal():
    return goall

@app.delete('/del/{Goal_id}')
def del_goal(Goal_id : int):
    for i in goall:
        if i.get('Goal_id') == Goal_id:
            goall.remove(i)

            return {"Message" : "Deteled your goal" , "Goal_deteled" : Goal_id}
        

@app.put('/update/{Goal_id}/name')
def goal_name_put(Goal_id : int , name :str):
    for i in goall:
        if i.get("Goal_id") == Goal_id:
            i['name'] = name
            return {"Executed" : "Name Change" , "Updated_goal" : goall}

@app.put('/update/{Goal_id}/deadline')
def goal_deadline_put(Goal_id : int , deadline :str):
    for i in goall:
        if i.get("Goal_id") == Goal_id:
            i['deadline'] = deadline
            return {"Executed" : "Deadline Change" , "Updated_goal" : goall}
        

@app.put('/update/{Goal_id}/description')
def goal_descrip_put(Goal_id : int , description :str):
    for i in goall:
        if i.get("Goal_id") == Goal_id:
            i['description'] = description
            return {"Executed" : "Description Change" , "Updated_goal" : goall}


@app.put('/update/{Goal_id}/start_d')
def goal_start_put(Goal_id : int , start_d :str):
    for i in goall:
        if i.get("Goal_id") == Goal_id:
            i['start_d'] = start_d
            return {"Executed" : "Start Date Change" , "Updated_goal" : goall}

@app.put('/update/{Goal_id}/end_d')
def goal_end_put(Goal_id : int , end_d :str):
    for i in goall:
        if i.get("Goal_id") == Goal_id:
            i['end_d'] = end_d
            return {"Executed" : "End date Change" , "Updated_goal" : goall}
        



@app.get('/export')
def export_goals():
    headers = ["Goal_id", "name", "description", "start_d", "end_d", "deadline"]
    with open('Active_goals.csv' , 'w+') as f:
        w = csv.DictWriter(f , fieldnames=headers)
        w.writeheader()
        w.writerows(goall)


        return FileResponse(
            path="Active_goals.csv" ,
            filename="Active_goals.csv" ,
            media_type= 'text/csv'
        )
        