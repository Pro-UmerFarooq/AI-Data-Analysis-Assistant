import streamlit as st
import pandas as pd

from analysis import *
from visualization import *
from gemini_helper import *
from qa_engine import *
from utils import *
from gemini_helper import ask_gemini
# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="AI Data Analysis Assistant",
    page_icon="📊",
    layout="wide"
)
# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("📊 AI Data Analysis Assistant")

st.markdown("""
Analyze any CSV dataset using Python and AI.

### Features

- 📂 Upload any CSV
- 📊 Automatic Analysis
- 📈 Data Visualization
- 🤖 AI Insights
- ❓ Ask Questions
""")

st.divider()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("📂 Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Choose a CSV File",
    type=["csv"]
)

# -------------------------------------------------
# NO FILE
# -------------------------------------------------

if uploaded_file is None:

    st.info("👈 Upload a CSV file from the sidebar.")

    st.stop()

# -------------------------------------------------
# LOAD DATASET
# -------------------------------------------------

try:

    df = load_csv(uploaded_file)

    if not validate_dataframe(df):
        st.error("Invalid Dataset")
        st.stop()

    st.success("✅ Dataset Loaded Successfully!")

except Exception as e:

    st.error(f"Error loading CSV: {e}")
    st.stop()

# -------------------------------------------------
# DATASET PREVIEW
# -------------------------------------------------

st.header("📑 Dataset Preview")

tab1, tab2 = st.tabs(["First 5 Rows", "Last 5 Rows"])

with tab1:

    st.dataframe(df.head())

with tab2:

    st.dataframe(df.tail())

st.divider()

# -------------------------------------------------
# DATASET SHAPE
# -------------------------------------------------

st.header("📌 Dataset Shape")

col1, col2 = st.columns(2)

with col1:

    st.metric("Rows", df.shape[0])

with col2:

    st.metric("Columns", df.shape[1])

st.divider()
# -------------------------------------------------
# COLUMN NAMES
# -------------------------------------------------

st.header("📋 Column Names")

st.write(df.columns.tolist())

st.divider()

# -------------------------------------------------
# DATA TYPES
# -------------------------------------------------

st.header("🧾 Data Types")

st.dataframe(
    pd.DataFrame(
        {
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        }
    ),
    use_container_width=True
)

st.divider()

# -------------------------------------------------
# DATASET INFORMATION
# -------------------------------------------------

st.header("📊 Dataset Information")

info = get_dataset_info(df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Rows", info["rows"])

with col2:
    st.metric("Columns", info["columns"])

with col3:
    st.metric("Missing Values", int(info["missing_values"].sum()))

with col4:
    st.metric("Duplicate Rows", info["duplicate_rows"])

st.divider()

# -------------------------------------------------
# MISSING VALUES
# -------------------------------------------------

st.header("🚨 Missing Values")

missing = missing_value_table(df)

st.dataframe(missing, use_container_width=True)

st.divider()

# -------------------------------------------------
# UNIQUE VALUES
# -------------------------------------------------

st.header("🔢 Unique Values")

unique = unique_values(df)

st.dataframe(unique, use_container_width=True)

st.divider()

# -------------------------------------------------
# NUMERICAL SUMMARY
# -------------------------------------------------

summary = numerical_summary(df)

if summary is not None:
    st.header("📈 Statistical Summary")
    st.dataframe(summary, use_container_width=True)
else:
    st.warning("No numerical columns found.")

st.divider()

# -------------------------------------------------
# CATEGORICAL SUMMARY
# -------------------------------------------------

categories = categorical_summary(df)

if categories:

    st.header("📋 Category Distribution")

    for column, values in categories.items():

        with st.expander(f"View {column}"):

            st.dataframe(values)

st.divider()

# -------------------------------------------------
# CORRELATION MATRIX
# -------------------------------------------------

corr = correlation_matrix(df)

if corr is not None:

    st.header("📌 Correlation Matrix")

    st.dataframe(corr.round(2), use_container_width=True)
# -------------------------------------------------
# VISUALIZATION
# -------------------------------------------------

st.divider()

st.header("📊 Visualization")

chart = generate_chart(df)

if chart:
    st.image(chart, use_container_width=True)
else:
    st.warning("No suitable chart found.")

# -------------------------------------------------
# QUESTION ANSWERING
# -------------------------------------------------

st.divider()

st.header("❓ Ask Questions")

question = st.text_input("Ask a question about your dataset")

if st.button("Get Answer"):

    answer = answer_question(df, question)

    st.success(answer)    

# -------------------------------------------------
# AI INSIGHTS
# -------------------------------------------------

st.divider()

st.header("🤖 AI Explanation")

summary_text = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Statistics

{summary}
"""


# -------------------------------------------------
# DOWNLOAD CSV
# -------------------------------------------------

st.divider()

st.download_button(
    "📥 Download CSV",
    data=get_download_csv(df),
    file_name="processed_dataset.csv",
    mime="text/csv"
)
st.divider()

st.header("🤖 Ask Gemini About Your Dataset")

question = st.text_input("Ask anything about your dataset")

if st.button("Ask Gemini"):

    if question.strip():

        with st.spinner("Gemini is thinking..."):

            answer = ask_gemini(df, question)

        st.success(answer)

    else:
        st.warning("Please enter a question.")
