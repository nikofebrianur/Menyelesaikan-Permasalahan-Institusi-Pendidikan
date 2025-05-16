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
age = st.slider("Usia saat mendaftar", 16, 40, 20)
tuition_paid = st.selectbox("Uang kuliah sudah dibayar?", ["Ya", "Tidak"])
scholarship = st.selectbox("Penerima beasiswa?", ["Ya", "Tidak"])
admission_grade = st.slider("Nilai saat masuk (0-200)", 0, 200, 120)
curricular_enrolled = st.slider("Jumlah matkul diambil sem 1", 0, 15, 5)
curricular_approved = st.slider("Jumlah matkul lulus sem 1", 0, 15, 4)

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
