from sklearn import metrics
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
from collections import Counter
import matplotlib.pyplot as plt
import urllib.request
import json
import seaborn as sns

def importDataframe():
    uploaded_file = st.file_uploader("Choose a log file")
    if uploaded_file is not None:
        global df
        try:
            df=pd.read_csv(uploaded_file)
        except:
            try:                
                df=pd.read_excel(uploaded_file)
            except:
                print("Upload either csv or excel file")
        return df

def displayMetrics():
    col1,col2 = st.columns([3,9])
    col1.write("# Metrics")
    choice = col2.selectbox("",metrics)

def systemStat():
    se_count=Counter(df["search_engine"])
    st.write(se_count)    
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x=list(se_count.keys()),y=list(se_count.values()))
    st.pyplot(fig)

def demographics():
    ips = df["IP"].unique()
    d=[]
    for ip1 in ips:
        with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+str(ip1)) as url:
            data = url.read().decode()
            data = data.split("(")[1].strip(")")
            d.append(data)
    d=set(d)
    for x in d:
        st.write(x)

def start():
    cols=st.columns([3,4,2])
    cols[1].image("icon.png",width=150)

    cols=st.columns([2,8,2])
    cols[1].title("|....... Log Spy  ......|")
    st.write("")

    df=importDataframe()

    metrics=[]
    if df is not None:
        cols=list(df.columns)
        cols=[x.lower() for x in cols]
        st.write(cols)
        if 'search_engine' in cols:
            metrics.append('System stat')
            systemStat()
        if 'ip' in cols:
            metrics.append('Demographics')
            demographics()

    