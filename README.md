# Shopping Behaviour Analysis Dashboard

An interactive Streamlit dashboard to explore customer demographics, spending patterns, and payment behavior with clean visuals and flexible filters.

## Features

- **Global Metrics**: View key indicators such as Total Purchase Amount, Average Purchase Value, Total Purchases, Most Popular Category, and Most Used Payment Method.
- **Interactive Filters**: Filter the dataset dynamically by:
  - Category
  - Gender
  - Payment Method
  - Age Range
- **Visual Analytics**:
  - **Age vs Purchase Amount**: Scatter plot to visualize individual purchase amounts across different ages and categories.
  - **Category Distribution**: Pie chart showing the proportion of purchases in each category.
  - **Purchase Amount by Gender**: Boxplot comparing spending distributions between genders.
  - **Average Spending Trend by Age**: Line chart tracking the average spending trend across different ages.
  - **Payment Method Usage**: Bar chart displaying the frequency of each payment method used.
- **Raw Dataset Preview**: Inspect the filtered dataset directly within the dashboard.

## Tech Stack

- **Python 3**
- **Streamlit**: Web framework for building the dashboard.
- **Pandas**: Data manipulation and analysis.
- **Altair**: Declarative statistical visualization library.

## Dataset

The dashboard uses the `shopping_behavior_updated.csv` dataset, which contains records of customer purchases including their age, gender, purchased category, purchase amount in USD, and payment method.

## Installation & Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/Mani2815/2547261_APP_Lab2.git
   cd 2547261_APP_Lab2
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requriments.txt
   ```
   *(Note: The requirements file is named `requriments.txt`)*

3. **Run the Dashboard**:
   ```bash
   streamlit run 2547261_Lab2.py
   ```

4. **Access the Application**:
   The Streamlit app will automatically open in your default web browser (usually at `http://localhost:8501`).
