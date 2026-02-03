# 🌐 TOPSIS Decision Making Web App

A web-based decision support tool built using **Python** and **Streamlit** that applies the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** algorithm for **Multi-Criteria Decision Making (MCDM)**.

This app uses the published PyPI package  
**Topsis-Pulkit-102303800** for computing the ranking.

---

## 🚀 Features

- Upload **CSV** or **Excel (.xlsx)** decision datasets  
- Enter **weights** for each criterion  
- Enter **impacts** (+ benefit / - cost)  
- Computes **TOPSIS Score** and **Rank**  
- Download result file  
- Automatically emails result file to user  
- Clean web interface (no coding required)

---

## 🧮 About TOPSIS

TOPSIS ranks alternatives based on distance from:

- Ideal Best Solution  
- Ideal Worst Solution  

It is widely used in:
- Engineering decision analysis  
- Business analytics  
- Optimization problems  

---

##Web app interface

<img width="852" height="705" alt="image" src="https://github.com/user-attachments/assets/ed30f927-c0b3-41f1-9425-4720ef6472fc" />


---

## 📥 Installation (Local Run)

```bash
pip install -r requirements.txt
streamlit run app.py
