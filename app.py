import streamlit as st
import pandas as pd
import joblib

# Load model files
model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("Heart Disease Prediction❤️")

age = st.number_input("Age", 1, 120, 30)
bp = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol", value=200)
fast = st.selectbox("Fasting Blood Sugar", [0,1])
hr = st.number_input("Maximum Heart Rate", value=150)
old = st.number_input("Oldpeak", value=0.0)

sex = st.selectbox("Sex", ["Female","Male"])
cp = st.selectbox("Chest Pain Type", ["ASY","ATA","NAP","TA"])
ecg = st.selectbox("Resting ECG", ["LVH","Normal","ST"])
angina = st.selectbox("Exercise Angina", ["No","Yes"])
slope = st.selectbox("ST Slope", ["Down","Flat","Up"])

data = dict.fromkeys(columns,0)

data["Age"]=age
data["RestingBP"]=bp
data["Cholesterol"]=chol
data["FastingBS"]=fast
data["MaxHR"]=hr
data["Oldpeak"]=old

if sex=="Male":
    data["Sex_M"]=1

if cp=="ATA":
    data["ChestPainType_ATA"]=1
elif cp=="NAP":
    data["ChestPainType_NAP"]=1
elif cp=="TA":
    data["ChestPainType_TA"]=1

if ecg=="Normal":
    data["RestingECG_Normal"]=1
elif ecg=="ST":
    data["RestingECG_ST"]=1

if angina=="Yes":
    data["ExerciseAngina_Y"]=1

if slope=="Flat":
    data["ST_Slope_Flat"]=1
elif slope=="Up":
    data["ST_Slope_Up"]=1

df=pd.DataFrame([data])

scaled=scaler.transform(df)

if st.button("Predict"):
    prediction=model.predict(scaled)

    if prediction[0]==1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")
