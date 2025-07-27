# Smart Firewall Rule Recommendation System 🔥🛡️

This project uses machine learning to analyze network log data and automatically recommend firewall rules that can help secure your system by filtering potentially malicious traffic.

---

## 📌 Features
- Parses and processes network log files (CSV format)
- Trains a machine learning model to detect patterns in network activity
- Recommends firewall rules based on new input logs
- Interactive web interface using Streamlit
- Includes feedback mechanism to improve rule accuracy over time

---

## 🧠 Technologies Used
- Python 3.x
- pandas, scikit-learn, joblib
- Streamlit (for UI)
- Git for version control

---

## 📁 Project Structure
```
├── data/               # Sample network logs
├── outputs/            # Generated models or rules
├── src/                # Core Python logic
├── test_cases/         # Placeholder for testing
├── ui/                 # Streamlit app
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/smart-firewall-rule-system.git
cd smart-firewall-rule-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run ui/app.py
```

### 4. Upload Log File
- Use the `network_logs.csv` file in `data/` as a test input.
- The app will suggest firewall rules based on the log content.

---

## 🎥 Walkthrough Video
> [Watch on YouTube](https://youtube.com/YOUR_VIDEO_LINK)  
> *(Max 10 min, shows code and app demo)*

---

## 💬 Feedback & Improvements
You can retrain the model using `train_model.py` and submit feedback via the UI, helping improve rule accuracy over time.

---

## 🧪 Test Cases
You can add test logs to the `test_cases/` folder for batch evaluation of rule quality.

---

## 📜 License
MIT License - feel free to use and modify with credit.
