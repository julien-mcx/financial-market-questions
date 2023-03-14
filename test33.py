from st_aggrid import AgGrid

df = pd.read_excel("contoh.xlsx")
AgGrid(df)
