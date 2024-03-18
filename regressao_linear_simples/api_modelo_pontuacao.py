from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe para validar os dados de entrada (request body)
class request_body(BaseModel):
    horas_de_estudo: float

# Carregar o modelo treinado
modelo_pontuacao = joblib.load('./modelo_pontuacao.pkl')

# Função para fazer a previsão de pontuação
@app.post('/predict_pontuacao')
def predict_pontuacao(data: request_body):
    # Preparar os dados para fazer a previsão
    input_feature = [[data.horas_de_estudo]]
    # Fazer a previsão
    y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)
    # Retornar a previsão
    return {'pontuacao': y_pred.tolist()}

# Criar um endpoint para a API
