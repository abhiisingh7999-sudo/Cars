import streamlit as st

st.set_page_config(
    page_title="Conclusion",
    layout="wide"
)

st.title("Project Conclusion")

st.write(
    "This page summarizes the main findings obtained from the Exploratory Data Analysis of the Used Cars dataset."
)

st.divider()

st.header("Key Findings")

st.write("""
- The dataset contains valuable information about used cars, including price, fuel type, transmission, mileage, engine size, and ownership details.
- Car price is influenced by factors such as manufacturing year, engine power, mileage, and brand.
- Petrol and Diesel cars make up the majority of the dataset.
- Manual transmission vehicles are more common than automatic vehicles.
- Some car companies have significantly more listings than others.
- Most vehicles are owned by first or second owners.
- Newer cars generally have higher selling prices than older cars.
""")

st.divider()

st.header("Business Insights")

st.write("""
- Buyers can compare prices based on brand, fuel type, and vehicle age.
- Sellers can estimate a reasonable selling price using similar vehicles in the dataset.
- Dealers can identify the most popular brands and fuel types in the market.
- The analysis helps understand market trends and customer preferences.
""")

st.divider()

st.header("Project Summary")

st.write("""
This project demonstrates how Python, Pandas, Plotly, and Streamlit can be used to analyze and visualize real-world data. Interactive charts make it easier to discover trends, compare categories, and support data-driven decision making.
""")

st.divider()

st.header("Technologies Used")

st.write("""
- Python
- Pandas
- Plotly Express
- Streamlit
""")

st.divider()

st.success("Exploratory Data Analysis Completed Successfully.")