# --- app.py ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Step 1: Title
st.title("📈 Retail Sales Dashboard (Stock-Style Data)")

# Step 2: Create DataFrame (your stock-like data)
Data = {
    "Customer ID": ["C01","C02","C03","C04","C05","C06","C07"],
    "Date": ["1-11-2025","2-11-2025","3-11-2025","4-11-2025","5-11-2025","6-11-2025","7-11-2025"],
    "Stock Price": [100,111,101,103,104,118,106],
    "CP": [95, 98, 99, 100, 102, 104, 105],
    "SP": [100, 102, 101, 104, 107, 106, 108]
}

df = pd.DataFrame(Data)

# Step 3: Calculate Profit/Loss and Daily Return
df["Profit/Loss"] = df["SP"] - df["CP"]
df["Daily_Return (%)"] = df["SP"].pct_change() * 100

# Step 4: Display DataFrame
st.subheader("📊 Stock Market Style Retail Data")
st.dataframe(df)

# Step 5: Show Summary
total_profit = df["Profit/Loss"].sum()
max_profit = df["Profit/Loss"].max()
min_profit = df["Profit/Loss"].min()
avg_profit = df["Profit/Loss"].mean()

st.write("### 💰 Summary")
st.write(f"**Total Profit:** ₹{total_profit}")
st.write(f"**Highest Profit:** ₹{max_profit}")
st.write(f"**Lowest Profit:** ₹{min_profit}")
st.write(f"**Average Profit:** ₹{round(avg_profit, 2)}")

# Step 6: Plot Profit/Loss Over Time
st.write("### 📈 Profit/Loss Over Time")
st.line_chart(df.set_index("Date")["Profit/Loss"])

# Step 7: Save data locally
if st.button("💾 Save Data to CSV"):
    df.to_csv("retail_stock_data.csv", index=False)
    st.success("✅ Data saved to 'retail_stock_data.csv'")

# Step 8: Option to Add New Entry
st.write("### ➕ Add New Record")

cust_id = st.text_input("Enter Customer ID")
date = st.text_input("Enter Date (e.g., 8-11-2025)")
cp = st.number_input("Enter Cost Price (₹)", min_value=1, step=1)
sp = st.number_input("Enter Selling Price (₹)", min_value=1, step=1)
stock_price = st.number_input("Enter Stock Price (₹)", min_value=1, step=1)

if st.button("Add Record"):
    new_record = pd.DataFrame([{
        "Customer ID": cust_id,
        "Date": date,
        "Stock Price": stock_price,
        "CP": cp,
        "SP": sp,
        "Profit/Loss": sp - cp,
        "Daily_Return (%)": np.nan  # can be calculated later
    }])
    df = pd.concat([df, new_record], ignore_index=True)
    st.success("✅ New record added successfully!")
    st.dataframe(df)
