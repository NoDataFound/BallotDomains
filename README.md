# Ballot.Domains

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.3.0-brightgreen)
![Plotly](https://img.shields.io/badge/Plotly-5.3.1-orange)

Ballot.Domain is a dynamic domain tracker for political candidates. Using the DNSlytics API, it fetches and updates domain lists for each candidate daily.

<img width="1880" alt="BallotDomains" src="https://raw.githubusercontent.com/NoDataFound/BallotDomains/refs/heads/main/images/ballotdomains.png">
<img width="1880" alt="BallotDomains Terms Word Cloud" src="https://github.com/NoDataFound/BallotDomains/blob/main/images/ballotdomains_terms_wordcloud.png">
<img width="1880" alt="BallotDomains Terms Word Cloud" src="https://github.com/NoDataFound/BallotDomains/blob/main/images/VT_graph.png">

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

### Candidate Domain Fetch Script

To fetch and update candidate domains, use the `domain_fetch.py` script. This script runs daily, retrieving the latest domain list for each candidate and updating `candidates_domains_all.csv`.

- **Run Script**: 

    ```bash
    python domain_fetch.py
    ```

- **Output Location**: `candidates_domains_all.csv` will be updated with the latest domains.
- **Frequency**: The script is set to run every 24 hours automatically. Once started, it will check for new data every 24 hours and update the CSV file accordingly.

### Creating the Blocklist

To generate a blocklist from the domains, use the `generate_blocklist.py` script. This script extracts domains from `candidates_domains_all.csv` and outputs them to `DO_NOT_AUTOMATE_THIS_REVIEW_FIRST_BLOCK_LIST.txt`.

- **Run Script**: 

    ```bash
    python generate_blocklist.py
    ```

- **Output Location**: The blocklist will be saved as `DO_NOT_AUTOMATE_THIS_REVIEW_FIRST_BLOCK_LIST.txt`.

## Application Features

- **Candidate Selection**: Select candidates to view domain stats.
- **Domain Count**: Shows each candidate's total domains and updates regularly.
- **Download Data**: Download combined domain data for selected candidates as CSV.
- **Dynamic Chart**: Sidebar donut chart showing percentage of domains by candidate.
