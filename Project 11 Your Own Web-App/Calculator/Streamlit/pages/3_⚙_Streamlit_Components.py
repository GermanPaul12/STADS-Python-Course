import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import graphviz as graphviz
import seaborn as sns
import altair as alt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# st.code('')
st.set_page_config('Streamlit Components',page_icon='⚙')
# Sidebar
with st.sidebar:
    st.title("Sections")
    st.markdown("[Start](#streamlit-components)", unsafe_allow_html=True)
    with st.expander("Text"):
        st.markdown("[Basics with Text](#basic-text)", unsafe_allow_html=True)
        st.markdown("[Markdown](#markdown)", unsafe_allow_html=True)
        st.markdown("[Data Structures and Metrics](#data-structures-and-different-metrics)", unsafe_allow_html=True)
    
    with st.expander("Charts and Magic"):
        st.markdown("[Magic Features](#magic-features)", unsafe_allow_html=True)
        st.markdown("[Charts](#charts)", unsafe_allow_html=True)
        st.markdown("[Maps](#map)", unsafe_allow_html=True)
        st.markdown("[Graphs](#graphviz)", unsafe_allow_html=True)
        st.markdown("[More Charts](#seaborn-countplot)", unsafe_allow_html=True)
    

#! Text
st.title("Streamlit Components")
st.write("-----")
st.subheader("Basic Text")
st.header("Streamlit Title")
st.code('st.header("Streamlit Header")')
st.write("Basic Text")
st.code('st.write("Basic Text")')
st.subheader("Markdown")
st.markdown("# Hallo")
st.code('st.markdown("# Hallo")')
code = f"""def hello():
    print('Hello World')"""
st.code(code, language='python')    
st.code("st.code(<your_code>)")
# defining random values in a dataframe using pandas and numpy
st.subheader("Data Structures and Different Metrics")
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
# Highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

# Defining Metrics
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")


#Defining Columns
c1, c2, c3 = st.columns(3)
# Defining Metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")


#Defining Nested JSON
st.write("JSON Data")
st.json({ "Books" : [{
    "BookName" : "Python Testing with Selenium",
    "BookID" : "1",
    "Publisher" : "Apress",
    "Year" : "2021",
    "Edition" : "First",
    "Language" : "Python",
    },
    {
        "BookName": "Beginners Guide to Streamlit with Python",
        "BookID" : "2",
        "Publisher" : "Apress",
        "Year" : "2022",
        "Edition" : "First",
        "Language" : "Python"
    }]
} )
st.write("-------")

st.header("Charts and Magic")
st.write("-----------")

st.subheader("Magic Features")
# Math calculations with no functions defined
"Adding 5 & 4 =", 5+4
# Displaying Variable 'a' and its value 
a = 5
"a", a

st.code('''
        # Math calculations with no functions defined
        "Adding 5 & 4 =", 5+4
        # Displaying Variable 'a' and its value 
        a = 5
        "a", a
        ''')

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

st.code('''
        # Markdown with Magic
        """
        # Magic Feature
        Markdown working without defining its function explicitly.
        """
        ''')
# Dataframe using magic

df = pd.DataFrame({'col': [1,2]})
'dataframe', df

st.code("""
        import pandas as pd
        # Dataframe using magic
        df = pd.DataFrame({'col': [1,2]})
        'dataframe', df
        """)

# Magic working on Charts
st.subheader("Magic Chart")
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart
st.code('''
        s = np.random.logistic(10, 5, size=5)
        chart, ax = plt.subplots()
        ax.hist(s, bins=15)
        # Magic chart
        "chart", chart
    ''')

st.header("Charts")
#! Visualisation
# Defining random Values for Chart
st.subheader("Scatter Plot with Plotly Express")
df = pd.DataFrame(
     np.random.randn(10, 2),
     columns=['a', 'b'])
# Defining Chart
chart = px.scatter(df, x='a', y='b')
# Defining Chart in write() function
st.write(chart)
st.code("""
        # Defining random Values for Chart
        df = pd.DataFrame(
            np.random.randn(10, 2),
            columns=['a', 'b'])
        # Defining Chart
        chart = px.scatter(df, x='a', y='b')
        # Defining Chart in write() function
        st.write(chart)
        """)



