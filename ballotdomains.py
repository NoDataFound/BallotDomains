import os
import requests
import pandas as pd
import time
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv

load_dotenv('.env')

st.set_page_config(page_title="Ballot.Domain", page_icon="🇺🇸", layout="wide")

csv_file_path = "candidates_domains.csv"

API_KEY = os.getenv('DNSLYTICS_API_KEY')
if not API_KEY:
    raise ValueError("Please set the DNSLYTICS_API_KEY environment variable in your .env file.")

def load_data():
    return pd.read_csv(csv_file_path)

df = load_data()
last_modified_time = os.path.getmtime(csv_file_path)

st.sidebar.image("images/ballotdomainlog.png", width=150, use_column_width=True)
selected_candidates = st.sidebar.multiselect("Select Candidates", df["Candidate"].unique())
show_combined = st.sidebar.checkbox("Show Combined Domains")

party_colors = {"Republican": "#FFB3B3", "Democratic": "#ADD8E6"}
candidate_dfs = []

def display_donut_chart():
    domain_counts = df.set_index("Candidate")["Domains"].str.split(", ").apply(len)
    fig = px.pie(
        values=domain_counts,
        names=domain_counts.index,
        title="Percentage of Domains by Candidate",
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    fig.update_traces(textinfo="percent+label")
    st.sidebar.plotly_chart(fig, use_container_width=True)

def display_candidates():
    if selected_candidates:
        cols = st.columns(len(selected_candidates))
        for idx, candidate_name in enumerate(selected_candidates):
            candidate_data = df[df["Candidate"] == candidate_name].iloc[0]
            domain_count = len(candidate_data["Domains"].split(", "))
            growth_indicator = "+1" if domain_count > 1 else "0"
            
            with cols[idx]:
                st.image(candidate_data["Photo"], width=100)
                st.metric(label=candidate_data["Candidate"], value=domain_count, delta=growth_indicator)
                
                domains = candidate_data["Domains"].split(", ")
                candidate_domains_df = pd.DataFrame({"Domain": domains})
                
                if not show_combined:
                    st.write(f"{candidate_data['Candidate']}'s Domains:")
                    color = party_colors.get(candidate_data["Party"], "#FFFFFF")
                    st.dataframe(candidate_domains_df.style.set_properties(**{
                        'background-color': color,
                        'color': 'black'
                    }))
                
            candidate_domains_df["Candidate"] = candidate_data["Candidate"]
            candidate_dfs.append(candidate_domains_df)

def display_combined():
    if show_combined and candidate_dfs:
        combined_df = pd.concat(candidate_dfs, ignore_index=True)
        st.write("Combined Domains for Selected Candidates")
        st.dataframe(combined_df)
        
        csv = combined_df.to_csv(index=False)
        st.download_button(
            label="Download Combined Domains as CSV",
            data=csv,
            file_name="combined_domains.csv",
            mime="text/csv",
        )

display_donut_chart()
display_candidates()
display_combined()

while True:
    current_modified_time = os.path.getmtime(csv_file_path)
    if current_modified_time != last_modified_time:
        df = load_data()
        last_modified_time = current_modified_time
        st.experimental_rerun()
    time.sleep(5)  