import streamlit as st
import pickle
import pandas as pd

# Buat Form Isian
def main():

    st.set_page_config(page_title='Aplikasi Predisksi Stroke')

    # Heading
    st.sidebar.title ('Aplikasi Predisksi Stroke')

    # Input
    gender = st.sidebar.selectbox('Jenis Kelamin', ['Male', 'Female'])
    if gender == "Male":
        gender =1
    else:
        gender =0

    age = st.sidebar.number_input('Usia', min_value=1, max_value=100, step=1)

    hypertension = st.sidebar.selectbox('Hypertension', ['No', 'Yes'])
    if hypertension == "Yes":
        hypertension=1
    else:
        hypertension=0
    
    heart_disease = st.sidebar.selectbox('Heart Disease', ['No', 'Yes'])
    if heart_disease == "Yes":
        heart_disease=1
    else:
        heart_disease=0

    ever_married = st.sidebar.selectbox('Ever Married', ['No', 'Yes'])
    if ever_married == "Yes":
        ever_married=1
    else:
        ever_married=0

    work_type = st.sidebar.selectbox('Tipe Pekerjaan', ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    if work_type == "Private":
        work_type=2
    elif work_type == "Self-employed":
         work_type=3
    elif work_type == "Govt_job":
         work_type=0
    elif work_type == "children":
         work_type=4
    elif work_type == "Never_worked":
         work_type=1

    Residence_type = st.sidebar.selectbox('Daerah Rumah', ['Urban', 'Rural'])
    if Residence_type == "Urban":
        Residence_type=0
    else:
        Residence_type=1

    avg_glucose_level = st.sidebar.number_input('Avg Glucose Level', min_value=1.0, max_value=300.0, step=1.0)
    bmi = st.sidebar.number_input('BMI', min_value=10.0, max_value=60.0, step=1.0)

    smoking_status = st.sidebar.selectbox('Smoking Status', ['Unknown', 'Never Smoked', 'Formerly Smoked', 'Smokes'])
    if smoking_status == "Unknown":
        smoking_status=4
    elif smoking_status == "Never Smoked":
         smoking_status=2
    elif smoking_status == "Formerly Smoked":
         smoking_status=1
    elif smoking_status == "Smokes":
         smoking_status=3

    # Create a Dictionary with input data
    input_data = {
        'gender':[gender],
        'age':[age],
        'hypertension':[hypertension],
        'heart_disease':[heart_disease],
        'ever_married':[ever_married],
        'work_type':[work_type],
        'Residence_type':[ever_married],
        'avg_glucose_level':[avg_glucose_level],
        'bmi':[bmi],
        'smoking_status':[smoking_status]
    }

    # Create a Data Frame
    input_df = pd.DataFrame(input_data)
    
    # Train Model
    model = pickle.load(open('stroke2.pkl','rb'))

    # Make a Prediction
    st.title('Prediksi Penyakit Stroke')
    st.write('Selamat Datang di Website Kami')

    # Display the Prediction
    st.title('Hasil Klasifikasi Adalah')
    if st.button('Predict'):
        # Make a Prediction
        prediction = prediction = model.predict(input_df)[0]

        #Display the Prediction
        if prediction == 1:
            st.write('Ada Resiko Terjangkit Stroke')
        else:
            st.write('Tidak Ada Resiko Terjangkit Stroke')


if __name__ =='__main__':
    main()