st.title('Bar Chart with Streamlit')
# Defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"])
# Bar Chart
st.bar_chart(df)
st.code('''
        # Defining dataframe with its values
        df = pd.DataFrame(
            np.random.randn(40, 4),
            columns=["C1", "C2", "C3", "C4"])
        # Bar Chart
        st.bar_chart(df)
    ''')

st.title('Area')
# Defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"])
# Bar Chart
st.line_chart(df)
st.code('''
        # Defining dataframe with its values
        df = pd.DataFrame(
            np.random.randn(40, 4),
            columns=["C1", "C2", "C3", "C4"])
        # Bar Chart
        st.line_chart(df)
        ''')

st.title('Area')
# Defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"])
# Bar Chart
st.area_chart(df)
st.code('''
        # Defining dataframe with its values
        df = pd.DataFrame(
            np.random.randn(40, 4),
            columns=["C1", "C2", "C3", "C4"])
        ''')

st.title('Map')
# Defining Latitude and Longitude
locate_map = pd.DataFrame(
  np.random.randn(50, 2)/[10,10] + [49.348950, 8.689420],
  columns = ['latitude', 'longitude'])
# Map Function
st.map(locate_map)
st.code("""
        # Defining Latitude and Longitude
        locate_map = pd.DataFrame(
            np.random.randn(50, 2)/[10,10] + [49.348950, 8.689420],
            columns = ['latitude', 'longitude'])
        # Map Function
        st.map(locate_map)
        """)

st.title('Graphviz')
# Creating graph object
st.graphviz_chart('''
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"
} ''')
st.code("""
        # Creating graph object
        st.graphviz_chart('''
            digraph {
                "Training Data" -> "ML Algorithm"
                "ML Algorithm" -> "Model"
                "Model" -> "Result Forecasting"
                "New Data" -> "Model"
            } ''')
        """)


st.title('Graphviz')
# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('Training Data', 'ML Algorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')
st.graphviz_chart(graph)
st.code("""
        # Create a graphlib graph object
        graph = graphviz.Digraph()
        graph.edge('Training Data', 'ML Algorithm')
        graph.edge('ML Algorithm', 'Model')
        graph.edge('Model', 'Result Forecasting')
        graph.edge('New Data', 'Model')
        st.graphviz_chart(graph)
        """)

# Data Set
st.subheader("Seaborn Countplot")
df = pd.read_csv("Streamlit/data/avocado.csv")
# Defining Count Graph/Plot
fig = plt.figure(figsize=(10, 5))
sns.countplot(x = "year", data = df)
st.pyplot(fig)
st.code('''
        df = pd.read_csv("Streamlit/data/avocado.csv")
        # Defining Count Graph/Plot
        fig = plt.figure(figsize=(10, 5))
        sns.countplot(x = "year", data = df)
        st.pyplot(fig)
        ''')

# Import python libraries
# Data Set
st.subheader("Seaborn Violin Plot")
df = pd.read_csv("Streamlit/data/avocado.csv")
# Defining Violin Graph
fig = plt.figure(figsize=(10, 5))
sns.violinplot(x = "year", y="AveragePrice", data = df)
st.pyplot(fig)
st.code('''
        st.subheader("Seaborn Violin Plot")
        df = pd.read_csv("Streamlit/data/avocado.csv")
        # Defining Violin Graph
        fig = plt.figure(figsize=(10, 5))
        sns.violinplot(x = "year", y="AveragePrice", data = df)
        st.pyplot(fig)
        ''')

# Defining Strip Plot
st.subheader("Seaborn Strip Plot")
fig = plt.figure(figsize=(10, 5))
sns.stripplot(x = "year", y="AveragePrice", data = df)
st.pyplot(fig)
st.code('''
        fig = plt.figure(figsize=(10, 5))
        sns.stripplot(x = "year", y="AveragePrice", data = df)
        st.pyplot(fig)
        ''')

