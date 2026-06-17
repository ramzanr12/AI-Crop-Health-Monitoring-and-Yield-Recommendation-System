## 🌱 AI Crop Health Monitoring and Yield Recommendation System

An intelligent agricultural web application that leverages Computer Vision 
and Machine Learning to assist farmers and agronomists in making data-driven 
decisions for better crop yield and health management.

### 🔍 Features

- **Crop Disease Detection** — Real-time plant disease identification from 
  leaf images using a fine-tuned YOLOv8 model
- **Crop Recommendation** — Suggests the best crop to grow based on soil 
  nutrients (N, P, K), temperature, humidity, and rainfall using ensemble ML models
- **Fertilizer Recommendation** — Recommends the optimal fertilizer type 
  based on soil and crop parameters
- **Yield Prediction** — Estimates expected crop yield using historical 
  agricultural data
- **AI Chatbot** — Conversational assistant for farming-related queries

### 🛠️ Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| ML Models | YOLOv8 (Ultralytics), Random Forest, KNN, SVM, Decision Tree, MLP |
| Data | CSV datasets, Excel soil data |
| Libraries | PyTorch, Scikit-learn, Joblib, OpenCV, Pandas |

### 📁 Project Structure

\`\`\`
├── app.py                  # Flask backend
├── models/                 # Pre-trained ML models (.pkl)
├── templates/              # HTML pages
├── static/                 # Images and assets
├── data/                   # Crop and soil datasets
└── *.ipynb                 # Model training notebooks
\`\`\`

### 🚀 Getting Started

\`\`\`bash
# Clone the repo
git clone https://github.com/ramzanr12/AI-Crop-Health-Monitoring-and-Yield-Recommendation-System.git

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows

# Install dependencies
pip install flask torch ultralytics joblib scikit-learn pandas opencv-python pillow openpyxl

# Run the app
python app.py
\`\`\`

Open http://localhost:5000 in your browser.
