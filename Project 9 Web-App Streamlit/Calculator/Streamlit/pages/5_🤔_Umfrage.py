import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

st.title("Umfrage Ergebnisse")
st.write("---")
class Credentials:
    api_url = "https://api.sheety.co/986330bc80cb53b1444abc4dc001bec9/answersFortgeschritteneProgrammierung/formResponses1"


def get_data():    
    response = requests.get(Credentials.api_url)
    data = response.json()
    df = pd.DataFrame([[0,0]], columns = [["Streamlit", "Voila"]])
    for i in data["formResponses1"]:
        if i["wasFindetIhrBesser?"] == "Streamlit":
            df.Streamlit += 1
        elif i["wasFindetIhrBesser?"] == "Voila":
            df.Voila += 1    
    df.to_csv("UmfrageDaten.csv", index = False)    

df = pd.read_csv("UmfrageDaten.csv")
chart, ax = plt.subplots()
bars = ax.bar(x=df.columns, height=df.iloc[0], color=["black", "orange"])
ax.set_yticks([i for i in range(0,31,2)])
ax.bar_label(bars)
ax.set_xlabel("Frameworks")
ax.set_ylabel("Votes for which is better (WWI22DSB)")
"Ergebnisdiagramm", chart
if st.button("Update Chart"):
            get_data()

st.write("---")

st.video("https://www.youtube.com/watch?v=IxAKFlpdcfc")