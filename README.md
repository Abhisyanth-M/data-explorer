# Smart Data Explorer Dashboard

A Streamlit web application that allows users to upload any CSV file and explore the data interactively — no coding required.

## Live Demo
https://data-explorer-f3jtejr9emx6umdsyjc83u.streamlit.app/

## Overview
Smart Data Explorer is designed for anyone who wants to quickly understand a dataset without writing code. Upload a CSV file and instantly get a preview, statistics, filtering options and column insights.

## Features
- Upload any CSV file
- Display dataset preview
- Show total number of rows and columns
- Select any column dynamically
- Display unique values of selected column
- Filter dataset based on selected column value
- Display filtered results
- Show basic statistical summary
- Show data type of selected column

## Tech Stack
- Python
- Streamlit
- Pandas

## How It Works
1. User uploads a CSV file through the file uploader
2. Pandas reads and loads the dataset into a dataframe
3. User selects a column from the dropdown
4. App displays unique values, data type and filtered results based on selection
5. Statistical summary is generated using pandas describe()

## Installation and Running Locally
```bash
git clone https://github.com/Abhisyanth-M/data-explorer
cd data-explorer
pip install streamlit pandas
python -m streamlit run app.py
```

## Limitations
- Only supports CSV file format
- Large files may load slowly depending on system memory
- No support for data cleaning or missing value handling

## Future Improvements
- Support for Excel and JSON file formats
- Data visualization with charts and graphs
- Missing value detection and handling
- Download filtered data as CSV

## GitHub
https://github.com/Abhisyanth-M/data-explorer
```
