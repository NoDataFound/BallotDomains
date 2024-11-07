import csv

with open('candidates_domains_all.csv', 'r') as infile, open('DO_NOT_AUTOMATE_THIS_REVIEW_FIRST_BLOCK_LIST.txt', 'w') as outfile:
    reader = csv.DictReader(infile)
    for row in reader:
        domains = row['Domains'].split(', ')
        for domain in domains:
            if domain:
                outfile.write(domain + '\n')
