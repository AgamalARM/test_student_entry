# -*- coding: utf-8 -*-
"""
Created on Tue May 10 03:25:56 2022

@author: Gamal
"""

import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
st.write(df)
Sensor_value = np.array([2])
df['student'] = Sensor_value

foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)

trend_value = np.array([foo])
df[bar] = trend_value


@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


csv = convert_df(df)
print(csv)
st.write(df)
st.write(csv)

df.to_csv (r'data.csv', index = False, header=True)



import pandas as pd

@st.cache(allow_output_mutation=True)
def get_data():
    return []

user_id = st.text_input("User ID")
foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)

if st.button("Add row"):
    get_data().append({"UserID": user_id, "foo": foo, "bar": bar})

st.write(pd.DataFrame(get_data()))




import numpy as np
#import SessionState 

# https://gist.githubusercontent.com/tvst/036da038ab3e999a64497f42de966a92/raw/f0db274dd4d295ee173b4d52939be5ad55ae058d/SessionState.py

# Create an empty dataframe
data = pd.DataFrame(columns=["Random"])
st.text("Original dataframe")

# with every interaction, the script runs from top to bottom
# resulting in the empty dataframe
st.dataframe(data) 

# persist state of dataframe
session_state = SessionState.get(df=data)

# random value to append; could be a num_input widget if you want
random_value = np.random.randn()

if st.button("Append random value"):
    # update dataframe state
    session_state.df = session_state.df.append({'Random': random_value}, ignore_index=True)
    st.text("Updated dataframe")
    st.dataframe(session_state.df)

# still empty as state is not persisted
st.text("Original dataframe")
st.dataframe(data)