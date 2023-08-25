import streamlit as st
import pandas as pd

def calculate_realize_gain_loss(row):
    return (row["exit_price"] * row["exit_unit"]) - row["cost"]

# Call set_page_config first
st.set_page_config(
    page_title="Trading Data App",
    page_icon="💹",
    layout="wide"
)

def main():
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
        col1, col2, col3 = st.columns(3)

        year = col1.text_input("Year of Trading")
        date = col2.date_input("Date")
        stock_name = col3.text_input("Stock Name")

        price_enter = st.number_input("Price Enter", step=0.01, format="%.2f")
        enter_unit = st.number_input("Enter Unit", step=1, min_value=1)

        exit_date = st.date_input("Exit Date")
        exit_price = st.number_input("Exit Price", step=0.01, format="%.2f")
        exit_unit = st.number_input("Exit Unit", step=1, min_value=1)

        submitted = st.form_submit_button("Add Trading Data")

    # Update DataFrame with new entry
    if submitted:
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

        st.session_state.trading_data = pd.concat([st.session_state.trading_data, pd.DataFrame([new_entry])], ignore_index=True)

    # Display the trading data in a table
    st.subheader("Trading Data Table")

    if len(st.session_state.trading_data) > 0:
        st.dataframe(st.session_state.trading_data, width=800)

if st.button("Edit"):
    max_index_value = len(st.session_state.trading_data) - 1
    selected_index = st.number_input("Enter the index to edit", value=0, min_value=0, max_value=max_index_value)
    if selected_index >= 0 and selected_index < len(st.session_state.trading_data):
        edit_mode = True
        year_edit = st.text_input("Year", st.session_state.trading_data.loc[selected_index, "Year"])
        # ... repeat for other columns ...

        confirm_edit = st.button("Confirm Edit")
        cancel_edit = st.button("Cancel Edit")

        if confirm_edit:
            st.session_state.trading_data.loc[selected_index, "Year"] = year_edit
            # ... repeat for other columns ...
            edit_mode = False

        if cancel_edit:
            edit_mode = False

        if not edit_mode:
            st.success("Edit complete.")

    if st.button("Append"):
        new_entry = {}
        new_entry["Year"] = st.text_input("Year")
        new_entry["Date"] = st.date_input("Date")
        new_entry["Stock Name"] = st.text_input("Stock Name")
        new_entry["Price Enter"] = st.number_input("Price Enter", step=0.01, format="%.2f")
        new_entry["Enter Unit"] = st.number_input("Enter Unit", step=1, min_value=1)
        new_entry["Exit Date"] = st.date_input("Exit Date")
        new_entry["Exit Price"] = st.number_input("Exit Price", step=0.01, format="%.2f")
        new_entry["Exit Unit"] = st.number_input("Exit Unit", step=1, min_value=1)
        new_entry["Cost"] = new_entry["Price Enter"] * new_entry["Enter Unit"]
        new_entry["Realize Gain/Loss"] = (new_entry["Exit Price"] * new_entry["Exit Unit"]) - new_entry["Cost"]
        st.session_state.trading_data = pd.concat([st.session_state.trading_data, pd.DataFrame([new_entry])], ignore_index=True)

    if st.button("Remove"):
        selected_index = st.number_input("Enter the index to remove", value=0, min_value=0, max_value=len(st.session_state.trading_data)-1)
        if selected_index >= 0 and selected_index < len(st.session_state.trading_data):
            st.session_state.trading_data.drop(selected_index, inplace=True)
            st.session_state.trading_data.reset_index(drop=True, inplace=True)    # ... (append and remove operations)

if __name__ == "__main__":
    main()
