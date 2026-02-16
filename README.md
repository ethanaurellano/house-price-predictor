# 🏠 Belgian House Price Predictor (ML Project)

This project is a Machine Learning application that predicts real estate prices in Belgium based on the square footage of a property. 

## 🎯 Project Overview
I built this to demonstrate how **Linear Regression** can be used to find patterns in historical data to make future predictions. It uses a custom dataset of house sizes and prices to "learn" the market value per square meter.

## 🛠️ Tech Stack
* **Python**: The core programming language.
* **Pandas**: Used for data manipulation and reading CSV files.
* **Scikit-Learn**: Used to implement the `LinearRegression` machine learning model.
* **Streamlit**: Used to turn the Python script into an interactive web application.

## 📊 How it Works
1. **Data Ingestion**: The app reads a `prices.csv` file containing historical house data.
2. **Model Training**: The AI uses Scikit-Learn to "fit" a trend line to the data points.
3. **User Input**: Users enter a house size (m²) via the web interface.
4. **Prediction**: The model calculates the estimated price based on the learned trend line.

## 🚀 How to Run Locally
1. Clone this repository.
2. Install the requirements:
   ```bash
   pip install streamlit pandas scikit-learn
3. Run application:
   ```bash
   python -m streamlit run house_app.py
