import streamlit as st
import pickle
import numpy as np

# Load model dan label encoder
with open('student_dropout_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

st.title("🎓 Prediksi Status Mahasiswa - Jaya Jaya Institut")

st.write("Masukkan informasi siswa untuk memprediksi apakah mereka akan lulus, dropout, atau masih aktif.")

# Contoh inputan fitur penting (ganti sesuai fitur X yang kamu pakai)
age = st.number_input("Usia saat mendaftar", min_value=16, max_value=40, value=20)
admission_grade = st.number_input("Nilai saat masuk (0-200)", min_value=0, max_value=200, value=120)
curricular_enrolled = st.number_input("Jumlah matkul diambil sem 1", min_value=0, max_value=15, value=5)
curricular_approved = st.number_input("Jumlah matkul lulus sem 1", min_value=0, max_value=15, value=4)

# Ubah input ke format model
X_input = np.array([[
    age,
    1 if tuition_paid == "Ya" else 0,
    1 if scholarship == "Ya" else 0,
    admission_grade,
    curricular_enrolled,
    curricular_approved
]])

# Predict
if st.button("Prediksi"):
    # Susun input dalam urutan dan format yang sesuai
    X_input = np.array([[
        age,
        1 if tuition_paid == "Ya" else 0,
        1 if scholarship == "Ya" else 0,
        admission_grade,
        curricular_enrolled,
        curricular_approved
    ]])

    # (Opsional) Scaling di sini kalau model kamu pakai scaler

    prediction = model.predict(X_input)[0]
    label = le.inverse_transform([prediction])[0]
    st.success(f"✅ Prediksi: **{label}**")
