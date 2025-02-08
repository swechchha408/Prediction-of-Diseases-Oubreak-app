import os  # interact with the file system and using it to determine the directory of code
import pickle  # pre-trained models loading
import streamlit as st  # web application
from streamlit_option_menu import option_menu  # creates stylish sidebar menu

st.set_page_config(page_title='Prediction of Disease Outbreak',
                   layout='wide',
                   page_icon='🩺')

# Define file paths
diabetes_model_path = 'D:\PREDICTIONS\saved_models\diabetes_logistic_model.sav'
heart_model_path = 'D:\PREDICTIONS\saved_models\heart_logistic_model.sav'
parkinson_model_path = 'D:\PREDICTIONS\saved_models\parkinsons_decision_tree_model.sav'

# Check if files exist and load models
if os.path.exists(diabetes_model_path):
    diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
else:
    st.error(f"File not found: {diabetes_model_path}")

if os.path.exists(heart_model_path):
    heart_model = pickle.load(open(heart_model_path, 'rb'))
else:
    st.error(f"File not found: {heart_model_path}")

if os.path.exists(parkinson_model_path):
    parkinson_model = pickle.load(open(parkinson_model_path, 'rb'))
else:
    st.error(f"File not found: {parkinson_model_path}")

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.number_input('Number of Pregnancies')
    with col2:
        glucose = st.number_input('Glucose level')
    with col3:
        blood_pressure = st.number_input('Blood Pressure value')
    with col1:
        skin_thickness = st.number_input('Skin Thickness value')
    with col2:
        insulin = st.number_input('Insulin level')
    with col3:
        bmi = st.number_input('BMI value')
    with col1:
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value')
    with col2:
        age = st.number_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Results'):
        input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
        input_data = [float(x) for x in input_data]  # converting to float because the model was trained on float data and the user inputs are taken as strings
        diab_prediction = diabetes_model.predict([input_data])  # predicting the input data
        if diab_prediction[0] == 1:  # slicing the prediction to get the result of the prediction and comparing it to 1
            diab_diagnosis = 'The Person is diabetic'
        else:
            diab_diagnosis = 'The Person is not diabetic'
        st.write(diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age')
    with col2:
        sex = st.number_input('Sex (1 = male; 0 = female)')
    with col3:
        cp = st.number_input('Chest Pain types')
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.number_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Results'):
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        input_data = [float(x) for x in input_data]  # converting to float because the model was trained on float data and the user inputs are taken as strings
        heart_prediction = heart_model.predict([input_data])  # predicting the input data
        if heart_prediction[0] == 1:  # slicing the prediction to get the result of the prediction and comparing it to 1
            heart_diagnosis = 'The Person has heart disease'
        else:
            heart_diagnosis = 'The Person does not have heart disease'
        st.write(heart_diagnosis)

if selected == 'Parkinson Disease Prediction':
    st.title('Parkinson Disease Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
    with col1:
        jitter_percent = st.number_input('MDVP:Jitter(%)')
    with col2:
        jitter_abs = st.number_input('MDVP:Jitter(Abs)')
    with col3:
        rap = st.number_input('MDVP:RAP')
    with col1:
        ppq = st.number_input('MDVP:PPQ')
    with col2:
        ddp = st.number_input('Jitter:DDP')
    with col3:
        shimmer = st.number_input('MDVP:Shimmer')
    with col1:
        shimmer_db = st.number_input('MDVP:Shimmer(dB)')
    with col2:
        apq3 = st.number_input('Shimmer:APQ3')
    with col3:
        apq5 = st.number_input('Shimmer:APQ5')
    with col1:
        apq = st.number_input('MDVP:APQ')
    with col2:
        dda = st.number_input('Shimmer:DDA')
    with col3:
        nhr = st.number_input('NHR')
    with col1:
        hnr = st.number_input('HNR')
    with col2:
        rpde = st.number_input('RPDE')
    with col3:
        dfa = st.number_input('DFA')
    with col1:
        spread1 = st.number_input('spread1')
    with col2:
        spread2 = st.number_input('spread2')
    with col3:
        d2 = st.number_input('D2')
    with col1:
        ppe = st.number_input('PPE')

    parkinson_diagnosis = ''
    if st.button('Parkinson Disease Test Results'):
        input_data = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
        input_data = [float(x) for x in input_data]  # converting to float because the model was trained on float data and the user inputs are taken as strings
        parkinson_prediction = parkinson_model.predict([input_data])  # predicting the input data
        if parkinson_prediction[0] == 1:  # slicing the prediction to get the result of the prediction and comparing it to 1
            parkinson_diagnosis = 'The Person has Parkinson disease'
        else:
            parkinson_diagnosis = 'The Person does not have Parkinson disease'
        st.write(parkinson_diagnosis)