import streamlit as st
import pandas as pd
import os

ARQUIVO_VOTOS = "votos.csv"
opcoes = ["Python", "JavaScript", "Java", "C#", "Outro"]

# Inicializar arquivo de votos se não existir
if not os.path.exists(ARQUIVO_VOTOS):
    pd.DataFrame({"opcao": opcoes, "votos": [0] * len(opcoes)}).to_csv(ARQUIVO_VOTOS, index=False)

# Carregar votos
df = pd.read_csv(ARQUIVO_VOTOS)

st.title("📊 Enquete: Qual sua linguagem favorita?")
escolha = st.radio("Escolha uma opção:", opcoes)

if st.button("Votar"):
    df.loc[df["opcao"] == escolha, "votos"] += 1
    df.to_csv(ARQUIVO_VOTOS, index=False)
    st.success(f"Obrigado por votar em {escolha}!")

# Mostrar resultados
st.subheader("🔍 Resultado parcial:")
st.bar_chart(df.set_index("opcao")["votos"])
