from joblib import load
import streamlit as st

modeloRegressao = load("modeloRegressao.joblib")

st.header("Previsão do Nível do Rio em Rio do Sul")

with st.form("preverNivelRio"):
    nivelItuporanga = st.number_input("Nível do rio em Ituporanga (cm)")
    chuvaItuporanga = st.number_input("Chuva em Ituporanga")
    nivelTaio = st.number_input("Nível do rio em Taió (cm)")
    chuvaTaio = st.number_input("Chuva em Taió")

    enviar = st.form_submit_button("Enviar")

if(enviar):
    nivelRioDoSul = modeloRegressao.predict([[nivelItuporanga, chuvaItuporanga, nivelTaio, chuvaTaio]])[0][0]

    st.write(f"Nível do rio em Rio do Sul: {nivelRioDoSul:.2f} cm")