import streamlit as st

def start()
    # menu = ["Frequent Visitors","Visitor Length","404 Codes","User Statistics"]
    # choice = st.sidebar.selectbox("Metrics", menu)
    # header_list = ['IP', 'Timestamp', 'Request', 'Status_code']
    uploaded_file = st.file_uploader("Choose a log file")
    if uploaded_file is not None:
        try:
            df=pd.read_csv("/content/drive/MyDrive/Logfile-analysis.xlsx",names=['index','IP','date_time','request','res_code'],header=None)
            except:
                try:
                    df=pd.read_excel("/content/drive/MyDrive/Logfile-analysis.xlsx",names=['index','IP','date_time','request','res_code'],header=None)
                except:
                    print("Upload either csv or excel file")