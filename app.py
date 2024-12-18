import streamlit as st
import pandas as pd
import pickle as pk
model =pk.load(open("model.pkl",'rb'))
scaler=pk.load(open("scaler.pkl",'rb'))

st.header("Load Pridiction App")
no_of_Dependents=st.slider("Choose NO of Dependents",0,5)
Education=st.selectbox("Choose Education",['Graduated','Not Graduated'])
Employed=st.selectbox("Self Employed",['Yes','No'])
Income=st.slider('Choose Anuual Income',0,10000000)
Loan_Amount=st.slider('Choose Loan Amount',0,10000000)
Loan_Duration=st.slider('Choose Loan Duration ',0,20)
Cibil=st.slider('Choose cibil score',0,1000)
Residentail=st.slider('Choose Residential Assets',0,10000000)
Commerical=st.slider('Choose Commerical_Assets',0,10000000)
Luxury=st.slider('Choose Luxury_Assets',0,10000000)
Bank=st.slider('Choose Bank_Assets',0,10000000)
Assets_value=st.slider('choose Assets_value',0,10000000)
if Education =="Graduated":
    Education_s=1
else:
    Education_s=0

if Education =="No":
    Employed_s=0
else:
    Employed_s=1
if st.button("Predict"):
    pridict_p=pd.DataFrame([[no_of_Dependents,Education_s,Employed_s,Income,Loan_Amount,Loan_Duration,Cibil,Residentail,Commerical,Luxury,Bank,Assets_value]],columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Residentail','commercial_assets_value','luxury_assets_value','bank_assets_value','Assets'])
    pridict_p=scaler.fit_transform(pridict_p)
    predict_p=model.predict(pridict_p)
    if predict_p[0]==1:
        st.markdown("Loan Request Is Approved")
    elif predict_p[0]==0:
        st.markdown("Loan Request Is Rejected")
    else:
        st.markdown("Loan Request Is Rejected")
