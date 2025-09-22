from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(

            age=float(request.form.get('age')),
            gender=request.form.get('gender'),
            sleep_duration=float(request.form.get('sleep_duration')),
            stress_level=float(request.form.get('stress_level')),
            diet_type=request.form.get('diet_type'),
            daily_screen_time=float(request.form.get('daily_screen_time')),
            exercise_frequency=request.form.get('exercise_frequency'),
            caffeine_intake=float(request.form.get('caffeine_intake')),
            reaction_time=float(request.form.get('reaction_time')),
            memory_test_score=float(request.form.get('memory_test_score')),

        )
        print(request.form.get('gender'))
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=np.round(results[0], 2))
    

if __name__=="__main__":
    app.run(host="0.0.0.0", port =8082, debug=True)        

