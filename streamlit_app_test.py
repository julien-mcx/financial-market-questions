from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import requests


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
st.write("test")
def primarychoice():
    st.sidebar.info("This app is maintained by Michoux Julien. " "You can contact me at [ju.michoux@gmail.com].")
    st.sidebar.title("Let's choose your asset type")
    l_assettype = ['Future /Forward', 'Equity', 'other']
    l_assettypechoice = st.sidebar.radio("Choose your asset type : ", l_assettype)

    if l_assettypechoice == 'Future /Forward':
        forward_future()
        
def possibilities_via_dictionnary(p_question):
    l_question = p_question
    data = {'Question_1': ['Choose','VRAI','FAUX'],\
        'Question_2': ['Choose','VRAI','FAUX'],\
        'Question_3': ['Choose','VRAI','FAUX'], \
        'Question_4': ['Choose','VRAI','FAUX'],\
        'Question_5': ['Choose','VRAI','FAUX'], \
        'Question_6': ['Choose','VRAI','FAUX'],\
        'Question_7': ['Choose','VRAI','FAUX'],\
        'Question_8': ['Choose','VRAI','FAUX'],\
        'Question_9': ['Choose','VRAI','FAUX'],\
        'Question_10': ['Choose','VRAI','FAUX'],\
        'Question_11': ['Choose','A=1 & B=2','A=2 & B=1', ],\
        'Question_12': ['Choose','VRAI','FAUX'],\
        'Question_13': ['Choose','VRAI','FAUX'],\

        }
    l_possibiitiesforonequestion = (data[f'{l_question}'])
    return(l_possibiitiesforonequestion)

def forward_future():
    st.write("Un contrat future est un accord entre deux parties, l'une acheteuse (ou long), l'autre vendeuse (ou short), souhaitant s’échanger un sous-jacent à une date future, à un prix fixé à l’avance.")
    st.write("Les origines des contrats à terme sont anciennes. Si, dès la Mésopotamie ancienne, certaines formes d’accords circulaient déjà, notamment grâce au Code de Hammurabi, il faudra néanmoins attendre le milieu du XIXème siècle pour voir émerger une Bourse dédiée et organisée, aux Etats-Unis, avec le Chicago Board of Trade (CBOT). \
        Un premier contrat forward, sur le blé, est ainsi signé le 13 mars 1851. Quelques années plus tard, en 1865, les contrats futures standardisés font leur apparition.")
    st.write("Un contrat forward est un accord d'achat ou de vente d'un actif (appelé sous-jacent) à une date future T (appelée la maturité) pour un certain prix (appelé le prix d'exercice).")
    st.write("Un éventail large de matières premières et actifs financiers forment ce que l'on appelle actif sous-jacent")
    
    test = pd.read_excel('https:\\github.com\\julien-mcx\\financial-market-questions\\blob\\main\\Questions.xlsx')
    st.write(test)
    myfile = requests.get(url)

    df=pd.read_excel(myfile.content)
    print(df)
    
# excel_file = 'Questions.xlsx'

# df = pd.read_excel(excel_file,
#                   sheet_name=sheet_name,
#                   usecols='B:D',
#                header=3)
# st.write(df)
    
if __name__ == '__main__':
    primarychoice()
