import streamlit as st
st.title("Global Trade Arbitrage App")
import streamlit as st
from scraper import scrape_all_marketplaces
from arbitrage_engine import find_arbitrage_opportunities
from ai_assistant import chat_with_ai
import pandas as pd
import os

st.set_page_config(page_title="Global Trade Arbitrage Intelligence", layout="wide")
st.title("🌍 Global Trade Arbitrage Intelligence App")

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Tabs for navigation
tabs = st.tabs([
    "📈 Arbitrage Finder",
    "📊 Global Leads",
    "📂 Upload Data",
    "🤖 AI Assistant"
])

# 1) Arbitrage Finder
with tabs[0]:
    st.subheader("Find Trade Arbitrage Opportunities")
    if st.button("Scrape & Analyze"):
        st.info("Scraping marketplaces…")
        df = scrape_all_marketplaces()
        st.success("Scrape complete!")
        st.info("Analyzing arbitrage opportunities…")
        arb_df = find_arbitrage_opportunities(df)
        st.dataframe(arb_df)
        arb_df.to_csv("data/arbitrage_opportunities.csv", index=False)
        st.success("Results saved to data/arbitrage_opportunities.csv")

# 2) Global Leads
with tabs[1]:
    st.subheader("All Leads & Market Data")
    if os.path.exists("data/scraped_leads.csv"):
        leads_df = pd.read_csv("data/scraped_leads.csv")
        st.dataframe(leads_df)
    else:
        st.warning("No scraped leads yet. Run ‘Scrape & Analyze’ first.")

# 3) Upload Data
with tabs[2]:
    st.subheader("Upload Your Own Product/Price Data")
    uploaded = st.file_uploader("Upload CSV", type="csv")
    if uploaded:
        upload_df = pd.read_csv(uploaded)
        upload_df.to_csv("data/uploaded_data.csv", index=False)
        st.success("File uploaded ✔")
        st.dataframe(upload_df)

# 4) AI Assistant
with tabs[3]:
    st.subheader("Ask the AI Anything About Trading/Arbitrage")
    q = st.text_input("Your question:")
    if q:
        answer = chat_with_ai(q)
        st.write("🤖", answer)
