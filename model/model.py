from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_selection import SelectFromModel
from 
import pandas as pd 
import numpy as np 

df = pd.read_csv('C:\\Users\\souza\\Downloads\\churnML\\data\\Bank Customer Churn Prediction.csv')

model = GradientBoostingClassifier(
                                    n_estimators=117, 
                                    min_samples_split=25,
                                    min_samples_leaf=23,
                                    max_depth=18,
                                    max_leaf_nodes=14,
                                    learning_rate=0.0810962798100498
                                            )
column_tranf = ColumnTransformer(('scaler', StandardScaler()),
                                ('one_hot', OneHotEncoder(handle_unknown='ignore')),
                                ''
                                
                                
                                )