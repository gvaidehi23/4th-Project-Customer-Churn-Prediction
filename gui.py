import pandas as pd
import numpy as np
import pickle
import streamlit as st
import matplotlib.pyplot as plt

pipe = pickle.load(open("pipe.pkl","rb"))
df = pd.read_csv('cleaned_data.csv')

st.title('🔍 Customer Churn Prediction App')


# setting bckground img
import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("custchurn.png")

st.markdown(f"""
<style>
.stApp {{
    background-image:
        linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.15)),
        url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)


# main heading on sidebar
st.sidebar.markdown("""<h1 style = "font-size : 20px; color : white;font-weight : bold; font-size : 28px">🤖&nbsp;&nbsp;ChurnPredict</h1>""", unsafe_allow_html = True)
st.sidebar.image("img1.png")
st.sidebar.markdown("""<h4 style = 'color : #87CEFA;'>⚪ Predict customer churn with AI.</h4>""",unsafe_allow_html=True)
st.sidebar.image("img2.png")
st.sidebar.markdown("""<h4 style = 'color : #87CEFA;'>⚪ Keep your customers loyal.</h4>""",unsafe_allow_html=True)
st.sidebar.image("img3.png")
st.sidebar.markdown("""<h4 style = 'color : #87CEFA;'>⚪ Every customer matters.</h4>""",unsafe_allow_html=True)
st.sidebar.image("img4.png")
st.sidebar.markdown("""<h4 style = 'color : #87CEFA;'>⚪ Understand customer behavior instantly.</h4>""",unsafe_allow_html=True)
st.sidebar.image("img5.png")
st.sidebar.markdown("""<h4 style = 'color : #87CEFA;'>⚪ Empowering smarter customer retention.</h4>""",unsafe_allow_html=True)




# setting sidebar bckground color
st.markdown("""
<style>
.stApp {
[data-testid="stSidebar"] {
    background: linear-gradient(to top, #0B1F3A, #1E3A5F, #4A6FA5);   
}
}
</style>
""", unsafe_allow_html=True)



# setting color to other small txt
st.markdown("""<style>
            label{color : #000000 !important; 
            }
            </style>""",unsafe_allow_html = True)




# creating selectboxes and other content inside sidebar

st.markdown("""<h4 style = 'color : #00004D;'>📝 Fill above details:</h4>""",unsafe_allow_html=True)

col1,space,col2 = st.columns([3,0.5,3])
custid = sorted(df['customerID'].unique())

with col1:
    customerID = st.selectbox('⚪ Select Customer ID',custid)
    gender = st.selectbox('⚪ Select Gender:',['Female', 'Male'])
    SeniorCitizen = st.selectbox('⚪ Senior citizen ?',['Yes', 'No'])
    Partner = st.selectbox('⚪ Partner ?',['Yes', 'No'])
    Dependents = st.selectbox('⚪ Dependents ?',['Yes', 'No'])
    tenure = st.number_input('⚪ Tenure (in months) :',value = 1,min_value = 1, max_value = 200, step = 50)
    PhoneService = st.selectbox('⚪ Phone Service ?',['Yes', 'No'])
    MultipleLines = st.selectbox('⚪ Multiple Lines ?',['Yes', 'No'])
    InternetService = st.selectbox('⚪ Internet Service :',sorted(df['InternetService'].unique()))
    OnlineSecurity = st.selectbox('⚪ Security Service ?',['Yes', 'No'])
with col2:    
    OnlineBackup = st.selectbox("⚪ Online Backup ?",['Yes','No'])
    DeviceProtection = st.selectbox('⚪ Device Protection Service ?',['Yes', 'No'])    
    TechSupport = st.selectbox('⚪ Tech Support Service ?',['Yes', 'No'])
    StreamingTV = st.selectbox('⚪ Streaming TV Subscription ?',['Yes', 'No'])
    StreamingMovies = st.selectbox('⚪ Streaming Movies subscription ?',['Yes', 'No'])
    Contract = st.selectbox('⚪ Contract Type:',sorted(df['Contract'].unique()))
    PaperlessBilling = st.selectbox('⚪ Paperless Billing ?',['Yes', 'No'])
    PaymentMethod = st.selectbox('⚪ Payment Method:',sorted(df['PaymentMethod'].unique()))
    MonthlyCharges = st.number_input("⚪ Monthly Charges:",value = 1, min_value = 1, max_value = 5000)
    TotalCharges = st.number_input("⚪ Total Charges:",value = 1, min_value = 1, max_value = 10000)



# enhance button look
st.markdown("""
<style>
div.stButton > button {
    background: #87CEEB;
    color: #4B0082;
    font-size: 20px;
    font-weight: 700;
    border: 2px solid rgba(255,255,255,0.2);
    border-radius: 15px;
    padding: 14px;
    width: 100%;
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)


Press = st.button('Predict Churn')
if Press:
    gender1 = 0 if gender=='Female' else 1
    SeniorCitizen1 = 1 if SeniorCitizen=='Yes' else 0
    Partner1 = 1 if Partner=='Yes' else 0
    Dependents1 =  1 if Dependents=='Yes' else 0
    PhoneService1 = 1 if PhoneService=='Yes' else 0

    MultipleLines1 = 1 if MultipleLines=='Yes' else 0
    OnlineSecurity1 = 1 if OnlineSecurity=='Yes' else 0
    OnlineBackup1 =  1 if OnlineBackup=='Yes' else 0
    DeviceProtection1 =  1 if DeviceProtection=='Yes' else 0
    TechSupport1 =  1 if TechSupport=='Yes' else 0
    StreamingTV1 =  1 if StreamingTV=='Yes' else 0
    StreamingMovies1 =  1 if StreamingMovies=='Yes' else 0
    PaperlessBilling1 =  1 if PaperlessBilling=='Yes' else 0


    myip = [[customerID, gender1, SeniorCitizen1, Partner1, Dependents1,
    tenure, PhoneService1, MultipleLines1, InternetService,
    OnlineSecurity1, OnlineBackup1, DeviceProtection1, TechSupport1,
    StreamingTV1, StreamingMovies1, Contract, PaperlessBilling1,
    PaymentMethod, MonthlyCharges, TotalCharges]]
    col = ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
    'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
    'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
    'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
    table = pd.DataFrame(data = myip, columns = col)
    result = pipe.predict(table)

    prob = pipe.predict_proba(table)[0]
    stay = prob[0] * 100
    leave = prob[1] * 100
    
    if result[0] == 1:
         st.title("")
         st.markdown("""
       <div style="
       background: linear-gradient(135deg,#ff6b6b,#ff3b3b);
       padding:15px;
       border-radius:12px;
       color:white;
       font-size:18px;
       font-weight:bold;
       box-shadow:0px 4px 12px rgba(0,0,0,0.2);
       ">🔴 The customer may discontinue the service.
       </div>
       """, unsafe_allow_html=True)
        
    else:
        st.title("")
        st.markdown("""
        <div style="
        background: linear-gradient(135deg,#2ecc71,#27ae60);
        padding:15px;
        border-radius:12px;
        color:white;
        font-size:18px;
        font-weight:bold;
        box-shadow:0px 4px 12px rgba(0,0,0,0.2);
        ">
       🟢 This customer is likely to continue using the service.
        </div>
        """, unsafe_allow_html=True)

    st.title("")
    # ploting pie chart

    st.markdown("""<h4 style = 'color : #00004D;'>📊 Graphical representation:</h4>""",unsafe_allow_html=True)

    labels = ["Will Stay", "Will Leave"]
    sizes = [stay, leave]

    fig, ax = plt.subplots(figsize=(1.8, 1.8))

    ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    colors=["#42A5F5", "#EF5350"],
    startangle=90,
    textprops={"fontsize": 5}
    )

    ax.axis("equal")
    st.pyplot(fig)

st.title("")
st.markdown("<h6 style = 'color : #87CEFA;'>Note : This application predicts whether a customer is likely to churn based on key factors such as contract type, tenure, monthly charges, internet service, payment method, and other customer-related information. The prediction is generated using a trained machine learning model to help businesses identify at-risk customers and take proactive retention measures. Results are predictive estimates and should be used to support, not replace, business decisions.</h6>",unsafe_allow_html=True)











