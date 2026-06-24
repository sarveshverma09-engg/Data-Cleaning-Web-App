import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Cleaning Web App",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Smart Data Cleaning Web App")
st.write("Upload CSV, XLSX or XLS files.")

uploaded_file = st.file_uploader(
    "Upload File",
    type=["csv", "xlsx", "xls"]
)

# ---------- FILE READING FUNCTION ----------

def load_file(file):

    file_name = file.name.lower()

    try:
        if file_name.endswith(".csv"):
            return pd.read_csv(file)

        elif file_name.endswith(".xlsx"):
            return pd.read_excel(file, engine="openpyxl")

        elif file_name.endswith(".xls"):
            return pd.read_excel(file, engine="xlrd")

        else:
            raise ValueError("Unsupported File Format")

    except Exception as e:
        raise e


# ---------- MAIN APP ----------

if uploaded_file is not None:

    try:

        st.info(f"Uploaded File: {uploaded_file.name}")

        df = load_file(uploaded_file)

        st.success("File Loaded Successfully ✅")

        # Dataset Overview
        st.header("📊 Dataset Overview")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        st.subheader("Preview")

        st.dataframe(df.head())

        # Data Types
        st.subheader("Column Data Types")

        dtype_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(dtype_df)

        # Missing Values
        st.header("🔍 Missing Values")

        missing = df.isnull().sum()

        missing_df = pd.DataFrame({
            "Column": missing.index,
            "Missing Values": missing.values
        })

        st.dataframe(missing_df)

        st.metric(
            "Total Missing Values",
            int(missing.sum())
        )

        # Duplicate Rows
        st.header("📌 Duplicate Rows")

        duplicates = df.duplicated().sum()

        st.metric(
            "Duplicate Rows",
            int(duplicates)
        )

        # Cleaning Section
        st.header("🛠 Cleaning Options")

        cleaned_df = df.copy()

        remove_missing = st.checkbox(
            "Remove Missing Values"
        )

        remove_duplicates = st.checkbox(
            "Remove Duplicate Rows"
        )

        if st.button("Apply Cleaning"):

            if remove_missing:
                cleaned_df = cleaned_df.dropna()

            if remove_duplicates:
                cleaned_df = cleaned_df.drop_duplicates()

            st.success("Cleaning Applied Successfully ✅")

            st.subheader("Cleaned Dataset")

            st.dataframe(cleaned_df.head())

            st.write(
                f"Shape After Cleaning: {cleaned_df.shape}"
            )

            # Download CSV
            csv = cleaned_df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="⬇ Download Cleaned CSV",
                data=csv,
                file_name="cleaned_data.csv",
                mime="text/csv"
            )

    except Exception as e:

        st.error("❌ Unable to read file.")

        st.error(str(e))

        st.info("""
Possible Reasons:

1. File is corrupted.
2. Wrong extension (.xlsx file renamed as .xls).
3. Excel file is password protected.
4. Unsupported format.
5. CSV encoding issue.
""")