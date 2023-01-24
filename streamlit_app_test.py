from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
def forward_future():
    st.write("Un contrat future est un accord entre deux parties, l'une acheteuse (ou long), l'autre vendeuse (ou short), souhaitant s’échanger un sous-jacent à une date future, à un prix fixé à l’avance.")
    st.write("Les origines des contrats à terme sont anciennes. Si, dès la Mésopotamie ancienne, certaines formes d’accords circulaient déjà, notamment grâce au Code de Hammurabi, il faudra néanmoins attendre le milieu du XIXème siècle pour voir émerger une Bourse dédiée et organisée, aux Etats-Unis, avec le Chicago Board of Trade (CBOT). \
        Un premier contrat forward, sur le blé, est ainsi signé le 13 mars 1851. Quelques années plus tard, en 1865, les contrats futures standardisés font leur apparition.")
    st.write("Un contrat forward est un accord d'achat ou de vente d'un actif (appelé sous-jacent) à une date future T (appelée la maturité) pour un certain prix (appelé le prix d'exercice).")
    st.write("Un éventail large de matières premières et actifs financiers forment ce que l'on appelle actif sous-jacent")


if __name__ == '__main__':
    forward_future()
