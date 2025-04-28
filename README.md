# Calorie Burn Prediction API dengan FastAPI

Sebuah mini-proyek berbasis FastAPI yang dapat memprediksi jumlah kalori yang terbakar selama latihan, berdasarkan input karakteristik latihan dan individu.

Struktur File
calorie_burn_api/
├── main.py             # Endpoint API utama
├── model.pkl           # File model Machine Learning yang telah dilatih
├── scaler.pkl          # File scaler untuk normalisasi fitur input
└── requirements.txt    # Daftar dependency yang dibutuhkan

Fitur API
Prediksi jumlah kalori yang terbakar selama latihan.
Menerima input melalui metode POST.
Hasil prediksi dalam bentuk angka (kalori).
Ringan, cepat, dan siap diintegrasikan ke aplikasi lain.

Cara Menjalankan
1. Clone Repositori (jika ada)
Jika Anda telah membuat repositori Git untuk proyek ini, clone repositori tersebut.
2. Buat Virtual Environment
python -m venv .env
   source .env/bin/activate  # Command Prompt: .env\Scripts\activate
3. Install Dependensi
4. Jalankan API
uvicorn main:app --reload
5. Akses Swagger UI Buka browser ke: [http://127.0.0.1:8000/docs]
Contoh JSON Input
{
  "Age": 30,
  "Gender": 1,  // 1: Male, 0: Female
  "Weight_kg": 70.5,
  "Height_m": 1.75,
  "Max_BPM": 180,
  "Avg_BPM": 145.2,
  "Session_Duration_hours": 1.2,
  "Workout_Type_Cardio": 1,  // 1: Ya, 0: Tidak
  "Workout_Type_Strength": 0, // 1: Ya, 0: Tidak
  "Workout_Type_HIIT": 0,    // 1: Ya, 0: Tidak
  "Workout_Type_Yoga": 0,     // 1: Ya, 0: Tidak
  "Fat_Percentage": 22.5,
  "Workout_Frequency_days_week": 3,
  "Experience_Level": 2
}
Gunakan kode dengan hati-hati
✅ Contoh Output

{
  "calories_burned": 650.25 
}
Proyek ini dapat dijadikan dasar pengembangan API prediksi sederhana lainnya.