#Read albany Dataset
st.subheader("Altair Box Plot")
df = pd.read_csv("Streamlit/data/albany.csv")
# Box Plot
box_plot = alt.Chart(df).mark_boxplot().encode(
x = "Date",
    y = "Large Bags"
)
st.altair_chart(box_plot)
st.code('''
        df = pd.read_csv("Streamlit/data/albany.csv")
        # Box Plot
        box_plot = alt.Chart(df).mark_boxplot().encode(
        x = "Date",
            y = "Large Bags"
        )
        st.altair_chart(box_plot)
        ''')

#Read albany Dataset
st.subheader("Altair Area Plot")
df = pd.read_csv("Streamlit/data/albany.csv")
# Area Plot
area = alt.Chart(df).mark_area(color="orange").encode(
x = "Date",
    y = "Large Bags"
)
st.altair_chart(area)
st.code('''
        #Read albany Dataset
        df = pd.read_csv("Streamlit/data/albany.csv")
        # Area Plot
        area = alt.Chart(df).mark_area(color="orange").encode(
        x = "Date",
            y = "Large Bags"
        )
        st.altair_chart(area)
        ''')

#Read albany Dataset
st.subheader("Altair Heat Map")
df = pd.read_csv("Streamlit/data/albany.csv")
heat_map  = alt.Chart(df).mark_rect().encode(
        alt.Y('AveragePrice:Q'),
        alt.X('Large Bags:Q'),
        alt.Color('AveragePrice:Q'),
        tooltip = ['AveragePrice', 'type', 'Large Bags', 'Date']
    ).interactive()
st.altair_chart(heat_map)
st.code("""
        df = pd.read_csv("Streamlit/data/albany.csv")
        heat_map  = alt.Chart(df).mark_rect().encode(
                alt.Y('AveragePrice:Q'),
                alt.X('Large Bags:Q'),
                alt.Color('AveragePrice:Q'),
                tooltip = ['AveragePrice', 'type', 'Large Bags', 'Date']
            ).interactive()
        st.altair_chart(heat_map)
        """)


#Read Avocado Dataset
st.subheader("Plotly Pie Chart")
data = pd.read_csv("Streamlit/data/avocado.csv")
st.header("Avocado Pie Chart")
# Implementing Pie Plot
pie_chart = go.Figure(go.Pie(    
    labels = data.type,
    values = data.AveragePrice,
    hoverinfo = "label+percent",
    textinfo = "value+percent"
))
st.plotly_chart(pie_chart)
st.code('''
        data = pd.read_csv("Streamlit/data/avocado.csv")
        st.header("Avocado Pie Chart")
        # Implementing Pie Plot
        pie_chart = go.Figure(go.Pie(    
            labels = data.type,
            values = data.AveragePrice,
            hoverinfo = "label+percent",
            textinfo = "value+percent"
        ))
        st.plotly_chart(pie_chart)
        ''')

#Read Avocado Dataset
data = pd.read_csv("Streamlit/data/avocado.csv")
st.header("Plotly Donut Chart")
# Donut Chart
donut_chart = px.pie(
    names = data.type,
    values = data.AveragePrice,
    hole=0.25,
)
st.plotly_chart(donut_chart)
st.code('''
        data = pd.read_csv("Streamlit/data/avocado.csv")
        st.header("Donut Chart")
        # Donut Chart
        donut_chart = px.pie(
            names = data.type,
            values = data.AveragePrice,
            hole=0.25,
        )
        st.plotly_chart(donut_chart)
        ''')


#Data Set
data = pd.read_csv("Streamlit/data/avocado.csv")
st.header("Plotly Express Scatter Chart")
#Scatter
scat = px.scatter(
    x = data.Date,
    y = data.AveragePrice
)
st.plotly_chart(scat)
st.code('''
        #Scatter
        scat = px.scatter(
            x = data.Date,
            y = data.AveragePrice
        )
        st.plotly_chart(scat)
        ''')



