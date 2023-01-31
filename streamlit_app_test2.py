# Streamlit-Google Sheet
## Modules
import streamlit as st 
from pandas import DataFrame

from gspread_pandas import Spread,Client
from google.oauth2 import service_account

# Application Related Module
import pubchempy as pcp
from pysmiles import read_smiles
# 
import networkx as nx
import matplotlib.pyplot as plt

from datetime import datetime

# Disable certificate verification (Not necessary always)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

st.write("gg")

# Create a Google Authentication connection object
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)
client = Client(scope=scope,creds=credentials)
spreadsheetname = "FuturesForwards"
spread = Spread(spreadsheetname,client = client)

# Check the connection
st.write(spread.url)
