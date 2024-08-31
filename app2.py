import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data loading function
def load_data():
    data = r"C:\Users\sumey\OneDrive\Desktop\10 data\dataa\raw_data\data.csv"
    df_news = pd.read_csv(data)  # Load the data
    return df_news

# Page 1: Top 10 Sources
def page_top_10(df_news):
    st.title(' Top 10 source with most article published')

    # Count articles per source
    article_counts = df_news['source_name'].value_counts()

    # Convert Series to DataFrame
    df_counts = article_counts.reset_index()
    df_counts.columns = ['source_name', 'article_count']

    # Sort the DataFrame by article_count in descending order
    df_sorted = df_counts.sort_values(by='article_count', ascending=False)

    # Assign ranks starting from 1
    df_sorted['rank'] = range(1, len(df_sorted) + 1)

    # Display the top 10 sources with their ranks
    top_10 = df_sorted.head(10)
    st.write("Top 10 sources with most article published :")

    # Create a bar plot for visualization
    fig, ax = plt.subplots()
    sns.barplot(x='article_count', y='source_name', data=top_10, palette='viridis', ax=ax)
    ax.set_title('Top 10 Sources by Article Count')
    ax.set_xlabel('Number of Articles')
    ax.set_ylabel('Source Name')

    st.pyplot(fig)

# Page 2: List 10 Sources
def page_list_10(df_news):
    st.title('List of 10 Sources with Their Count')

    # Count articles per source
    article_counts = df_news['source_name'].value_counts()

    # Convert Series to DataFrame
    df_counts = article_counts.reset_index()
    df_counts.columns = ['source_name', 'article_count']

    # Sort the DataFrame by article_count in ascending order
    df_sorted = df_counts.sort_values(by='article_count', ascending=True)

    # Assign ranks starting from 1
    df_sorted['rank'] = range(1, len(df_sorted) + 1)

    # Display the list of sources with their counts
    list_10 = df_sorted.head(10)
    st.write("List of 10 sources with their count:")

    # Create a bar plot for visualization
    fig, ax = plt.subplots()
    sns.barplot(x='article_count', y='source_name', data=list_10, palette='rocket', ax=ax)
    ax.set_title('List of 10 Sources by Article Count')
    ax.set_xlabel('Number of Articles')
    ax.set_ylabel('Source Name')

    st.pyplot(fig)

# Main Streamlit app
st.sidebar.title('Navigation')
page = st.sidebar.radio('Select a Page', ['Top 10 Sources', 'List 10 Sources'])

# Load data
df_news = load_data()

if page == 'Top 10 Sources':
    page_top_10(df_news)
elif page == 'List 10 Sources':
    page_list_10(df_news)
