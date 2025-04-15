import sys
import os
import pandas as pd
from src.exception_handler import handle_exception
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise handle_exception(e)



class CustomData:
    def __init__(  self,
        age: int,
        gender: str,
        sleep_duration: int,
        stress_level: int,
        diet_type: str,
        daily_screen_time: int,
        exercise_frequency: str,
        caffeine_intake: int,
        reaction_time: int,
        memory_test_score: int,
        # cognitive_score: int,
        # ai_predicted_score: int,
        ):

        self.age = age
        self.gender = gender
        self.sleep_duration = sleep_duration
        self.stress_level = stress_level
        self.diet_type = diet_type
        self.daily_screen_time = daily_screen_time
        self.exercise_frequency = exercise_frequency
        self.caffeine_intake = caffeine_intake
        self.reaction_time = reaction_time
        self.memory_test_score = memory_test_score
        # self.cognitive_score = cognitive_score
        # self.ai_predicted_score = ai_predicted_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age": [self.age],
                "Gender": [self.gender],
                "Sleep_Duration": [self.sleep_duration],
                "Stress_Level": [self.stress_level],
                "Diet_Type": [self.diet_type],
                "Daily_Screen_Time": [self.daily_screen_time],
                "Exercise_Frequency": [self.exercise_frequency],
                "Caffeine_Intake": [self.caffeine_intake],
                "Reaction_Time": [self.reaction_time],
                "Memory_Test_Score": [self.memory_test_score],
                # "Cognitive_Score": [self.cognitive_score],
                # "AI_Predicted_Score": [self.ai_predicted_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise handle_exception(e)



# if __name__=="__main__":
#     test_dict = {
#                 "Age": [20],
#                 "Gender": ['Male'],
#                 "Sleep_Duration": [2],
#                 "Stress_Level": [2],
#                 "Diet_Type": ['Vegetarian'],
#                 "Daily_Screen_Time": [2],
#                 "Exercise_Frequency": ['Low'],
#                 "Caffeine_Intake": [2],
#                 "Reaction_Time": [2],
#                 "Memory_Test_Score": [2],
#                 # "Cognitive_Score": [self.cognitive_score],
#                 "AI_Predicted_Score": [2],
#             }
#     test=pd.DataFrame(test_dict)
#     print(PredictPipeline().predict(test))