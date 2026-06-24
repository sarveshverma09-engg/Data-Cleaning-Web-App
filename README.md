# 🧹 Smart Data Cleaning Web App

A Streamlit-based Data Cleaning application that helps users quickly inspect and clean datasets without writing code. The application supports CSV, XLSX, and XLS files and provides dataset analysis, missing value detection, duplicate detection, and downloadable cleaned data.

## 🚀 Features

### 📂 File Upload

* Upload CSV files
* Upload XLSX files
* Upload XLS files

### 📊 Dataset Overview

* Display number of rows and columns
* Preview dataset records
* View column data types

### 🔍 Data Quality Analysis

* Detect missing values in each column
* Count total missing values
* Detect duplicate rows

### 🛠 Data Cleaning

* Remove missing values
* Remove duplicate rows
* Apply cleaning with a single click

### ⬇ Export Cleaned Data

* Download cleaned dataset as CSV

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* OpenPyXL
* XLRD

## 📂 Supported File Formats

| Format | Supported |
| ------ | --------- |
| CSV    | ✅         |
| XLSX   | ✅         |
| XLS    | ✅         |

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/data-cleaning-web-app.git
cd data-cleaning-web-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📋 Features Workflow

1. Upload dataset
2. Analyze dataset structure
3. Check missing values
4. Check duplicate records
5. Apply cleaning operations
6. Download cleaned dataset

## 📦 Requirements

```text
streamlit
pandas
openpyxl
xlrd
```

## 🔮 Future Improvements

* Missing value imputation
* Outlier detection
* Column-wise cleaning options
* Data visualization dashboard
* Automatic data quality reports

## 👨‍💻 Author

**Sarvesh Verma**
B.Tech CSE (AI & ML)

---

⭐ If you found this project useful, consider starring the repository.