# Data Set
data = pd.read_csv("Streamlit/data/avocado.csv")
# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]
#Line
line_chart = px.line(
    x = al_df["Date"],
    y = al_df["Large Bags"]
)
st.header("Plotly Express Line Chart")
st.plotly_chart(line_chart)
st.code('''
        # Data Set
        data = pd.read_csv("Streamlit/data/avocado.csv")
        # Minimizing Dataset
        albany_df = data[data['region']=="Albany"]
        al_df = albany_df[albany_df["year"]==2015]
        #Line
        line_chart = px.line(
            x = al_df["Date"],
            y = al_df["Large Bags"]
        )
        st.header("Line Chart")
        st.plotly_chart(line_chart)
        ''')


data = pd.read_csv("Streamlit/data/avocado.csv")
# Minimizing Dataset
st.subheader("Plotly Express Bar Chart")
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]
# Bar graph
bar_graph = px.bar(
    al_df,
    title = "Bar Graph",
    x = "Date",
    y = "Large Bags"
    )
st.plotly_chart(bar_graph)
st.code('''
        albany_df = data[data['region']=="Albany"]
        al_df = albany_df[albany_df["year"]==2015]
        # Bar graph
        bar_graph = px.bar(
            al_df,
            title = "Bar Graph",
            x = "Date",
            y = "Large Bags"
            )
        st.plotly_chart(bar_graph)
        ''')


#Bar Color
st.subheader("Plotly Express Colored Bar Chart")
bar_graph = px.bar(
    x = al_df["Date"],
    y = al_df["Large Bags"],
    title = "Bar Graph",
    color=al_df["Large Bags"]
)
st.plotly_chart(bar_graph)
st.code('''
        bar_graph = px.bar(
            x = al_df["Date"],
            y = al_df["Large Bags"],
            title = "Bar Graph",
            color=al_df["Large Bags"]
        )
        st.plotly_chart(bar_graph)
        ''')

st.subheader("Plotly Express H-Bar Plot")
# Data Set
data = pd.read_csv("Streamlit/data/avocado.csv")
# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]
# Horizontal Bar Graph
bar_graph = px.bar(
    al_df,
    x = "Large Bags",
    y = "Date",
    title = "Bar Graph",
    color="Large Bags",
    orientation='h'
)
st.plotly_chart(bar_graph)
st.code('''
        # Data Set
        data = pd.read_csv("Streamlit/data/avocado.csv")
        # Minimizing Dataset
        albany_df = data[data['region']=="Albany"]
        al_df = albany_df[albany_df["year"]==2015]
        # Horizontal Bar Graph
        bar_graph = px.bar(
            al_df,
            x = "Large Bags",
            y = "Date",
            title = "Bar Graph",
            color="Large Bags",
            orientation='h'
        )
        st.plotly_chart(bar_graph)
        ''')

st.subheader("Plotly Go Scatter Plot")
# Data Set
data = pd.read_csv("Streamlit/data/avocado.csv")
# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]
fig = make_subplots(rows=3, cols=1)
# First Subplot
fig.add_trace(go.Scatter(
    x=al_df["Date"],
    y=al_df["Total Bags"],
), row=1, col=1)
# Second SubPlot
fig.add_trace(go.Scatter(
    x=al_df["Date"],
    y=al_df["Small Bags"],
), row=2, col=1)
# Third SubPlot
fig.add_trace(go.Scatter(
   x=al_df["Date"],
   y=al_df["Large Bags"],
), row=3, col=1)
st.plotly_chart(fig)
st.code('''
        # Data Set
        data = pd.read_csv("Streamlit/data/avocado.csv")
        # Minimizing Dataset
        albany_df = data[data['region']=="Albany"]
        al_df = albany_df[albany_df["year"]==2015]
        fig = make_subplots(rows=3, cols=1)
        # First Subplot
        fig.add_trace(go.Scatter(
            x=al_df["Date"],
            y=al_df["Total Bags"],
        ), row=1, col=1)
        # Second SubPlot
        fig.add_trace(go.Scatter(
            x=al_df["Date"],
            y=al_df["Small Bags"],
        ), row=2, col=1)
        # Third SubPlot
        fig.add_trace(go.Scatter(
        x=al_df["Date"],
        y=al_df["Large Bags"],
        ), row=3, col=1)
        st.plotly_chart(fig)
        ''')

