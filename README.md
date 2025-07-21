# FraudSheild : Credit Card Fraud Detection System

A machine learning-based project to detect fraudulent credit card transactions. The model is trained on a highly imbalanced dataset and deployed using Flask for real-time web-based predictions.

---

## 📌 Project Highlights

- Built a classification model to detect fraud using anonymized credit card transaction data.
- Compared **six different machine learning algorithms** and found **Random Forest** performed best with an accuracy of **99.95%**.
- The system is deployed using **Flask** with a simple and interactive **HTML/CSS/JS frontend**.
- Real-time predictions are made based on user input, making the system practical and testable.
<img width="629" height="169" alt="image" src="https://github.com/user-attachments/assets/b206f233-962e-45f3-a514-75438a83b4f7" />


## 🧠 Machine Learning & Python Details

### 🔶 Dataset:
- Source: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Contains 284,807 transactions with only 492 fraud cases (highly imbalanced)
- Features: V1–V28 (PCA transformed), Amount, Time
- Target: `Class` (0 = Not Fraud, 1 = Fraud)
<img width="1133" height="394" alt="image" src="https://github.com/user-attachments/assets/50d23ac4-c5d4-4b3c-85be-c5c3485d35e3" />


### 🔶 Algorithms Compared:
- Logistic Regression
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Decision Tree
- Naive Bayes
- **Random Forest** (Best Performance)

<img width="734" height="182" alt="image" src="https://github.com/user-attachments/assets/935642ab-1b71-4d7a-bf08-7914b3b39825" />

### 🔶 Model Evaluation:
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- Special focus on **Recall for Class 1 (fraud)** to minimize false negatives

### 🔶 Preprocessing:
- Checked for null values: `df.isnull().sum()`
- Scaled features using `StandardScaler` if needed
- Handled class imbalance using techniques like **under-sampling** (optional)

### 🔶 Model Saving:
```python
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)



