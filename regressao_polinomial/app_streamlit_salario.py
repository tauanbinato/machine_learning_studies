import streamlit as st
import json
import requests

# Titulo da Aplicação
st.title('Modelo de predição de Salário')

# Inputs
st.write('Por favor, preencha os campos abaixo:')
tempo_na_empresa = st.slider('Tempo na Empresa (Meses)', min_value=1, max_value=150, value=5, step=1)
nivel_na_empresa = st.slider('Nível na Empresa ', min_value=1, max_value=10, value=1, step=1)

# Preparar dados para enviar para a API
input_features = {
    "tempo_na_empresa": tempo_na_empresa,
    "nivel_na_empresa": nivel_na_empresa
}

# Botão para fazer a previsão
if st.button('Prever Salário'):
    # Enviar os dados para a API
    res = requests.post(url='http://localhost:8000/predict', data=json.dumps(input_features))
    res_json = json.loads(res.text)

    salario_em_reais = round(res_json['salario_em_reais'])

    # Mostrar o resultado
    st.subheader(f'Salário Previsto: R$ {salario_em_reais}')
