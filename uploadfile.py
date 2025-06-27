import pandas as pd
import streamlit as st  
import matplotlib.pyplot as plt

st.title("# CSV File Upload and Analysis")

def upload_file():
    st.title('Upload CSV File')
    upload_file = st.file_uploader("Choose a CSV file", type="csv")
    if upload_file is not None:
        df = pd.read_csv(upload_file)
        st.write("Data Preview:")
        st.dataframe(df.head())
        chartcontainer = st.container()  # Create a container for the pie chart
        with chartcontainer:
            with st.expander("Generate Pie Chart for 'Profile Name'"):
                pf_name_pie_chart(df)
        sum_container = st.container()  # Create a container for the summary
        with sum_container:
            with st.expander("Data Summary"):
                st.write(df.describe())
        dtypes_container = st.container()  # Create a container for data types
        with dtypes_container:
            with st.expander("Data Types"):
                st.write(df.dtypes)
        st.write("Missing Values:")
        #st.write(df.isnull().sum())
        st.write("Data Shape:")
        #st.write(df.shape)
        st.write("Column Names:")
        #st.write(df.columns.tolist())

        
def pf_name_pie_chart(df):
    if 'Profile Name' in df.columns:
        profile_counts = df['Profile Name'].value_counts()
        plt.figure(figsize=(10, 6))
        plt.pie(profile_counts, labels=profile_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Profile Name Distribution')
        st.pyplot(plt)
    else:
        st.warning("Column 'Profile Name' not found in the uploaded CSV file.")


if __name__ == "__main__":
    upload_file()
    
    
#:some ideas for improvement:
# 1. Add functions and buttons for things such as Data Types, Missing Values, Data Shape, and Column Names to be displayed in separate sections.
# 2. Use the `st.cache` decorator to cache the data loading function for better performance on repeated uploads.
# 3. I dont want all the information to be displayed at once, so i would like to use `st.expander` to organize the output sections.
# 4. Add error handling for file reading to manage cases where the CSV might be malformed
# 5. Include options for users to select specific columns for analysis or visualization.




# This code allows users to upload a CSV file and displays various information about the data.
# It includes a preview of the data, summary statistics, data types, missing values, shape of the data, and column names.
# The `upload_file` function is called when the button is clicked, and it uses Streamlit to create a user interface for file uploading and data display.
# The code is structured to be run as a standalone script, and the `if __name__ == "__main__":` block ensures that the `upload_file` function is executed when the script is run directly.
# The code uses the Streamlit library for creating web applications and the Pandas library for data manipulation.
# The `matplotlib.pyplot` import is included but not used in this snippet, so it can be removed if not needed for plotting purposes.
# The code is designed to be user-friendly and provides a simple way to analyze CSV files interactively.
# The `st.file_uploader` function allows users to select a CSV file from their local system, and the uploaded file is processed using Pandas.
# The various data insights are displayed using Streamlit's `st.write` and `st.dataframe` functions, making it easy for users to understand the structure and content of the uploaded data.
# Overall, this code serves as a basic template for uploading and analyzing CSV files in a Streamlit application.