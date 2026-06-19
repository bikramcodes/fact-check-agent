from tavily import TavilyClient
import streamlit as st

tavily_key = st.secrets["TAVILY_API_KEY"]

client = TavilyClient(
    api_key=tavily_key
)

def search_claim(claim):

    result = client.search(
        query=claim,
        search_depth="advanced",
        max_results=5
    )

    return result
