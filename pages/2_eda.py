import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="EDA",
    layout="wide"
)

df = pd.read_csv("Cars_cleaned.csv")

st.title("Exploratory Data Analysis")
st.write("This page contains visual analysis of the Cars dataset.")
st.divider()

st.header("Dataset Preview")
st.dataframe(df.head()) 

st.divider()

st.header("Top 10 Car Companies")

company = df["Company_Name"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(company.index, company.values)
ax.set_xlabel("Company")
ax.set_ylabel("Number of Cars")
ax.set_title("Top 10 Car Companies")
plt.xticks(rotation=45)

st.pyplot(fig)

st.divider()

st.header("Fuel Type Distribution")

fuel = df["Fuel_Type"].value_counts()

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(
    fuel.values,
    labels=fuel.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.set_title("Fuel Type Distribution")

st.pyplot(fig)

st.divider()

st.header("Transmission Distribution")

trans = df["Transmission"].value_counts()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(trans.index, trans.values)
ax.set_xlabel("Transmission")
ax.set_ylabel("Count")
ax.set_title("Transmission Distribution")

st.pyplot(fig)

st.divider()

st.header("Owner Type Distribution")

owner = df["Owner_Type"].value_counts()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(owner.index, owner.values)
ax.set_xlabel("Owner Type")
ax.set_ylabel("Count")
ax.set_title("Owner Type Distribution")
plt.xticks(rotation=20)

st.pyplot(fig)

st.divider()

st.header("Top 10 Locations")

location = df["Location"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(location.index, location.values)
ax.set_xlabel("Location")
ax.set_ylabel("Number of Cars")
ax.set_title("Cars by Location")
plt.xticks(rotation=45)

st.pyplot(fig)

st.divider()

st.header("Year vs Price")

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["Year"], df["Price"])
ax.set_xlabel("Year")
ax.set_ylabel("Price")
ax.set_title("Year vs Price")

st.pyplot(fig)

st.divider()

st.header("Price by Fuel Type")

fuel_groups = []
label = []

for fuel_type in df["Fuel_Type"].dropna().unique():
    fuel_groups.append(df[df["Fuel_Type"] == fuel_type]["Price"])
    label.append(fuel_type)

fig, ax = plt.subplots(figsize=(7, 5))
ax.boxplot(fuel_groups, label=label)
ax.set_xlabel("Fuel Type")
ax.set_ylabel("Price")
ax.set_title("Price by Fuel Type")

st.pyplot(fig)

st.divider()

st.header("Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()

fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(corr, cmap="coolwarm")

ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=90)
ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)

plt.colorbar(cax)

st.pyplot(fig)

st.divider()

st.header("Average Price by Fuel Type")

avg_price = df.groupby("Fuel_Type")["Price"].mean()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(avg_price.index, avg_price.values)
ax.set_xlabel("Fuel Type")
ax.set_ylabel("Average Price")
ax.set_title("Average Price by Fuel Type")

st.pyplot(fig)

st.divider()

st.header("Average Mileage by Fuel Type")

avg_mileage = df.groupby("Fuel_Type")["Mileage_value"].mean()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(avg_mileage.index, avg_mileage.values)
ax.set_xlabel("Fuel Type")
ax.set_ylabel("Average Mileage")
ax.set_title("Average Mileage by Fuel Type")

st.pyplot(fig)

st.divider()

st.header("Average Engine Size by Fuel Type")

avg_engine = df.groupby("Fuel_Type")["Engine_value"].mean()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(avg_engine.index, avg_engine.values)
ax.set_xlabel("Fuel Type")
ax.set_ylabel("Engine Size")
ax.set_title("Average Engine Size")

st.pyplot(fig)

st.divider()

st.header("Average Power by Fuel Type")

avg_power = df.groupby("Fuel_Type")["Power_value"].mean()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(avg_power.index, avg_power.values)
ax.set_xlabel("Fuel Type")
ax.set_ylabel("Power")
ax.set_title("Average Power")

st.pyplot(fig)

st.divider()

st.header("Dataset Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])
    st.metric("Columns", df.shape[1])

with col2:
    st.metric("Missing Values", df.isnull().sum().sum())
    st.metric("Duplicate Records", df.duplicated().sum())

st.divider()

st.success("Exploratory Data Analysis Completed Successfully.")