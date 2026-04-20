import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------
# Cloud Pricing
# -------------------------------
pricing = {
    "AWS": {"storage": 2, "compute": 5, "data": 1},
    "Azure": {"storage": 2.2, "compute": 5.5, "data": 1.2},
    "GCP": {"storage": 2.1, "compute": 4.8, "data": 1}
}

# -------------------------------
# UI
# -------------------------------
st.title("☁️ Cloud Cost Calculator")

storage = st.number_input("Enter Storage (GB)", min_value=0.0)
compute = st.number_input("Enter Compute Hours", min_value=0.0)
data_transfer = st.number_input("Enter Data Transfer (GB)", min_value=0.0)

# -------------------------------
# Calculation Function
# -------------------------------
def calculate_cost(storage, compute, data_transfer):
    results = []

    for provider in pricing:
        storage_cost = storage * pricing[provider]["storage"]
        compute_cost = compute * pricing[provider]["compute"]
        data_cost = data_transfer * pricing[provider]["data"]

        total = storage_cost + compute_cost + data_cost

        results.append([provider, storage_cost, compute_cost, data_cost, total])

    return pd.DataFrame(results, columns=[
        "Provider", "Storage Cost", "Compute Cost", "Data Transfer Cost", "Total Cost"
    ])

# -------------------------------
# Button Action
# -------------------------------
if st.button("Calculate Cost"):
    df = calculate_cost(storage, compute, data_transfer)

    st.subheader("📊 Results")
    st.dataframe(df)

    # Graph
    fig, ax = plt.subplots()
    ax.bar(df["Provider"], df["Total Cost"])
    ax.set_title("Cloud Cost Comparison")
    ax.set_xlabel("Provider")
    ax.set_ylabel("Cost (₹)")

    st.pyplot(fig)

    # Download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "cloud_cost.csv", "text/csv")