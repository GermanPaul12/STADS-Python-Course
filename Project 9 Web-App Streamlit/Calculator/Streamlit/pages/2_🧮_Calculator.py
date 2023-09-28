import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


st.set_page_config('Calculator',page_icon='🧮')
state = st.session_state

def main():
    if 'calc_list' not in state:
        state.calc_list = []
    # Sidebar
    with st.sidebar:
        st.title("Sections")
        st.markdown("[*Start*](#calculator-app-using-streamlit)", unsafe_allow_html=True)
        st.markdown("[*Simple Calculator*](#simple-calculator)", unsafe_allow_html=True)
        st.markdown("[*CSV Calculator*](#csv-calculator)", unsafe_allow_html=True, help='Go to CSV-Calculator')
    
    # Calculator
    with st.container():
        st.title("Calculator App using Streamlit")
        st.write("---")  # creates a horizontal line
        st.header("Simple Calculator",)
        st.write("---")  # creates a horizontal line
        
        st.write("Operation")
        op = st.radio(
            "Select an operation to perform:",
            ("Add ( + )", "Subtract ( - )", "Multiply ( * )", "Divide ( / )"),
            key='operationCalc'
        )
        
        num1 = st.number_input(label="Enter first number",value=0.0,step=1.0,format='%s',key='number1')
        num2 = st.number_input(label="Enter second number",value=0.0,step=1.0,format='%s',key='number2')
        calculate(num1, num2, op)
        
        history_list = False
        if len(state.calc_list)>0:
            history_list = True
        with st.expander("History List of the last 10 calculations",expanded=history_list):
            if len(state.calc_list)==11:
                state.calc_list.pop(0)
            if len(state.calc_list) > 0:
                for ind,value in enumerate(state.calc_list[::-1],start=1):
                    st.write(ind,':',value)
            else:
                st.write("No previous calculations")            
        st.write("---")  # creates a horizontal line

    # CSV - Calculator
    with st.container():
        st.header("CSV Calculator")
        st.write("---")
        st.subheader("Please provide a csv as shown in the example below. Column names should be the same.")
        df = pd.read_csv("Streamlit/data/calc_csv.csv")
        df

        st.subheader("Upload Csv")
        
        csv_file = st.file_uploader("Upload your csv file to calculate results for whole dataset",
                                    type=["csv"])
        if csv_file:
            df = pd.read_csv(csv_file)

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                calc_result = st.button("Calculate result ad create insights", key='csv')
            with col2:
                save_file = st.button("Download Csv")
        
        if calc_result:
            with st.expander("Expand to see results",expanded=True):     
                df["result"] = [calculate(df.num1.iloc[i], df.num2.iloc[i],
                                        df.op.iloc[i], return_message=False) for i in range(len(df))]
                df     
                op_count = df.op.value_counts()
                bar = px.bar(op_count, title="How many operations are there in the dataset for each operator")
                pie = px.pie(op_count, values="count", names=op_count.index, title="Distribution of operators in the dataset")
                st.plotly_chart(bar)
                st.plotly_chart(pie)   
            
        
        if save_file:
            if csv_file is not None:
                # To See details
                csv_details = {"file_name":csv_file.name,
                "file_type":csv_file.type,
                                "file_size":csv_file.size}
                st.write(csv_details)
                # To save uploaded Csv
                results = [calculate(df.num1.iloc[i], df.num2.iloc[i],
                                    df.op.iloc[i], return_message=False) for i in range(len(df))]

                df["result"] = results     
                df.to_csv("downloaded_streamlit_csv.csv", index=False)       
                    
                st.success("Csv Saved Successfully")
                
            else:
                st.warning("No Csv File is Uploaded")     
   
# ---- METHODES ----
def add_calculation_to_history(calculation:(str))->None:
    '''
    Adds given calculation to the history
    @param calculation: The calculation to add to history
    '''
    state.calc_list.append(calculation) 

@st.cache_data
def calculate(num1:(int or float), num2:(int or float), op:(str), return_message:(bool)=True)->(int or float):
    '''
    Calculate any numbers with basic operators
    @param num1: Set to any numeric
    @param num2: Set to any numeric
    @param op: Choose your operator of choice
    @param return_message: Let's you choose between displaying only a return message of your calculation or returning the result default: True
    @return: Returns your mathematic result
    '''
    ans = 0
    if (op == '+') or (op=='Add ( + )'):
        operator = '+'
        ans = num1 + num2
    elif (op == "-") or (op =='Subtract ( - )'):
        operator = '-'
        ans = num1 - num2
    elif (op == "*") or (op =='Multiply ( * )'):
        operator = '*'
        ans = num1 * num2
    elif (op == "/") or (op =='Divide ( / )'):
        operator = '/'
        if num2 != 0:
            ans = num1 / num2
        else:
            st.error(":color[:red[ERROR:]] Division by 0. Please enter a non-zero number.")
            ans = np.NaN
            st.error(f"{state['number1']} {operator} :red[{state['number2']}] = {ans}")
            return ans
    else:
        st.error('This should not happen! Please report to the authorities')
    if return_message:
        add_calculation_to_history(f"{state['number1']} {operator} {state['number2']} = {round(ans,10)}")
        st.success(f"{state['number1']} {operator} {state['number2']} = {round(ans,10)}")
        return ans
    else:
        return ans

if __name__ == '__main__':
    main()
