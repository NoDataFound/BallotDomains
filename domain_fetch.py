import os
import requests
import pandas as pd
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('DNSLYTICS_API_KEY')
if not API_KEY:
    raise ValueError("Please set the DNSLYTICS_API_KEY environment variable in your .env file.")

csv_path = "candidates_domains_all.csv"

df = pd.read_csv(csv_path)

def fetch_domains(candidate_name):
    candidate_query = candidate_name.replace(" ", "").lower()
    all_domains = set()
    
    for page in range(1, 41): 
        url = f"https://api.dnslytics.net/v1/domainsearch/{candidate_query}?apikey={API_KEY}&tld=all&active=all&fromdate=20150101&page={page}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "succeed":
                page_domains = {domain_info["domain"] for domain_info in data.get("data", {}).get("domains", [])}
                all_domains.update(page_domains)
                
                if len(page_domains) < 2500:
                    break
            else:
                print(f"API did not succeed for {candidate_name}: {data}")
                break
        else:
            print(f"Error fetching data for {candidate_name} on page {page}: {response.status_code}")
            break

    return list(all_domains)

def update_domains():
    for idx, row in df.iterrows():
        candidate_name = row["Candidate"]
        existing_domains = set(str(row["Domains"]).split(", "))  

        new_domains = fetch_domains(candidate_name)
        new_domains_set = {domain.replace(".", "[.]") for domain in new_domains}  # Defang domains

        domains_to_add = new_domains_set - existing_domains

        if domains_to_add:
            updated_domains = ", ".join(existing_domains | domains_to_add)
            df.at[idx, "Domains"] = updated_domains
            print(f"Updated domains for {candidate_name}: {domains_to_add}")
        else:
            print(f"No new domains found for {candidate_name}.")

    df.to_csv(csv_path, index=False)
    print(f"CSV updated successfully on {datetime.now()}.")

def daily_update():
    last_checked = datetime.now() - timedelta(days=1)
    while True:
        current_time = datetime.now()
        if current_time - last_checked >= timedelta(days=1):
            update_domains()
            last_checked = current_time
        time.sleep(86400)  

if __name__ == "__main__":
    daily_update()
