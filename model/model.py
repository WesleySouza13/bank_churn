from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_selection import SelectFromModel
import pandas as pd 
import numpy as np 

df = pd.read_csv('C:\\Users\\souza\\Downloads\\churnML\\data\\Bank Customer Churn Prediction.csv')