import streamlit as st
import pandas as pd

def calculate_realize_gain_loss(row):
    return (row["exit_price"] * row["exit_unit"]) - row["cost"]

def main():
    st.set_page_config(
        page_title="Trading Data App",
        page_icon="??",
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
        col1, col2, col3 = st.beta_columns(3)

        year = col1.text_input("Year of Trading")
        date = col2.date_input("Date")
        stock_name = col3.text_input("Stock Name")

        price_enter = st.number_input("Price Enter", step=0.01, format="%.2f")
        enter_unit = st.number_input("Enter Unit", step=1, min_value=1)

        exit_date = st.date_input("Exit Date")
        exit_price = st.number_input("Exit Price", step=0.01, format="%.2f")
        exit_unit = st.number_input("Exit Unit", step=1, min_value=1)

        st.form_submit_button("Add Trading Data")

    # Update DataFrame with new entry
    if st.session_state.trading_form.submitted:
        cost = price_enter * enter_unit
        realize_gain_loss = (exit_price * exit_unit) - cost

        new_entry = {
            "Year": year,
            "Date": date,
            "Stock Name": stock_name,
            "Price Enter": price_enter,
            "Enter Unit": enter_unit,
            "Cost": cost,
            "Exit Date": exit_date,
            "Exit Price": exit_price,
            "Exit Unit": exit_unit,
            "Realize Gain/Loss": realize_gain_loss
        }

        st.session_state.trading_data = st.session_state.trading_data.append(new_entry, ignore_index=True)

    # Display the trading data in a table
    st.subheader("Trading Data Table")
    st.dataframe(st.session_state.trading_data, index=False)

if __name__ == "__main__":
    main()
