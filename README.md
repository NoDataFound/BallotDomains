# Ballot.Domain

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.3.0-brightgreen)
![Plotly](https://img.shields.io/badge/Plotly-5.3.1-orange)

Ballot.Domain is a dynamic domain tracker for political candidates. Using the DNSlytics API, it fetches and updates domain lists for each candidate daily. 

<img width="1880" alt="BallotDomains" src="https://raw.githubusercontent.com/NoDataFound/BallotDomains/refs/heads/main/images/ballotdomains.png">

## Features

- **Dynamic Domain Search**: Fetches candidate-specific domains from DNSlytics API.
- **Interactive UI**: Displays domain count, metrics, and data in a Streamlit interface.
- **Daily Update**: Checks DNSlytics for new domains every 24 hours and updates the CSV automatically.
- **Visual Analytics**: Donut chart in the sidebar showing domain distribution by candidate.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NoDataFound/BallotDomains.git
    cd BallotDomains
    ```

2. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Add your DNSlytics API key to a `.env` file in the root directory:

    ```plaintext
    DNSLYTICS_API_KEY=your_api_key_here
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run ballotdomains.py
    ```

## Usage

- **Candidate Selection**: Select candidates to view domain stats.
- **Domain Count**: Shows each candidate's total domains and updates regularly.
- **Download Data**: Download combined domain data for selected candidates as CSV.
- **Dynamic Chart**: Sidebar donut chart showing percentage of domains by candidate.


