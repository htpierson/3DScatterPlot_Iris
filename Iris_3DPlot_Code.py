import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
import plotly as plt
import plotly.express as px

iris = load_iris()
labels = iris.feature_names
targets = iris.target
print(labels)

st.write('''
#Iris Data Set
How are sepal length, sepal width, and petal width related in different iris species?
''')

df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
st.plotly_chart(fig, use_container_width=True)
