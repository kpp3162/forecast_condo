import pickle
from fastapi import FastAPI
from sklearn.naive_bayes import GaussianNB


with open('trained_model.plk','rb') as f:
    model = pickle.load(f)

app = FastAPI()
@app.get("/")
async def main():
    return 'Deploy Model'

@app.get("/predict")
async def create_item(developer_id,
                       district_id,
                       lat,
                       lon,
                       project_land_rai,
                       total_unit,
                       starting_price,created_at,
                       Unit,
                       Bedroom,
                       Bathroom,
                       project_status_0,
                       project_status_1,
                       project_status_2):

 instant= [[developer_id,district_id,lat,lon,project_land_rai,
                       total_unit,
                       starting_price,created_at,
                       Unit,
                       Bedroom,
                       Bathroom,
                       project_status_0,
                       project_status_1,
                       project_status_2]]
 result = model.predict(instant)[0]
 return {"Price2020":int(result)}

if __name__ == '__main__':
   import uvicorn
   uvicorn.run(app, host="0.0.0.0", port=5000, debug=True) 