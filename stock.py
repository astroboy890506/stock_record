import streamlit as st
import pandas as pd

def calculate_realize_gain_loss(row):
    return (row["exit_price"] * row["exit_unit"]) - row["cost"]

def main():
    st.set_page_config(
        page_title="Trading Data App",
        page_icon="💹",
        layout="wide"
    )

    st.title("Trading Data Entry and Analysis")

    # Create or load trading data DataFrame
    if "trading_data" not in st.session_state:
        st.session_state.trading_data = pd.DataFrame(columns=[
            "Year", "Date", "Stock Name",
            "Price Enter", "Enter Unit", "Cost",
            "Exit Date", "Exit Price", "Exit Unit", "Realize Gain/Loss"
        ])

    # Input form for trading data
    with st.form("trading_form"):
        # ... (your input form code)

    # Update DataFrame with new entry
    if st.form_submit_button("Add Trading Data"):
        # ... (your data appending code)

    # Display the trading data in a table
    st.subheader("Trading Data Table")
    st.dataframe(st.session_state.trading_data)  # Removed index=False

if __name__ == "__main__":
    main()
