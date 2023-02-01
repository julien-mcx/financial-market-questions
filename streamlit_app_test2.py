# streamlit_app.py

import streamlit as st
from gsheetsdb import connect

# Create a connection object.
conn = connect()

# # Perform SQL query on the Google Sheet.
# # Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]

import requests

response = requests.get(sheet_url)
response.raise_for_status()  # raises exception when not a 2xx response
if response.status_code != 204:
    return response.json()

st.write(response)
st.write(sheet_url)
st.write(conn)

# rows = run_query(f'SELECT * FROM "{sheet_url}"')

# # Print results.
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")
