# import libraries
import urllib.request
import csv
from bs4 import BeautifulSoup

file = "jobslists.csv"

link_to_er = 'http://www.careercenter.ucsc.edu/ers/erspub/main.cfm?action=non_workstudy'
page = urllib.request.urlopen(link_to_er)
soup = BeautifulSoup(page, 'html.parser')
print(soup.title.string)

# number_of_jobs = soup.find('td', attrs={'class': 'title'}).string.strip()

table_of_jobs = soup.find('table', attrs={'cellpadding': '3'})
rows = table_of_jobs.find_all('tr',attrs={})
number_of_jobs = len(rows)-2

print('There are currently: ' + str(number_of_jobs) + ' available jobs')
print()
jobs = []
for row in rows:
    cols = row.find_all('td', attrs={'class': 'smallwording'})
    links = row.find_all('a', href=True)
    for col in cols:
        print()  # New line

        print(cols[0].text.strip())
        print(cols[1].text.strip())
        print(cols[2].text.strip())
        jobs.append('Posted: ' + cols[0].text.strip())
it = iter(jobs)
job_dict = dict(zip(it, it))
print(job_dict)
with open(file, "w") as file:
    writer = csv.writer(file)
    for item in job_dict.items():
        writer.writerow(item)

file.close()
