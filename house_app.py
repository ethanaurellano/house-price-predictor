import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. The Title
st.title("🏠 Belgian House Price Predictor")
st.write("This AI learns the relationship between house size and price.")

# 2. Load the data
# We use 'Pandas' to read our CSV file
df = pd.read_csv('prices.csv')

# 3. Train the Model (The "Teaching" part)
# We tell the AI: "Look at Size (X) and learn to predict Price (y)"
X = df[['Size']] 
y = df['Price']

model = LinearRegression()
model.fit(X, y) # This 'fit' command is where the AI learns the pattern

# 4. User Interface
st.divider()
size_input = st.number_input("Enter the house size in m²:", min_value=10, value=100)

if size_input:
    # 5. Prediction
    # We ask the AI to guess the price for the user's input
    prediction = model.predict([[size_input]])
    final_price = prediction[0]
    
    st.subheader(f"Estimated Market Value: €{final_price:,.2f}")
    st.info("Logic: The AI found that every 1m² adds roughly €3,000 to the price.")