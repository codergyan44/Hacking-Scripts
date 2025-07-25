import streamlit as st
import requests
import pandas as pd

def Bank_Data_Finder(IFSC_Code):
    """Fetches and returns detailed information about a bank branch using its IFSC code.
    Parameters:
        - IFSC_Code (str): The IFSC code of the bank branch for which information is being retrieved.
    Returns:
        - list: A list containing detailed information about the bank branch, which includes the bank name, branch, address, city, state, IFSC code, contact information, and the availability of services like UPI, RTGS, NEFT, and IMPS.
    Processing Logic:
        - Constructs the URL by appending the IFSC code to a predefined base URL to fetch bank details via an API request.
        - Retrieves data in JSON format and extracts specific details about the bank branch.
        - Checks the availability of various banking services and formats how this information is appended to the results.
        - Handles exceptions gracefully, printing an error message if the request fails."""
    try:
        #fetching the data
        url = 'https://ifsc.razorpay.com/' + 'SBIN0000813'
        bank_info = requests.get(url).json()
        all_details = []
        bank_name = bank_info['BANK']
        branch = bank_info['BRANCH']
        address = bank_info['ADDRESS']
        city = bank_info['CITY']
        state = bank_info['STATE']
        ifsc = bank_info['IFSC']
        contact = bank_info['CONTACT']
        upi = 'UPI: ' + 'Available' if bank_info['UPI'] == True else 'Not Available'
        rtgs = 'RTGS: ' + 'Available' if bank_info['RTGS'] == True else 'Not Available'
        neft = "NEFT: " + 'Available' if bank_info['NEFT'] == True else 'Not Available'
        imps = 'IMPS: ' + 'Available' if bank_info['IMPS'] == True else 'Not Available'
         #appending all the details
        all_details.append(bank_name)
        all_details.append(branch)
        all_details.append(address)
        all_details.append(city)
        all_details.append(state)
        all_details.append(ifsc)
        all_details.append(contact)
        all_details.append(upi)
        all_details.append(rtgs)
        all_details.append(neft)
        all_details.append(imps)
        return all_details
    except Exception as e:
        print(e)

def run():
 #function for streamlit
    """This function serves as a Streamlit interface to find and display bank data using an IFSC code.
    Parameters:
        - None
    Returns:
        - None
    Processing Logic:
        - Retrieves bank information using an IFSC code entered by the user.
        - Displays the bank data in a table if the IFSC code is valid.
        - Shows a warning message if the IFSC code is invalid."""
    st.title("Bank Data Finder")

    ## IFSC
    ifsc = st.text_input('Enter your Bank IFSC Code Eg.KARB0000001')
    if st.button("Search"):
        bank_data = Bank_Data_Finder(ifsc)
        data = pd.DataFrame(bank_data)
        if bank_data:
            index_name = ['Bank Name','Branch','Address','City','State','IFSC','Contact','UPI','RTGS','NEFT','IMPS']
            df = pd.DataFrame({'Info': bank_data},index = index_name)
            st.dataframe(df)
        else:
            st.warning("Check your IFSC code!!!")
run()

### Sample  IFSC codes
# UTIB0003655
# SBIN0000813
# UBIN0531324