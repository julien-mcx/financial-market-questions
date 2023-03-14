from st_aggrid import AgGrid

df = pd.read_excel("QuestionsFinancedeMarche.xlsx")
AgGrid(df)
