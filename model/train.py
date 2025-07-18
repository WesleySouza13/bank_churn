from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.feature_selection import SelectFromModel
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import accuracy_score, recall_score, precision_score 
import pandas as pd 
import numpy as np 
import joblib
df = pd.read_csv('C:\\Users\\souza\\Downloads\\churnML\\data\\Bank Customer Churn Prediction.csv')
x = df.drop('customer_id', axis=1)
x = df.drop('churn', axis=1)
y = df['churn']

print(x)
cat_atribs = ['country', 'gender']
num_atribs = ['credit_score', 'age', 'tenure', 'balance', 'products_number',
    'credit_card', 'active_member', 'estimated_salary']

# split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

# criando x y treino com oversampling 
over = RandomOverSampler()

x_over_train, y_over_train = over.fit_resample(x_train, y_train)

# setando modelo e seus parametros
model = GradientBoostingClassifier(
                                    n_estimators=117, 
                                    min_samples_split=25,
                                    min_samples_leaf=23,
                                    max_depth=18,
                                    max_leaf_nodes=14,
                                    learning_rate=0.0810962798100498,
                                    random_state=42
                                            )
column_transf = ColumnTransformer([
                                ('scaler', MinMaxScaler(), num_atribs),
                                ('one_hot', OneHotEncoder(handle_unknown='ignore'), cat_atribs)]
                                        
)
# setando pipeline
pipe = Pipeline(steps=[
    ('transf', column_transf),
    ('feat_selec', SelectFromModel(estimator=model)),
    ('model', model)
])

# treinando pipeline 
pipe.fit(x_over_train, y_over_train)
y_pred = pipe.predict(x_test)
acc = accuracy_score(y_pred=y_pred, y_true=y_test)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f'metricas: acuracia: {acc} precision: {precision} recall {recall}')
    
# salvando o modelo 
joblib.dump(pipe, 'modelo_gradientBoosting.pkl')

