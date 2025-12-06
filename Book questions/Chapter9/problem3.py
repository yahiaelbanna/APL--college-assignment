from bs4 import BeautifulSoup

html = """
<table>
    <tr><th>Name</th><th>Age</th></tr>
    <tr><td>Alice</td><td>25</td></tr>
    <tr><td>Bob</td><td>30</td></tr>
</table>
"""

soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')

for row in rows:
    cols = row.find_all(['td', 'th'])
    row_data = [col.text for col in cols]
    print(row_data)