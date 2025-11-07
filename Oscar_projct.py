import pandas as pd 
from bs4 import BeautifulSoup
import requests
import re       

headers = {"User-Agent": "Mozilla/5.0 ..."}

url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
req = requests.get(url, headers=headers)
print(req)

soup = BeautifulSoup(req.text, "html.parser")

# Find the Oscar-winning films table
table = soup.find("table", class_="wikitable")

# Extract data
Film = []
Year = []
Awards = []
Nominations = []

for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if len(cols) == 4:
        Film.append(cols[0].text.strip())
        Year.append(cols[1].text.strip())
        Awards.append(cols[2].text.strip())
        Nominations.append(cols[3].text.strip())

# Create DataFrame
df = pd.DataFrame({
    "Film": Film,
    "Year": Year,
    "Awards": Awards,
    "Nominations": Nominations
})
df.index = range(1, len(df) + 1)

# print(df.head(50))
# print(f"\nTotal Films: {len(df)}")


# FOR COLLECTING THE PARTICULAR DATA WHICH IS UNDER <tr>---
arr=[]
for i in soup.findAll('tr'):
    arr.append(i)
# print(arr[5])
arr=[]
for i in soup.findAll('td'):                    #<td>
    arr.append(i)
# print(arr[4])

# CLEANING THE <td> DATA---
arr=[]
for i in soup.findAll('td'):                    
    arr.append(i.text)
x= arr[12].strip()                      #STRIP()
y = re.sub('^', " ", arr[8])            #REGEX()
# print(x)
# print(y)

# DATA COLUMNS(FINAL DATA CLEAN)---
Film=[]
Year=[]
Awards=[]
Nominations=[]
count=0
for i in soup.findAll('td'):
    if count==0:
        Film.append(i.text.strip())
        count+=1
    elif count==1:
        Year.append(i.text.strip())
        count+=1
    elif count==2:
        Awards.append(i.text.strip())
        count+=1
    elif count==3:
        Nominations.append(i.text.strip())
        count=0
# print(Nominations)
# print(len(Nominations))

# ✅ Save the scraped data to a CSV file
# df.to_csv("Oscar_Winning_Films.csv", index=False)
# print("\n✅ CSV file 'Oscar_Winning_Films.csv' created successfully!")




