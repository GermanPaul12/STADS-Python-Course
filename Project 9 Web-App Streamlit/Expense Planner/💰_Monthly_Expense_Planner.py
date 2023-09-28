import streamlit as st

st.set_page_config(page_title='Expense Planner',page_icon='💰')
st.title("Monthly Expense Planner")

st.subheader(":orange[Add row]")  

if "income_rows" not in st.session_state: st.session_state["income_rows"] = []
if "expense_rows" not in st.session_state: st.session_state["expense_rows"] = []
if "income_sources" not in st.session_state: st.session_state["income_sources"] = []
if "expense_sources" not in st.session_state: st.session_state["expense_sources"] = []

def add_row_to_list(typee,label):
    if label == "":
        st.warning("Please provide a label for the row!", icon="🚨")    
    elif typee == "Income":
        if label not in st.session_state.income_rows: st.session_state.income_rows.append(label)
    else:
        if label not in st.session_state.expense_rows: st.session_state.expense_rows.append(label) 
        
           
col1, col2 = st.columns(2)
with col1:
    income_or_expense = st.selectbox("Type", ["Income", "Expense"], index=1)
with col2:
    row_label = st.text_input("Row Label")    
add_button = st.button("Add Row", on_click=add_row_to_list, args=(income_or_expense, row_label))    


st.subheader(":green[Income]")        
income = st.number_input("Salary")
st.session_state.income_sources = []
st.session_state.income_sources.append(income)
for i,e in enumerate(st.session_state.income_rows):
    inco = st.number_input(e, key=f"IncomeNr{i}")
    st.session_state.income_sources.append(inco)
sum_income = st.markdown(f":green[Total Income: {sum(st.session_state.income_sources)}]")


st.subheader(":red[Expenses]")    
st.session_state.expense_sources = []
for i,c in enumerate(st.session_state.expense_rows):
    expo = st.number_input(c, key=f"ExpenseNr{i}")
    st.session_state.expense_sources.append(expo)
sum_expenses = st.markdown(f":red[Total Expenses: {sum(st.session_state.expense_sources)}]")

st.subheader("Total")
if sum(st.session_state.income_sources) - sum(st.session_state.expense_sources) > 0:
    st.markdown(f":green[Balance: {sum(st.session_state.income_sources) - sum(st.session_state.expense_sources):.2f}]")
elif sum(st.session_state.income_sources) - sum(st.session_state.expense_sources) < 0:
    st.markdown(f":red[Balance: {sum(st.session_state.income_sources) - sum(st.session_state.expense_sources):.2f}]")    
else:
    st.markdown(f":orange[Balance: {sum(st.session_state.income_sources) - sum(st.session_state.expense_sources):.2f}]")   