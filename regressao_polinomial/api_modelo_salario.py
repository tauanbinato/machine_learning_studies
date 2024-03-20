from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe para os dados de entrada
class request_body(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int

# Carregar o modelo
model_poly = joblib.load('./modelo_salario_pol.pkl')

# Criar a rota
@app.post('/predict')
def predict(data: request_body):
    input_features = {
        'tempo_na_empresa': data.tempo_na_empresa,
        'nivel_na_empresa': data.nivel_na_empresa
    }
    # Criar um dataframe com os dados de entrada
    pred_df = pd.DataFrame(input_features, index=[1])
    # Fazer a previsão
    y_pred = model_poly.predict(pred_df)[0].astype(float)
    return {'salario_em_reais': y_pred.tolist() }
