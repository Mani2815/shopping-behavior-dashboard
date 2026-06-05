# -*- coding: utf-8 -*-

import streamlit as st
import altair as alt
import pandas as pd

# ------------------ PAGE CONFIG ------------------

st.set_page_config(
    page_title="Shopping Behaviour Analysis",
    layout="wide",
)

# ------------------ DATA ------------------

df = pd.read_csv("shopping_behavior_updated.csv")

# ------------------ TITLE ------------------

"""
# Shopping Behaviour Analysis Dashboard

An interactive dashboard to explore customer demographics,
spending patterns, and payment behaviour with clean visuals
and flexible filters.
"""

"""
## Dataset Overview
"""

# ------------------ GLOBAL METRICS ------------------

total_purchase = df["Purchase Amount (USD)"].sum()
avg_purchase = df["Purchase Amount (USD)"].mean()
total_orders = len(df)

top_category = df["Category"].value_counts().idxmax()
top_payment = df["Payment Method"].value_counts().idxmax()

with st.container():
    cols = st.columns(3)

    cols[0].metric("Total Purchase Amount (USD)", f"{total_purchase:.2f}")
    cols[1].metric("Average Purchase Value", f"{avg_purchase:.2f}")
    cols[2].metric("Total Purchases", total_orders)

    cols = st.columns(2)
    cols[0].metric("Most Popular Category", top_category)
    cols[1].metric("Most Used Payment Method", top_payment)

"""
## Filter & Compare Shopping Behaviour
"""

# ------------------ FILTERS ------------------

cols = st.columns(4)

with cols[0]:
    category_filter = st.multiselect(
        "Category",
        df["Category"].unique(),
        default=list(df["Category"].unique())
    )

with cols[1]:
    gender_filter = st.multiselect(
        "Gender",
        df["Gender"].unique(),
        default=list(df["Gender"].unique())
    )

with cols[2]:
    payment_filter = st.multiselect(
        "Payment Method",
        df["Payment Method"].unique(),
        default=list(df["Payment Method"].unique())
    )

with cols[3]:
    age_range = st.slider(
        "Age Range",
        int(df["Age"].min()),
        int(df["Age"].max()),
        (18, 60)
    )

# ------------------ APPLY FILTERS ------------------

filtered_df = df[
    (df["Category"].isin(category_filter)) &
    (df["Gender"].isin(gender_filter)) &
    (df["Payment Method"].isin(payment_filter)) &
    (df["Age"] >= age_range[0]) &
    (df["Age"] <= age_range[1])
]

if filtered_df.empty:
    st.warning("No data available for the selected filters.")

# ------------------ VISUAL ANALYTICS ------------------

cols = st.columns([3, 1])

with cols[0].container(border=True):
    "### Age vs Purchase Amount"

    st.altair_chart(
        alt.Chart(filtered_df)
        .mark_circle(size=70)
        .encode(
            alt.X("Age:Q", title="Customer Age"),
            alt.Y("Purchase Amount (USD):Q", title="Purchase Amount (USD)"),
            alt.Color("Category:N"),
            tooltip=["Age", "Category", "Purchase Amount (USD)"]
        )
        .interactive(),
        use_container_width=True
    )

with cols[1].container(border=True):
    "### Category Distribution"

    st.altair_chart(
        alt.Chart(filtered_df)
        .mark_arc()
        .encode(
            alt.Theta("count():Q"),
            alt.Color("Category:N"),
            tooltip=["Category", "count()"]
        ),
        use_container_width=True
    )

cols = st.columns(2)

with cols[0].container(border=True):
    "### Purchase Amount by Gender"

    st.altair_chart(
        alt.Chart(filtered_df)
        .mark_boxplot()
        .encode(
            alt.X("Gender:N"),
            alt.Y("Purchase Amount (USD):Q"),
            alt.Color("Gender:N")
        ),
        use_container_width=True
    )

with cols[1].container(border=True):
    "### Average Spending Trend by Age"

    age_trend = (
        filtered_df
        .groupby("Age", as_index=False)["Purchase Amount (USD)"]
        .mean()
    )

    st.altair_chart(
        alt.Chart(age_trend)
        .mark_line(point=True)
        .encode(
            alt.X("Age:Q"),
            alt.Y("Purchase Amount (USD):Q"),
        ),
        use_container_width=True
    )

cols = st.columns(2)

with cols[0].container(border=True):
    "### Payment Method Usage"

    st.altair_chart(
        alt.Chart(filtered_df)
        .mark_bar()
        .encode(
            alt.X("Payment Method:N"),
            alt.Y("count():Q"),
            alt.Color("Payment Method:N"),
        ),
        use_container_width=True
    )

with cols[1].container(border=True):
    "### Raw Dataset Preview"

    st.dataframe(filtered_df, use_container_width=True)
