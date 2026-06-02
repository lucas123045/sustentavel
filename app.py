
import streamlit as st
import pandas as pd
import random

st.title("🚀 Orion Energy Monitor AI")

temp = random.randint(20, 100)
energia = random.randint(5, 100)
comunicacao = random.choice(["ONLINE", "OFFLINE"])
fonte = random.choice(["Solar", "Bateria", "Eólica Simulada"])

st.metric("Temperatura", f"{temp} °C")
st.metric("Energia", f"{energia}%")
st.metric("Comunicação", comunicacao)
st.metric("Fonte de Energia", fonte)

if temp > 80:
    st.error("ALERTA CRÍTICO: Temperatura elevada")

if energia < 20:
    st.warning("ALERTA: Baixa energia")

if comunicacao == "OFFLINE":
    st.error("ALERTA: Falha de comunicação")

if energia < 15:
    st.info("Ação automática: módulos não essenciais desligados")
