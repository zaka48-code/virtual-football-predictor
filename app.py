import streamlit as st

st.title("Virtual Football Predictor")

team = st.text_input("Equipe cible")

results = st.file_uploader("Capture résultats récents")
ranking = st.file_uploader("Capture classement")
next_match = st.file_uploader("Capture prochains matchs")

if st.button("Analyser"):
    st.write("Analyse en cours...")

    prediction = "Victoire probable"

    st.success(prediction)
