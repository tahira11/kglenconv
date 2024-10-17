import streamlit as st

st.title("Simple Unit Converter")

conversion_types = {"Weight": {"Kg to Grams": 1000, "Grams to Kg": 1/1000}, 
                    "Time": {"Hours to Seconds": 3600, "Seconds to Hours": 1/3600},
                    "Distance": {"Meters to Km": 1/1000, "Km to Meters": 1000}}

conversion_choice = st.selectbox("Select Conversion Type", ["Weight", "Time", "Distance"])
unit = st.radio("Convert:", list(conversion_types[conversion_choice].keys()))
amount = st.number_input("Enter Value", min_value=0.01, step=0.01)

try:
    converted_amount = amount * conversion_types[conversion_choice][unit]
    st.success(f"{amount} is equivalent to {converted_amount:.2f}")
except Exception as e:
    st.error(f"An error occurred: {e}")
