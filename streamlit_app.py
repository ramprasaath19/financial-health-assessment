# streamlit_app.py
import streamlit as st
import requests

# Define the Streamlit app
def main():
    st.title("Financial Risk Assessment Demo")

    # User input section
    st.header("Enter Financial Data:")
    income = st.number_input("Income", min_value=0.0)
    expenses = st.number_input("Expenses", min_value=0.0)

    if st.button("Assess Risk"):
        # Make a request to the FastAPI endpoint
        response = assess_risk(income, expenses)
        print(response)
        # Display the risk assessment result
        st.subheader("Risk Assessment Result:")
        st.write(f"Risk Level: {response['risk_level']}")

# Function to make a POST request to the FastAPI endpoint
def assess_risk(income, expenses):
    url = "http://localhost:8000/assess_risk/"  
    data = {"income": income, "expenses": expenses}

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Error occurred while assessing risk.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
