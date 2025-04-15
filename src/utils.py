
import os
import numpy as np 
import requests
import pandas as pd
from src.exception_handler import handle_exception
from src.logger import logging
import dill
import pickle
import kagglehub
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV




def fetch_kaggle_as_dataframe(kaggle_url: str, file_name: str) -> pd.DataFrame:
    """
    Fetch Kaggle csv data and convert it into a pandas DataFrame.
    """
    try:
        path = kagglehub.dataset_download(kaggle_url)
        csv_path = os.path.join(path, file_name)
        df = pd.read_csv(csv_path)

        return df

    except Exception as e:
        raise handle_exception(e)
    

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise handle_exception(e)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            # train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise handle_exception(e)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise handle_exception(e)

def binary_encoder(df, heart_attack_date, target_column_name):
    try:
        df[target_column_name] = df[heart_attack_date].apply(lambda x: 1 if x else 0)
        return df
    except Exception as e:
        raise handle_exception(e)
    

# def date_feature_extractor(df, date_column):
#     try:
#         df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
#         df[f'{date_column}_year'] = df[date_column].dt.year
#         df[f'{date_column}_month'] = df[date_column].dt.month
#         df[f'{date_column}_day'] = df[date_column].dt.day
#         df[f'{date_column}_day_of_week'] = df[date_column].dt.dayofweek  # Monday=0, Sunday=6
#         df[f'{date_column}_quarter'] = df[date_column].dt.quarter  # 1, 2, 3, or 4
#         df[f'{date_column}_is_weekend'] = (df[date_column].dt.weekday >= 5).astype(int)  # 1 for weekend, 0 for weekdays
#         df.drop(columns=[date_column], inplace=True)
#         return df
#     except Exception as e:
#         raise handle_exception(e)
