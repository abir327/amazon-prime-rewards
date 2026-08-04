from bs4 import BeautifulSoup

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find the anchor with cct_cg_optingiveaway_1a1
target_a = None
for a in soup.find_all('a'):
    if 'href' in a.attrs and 'cct_cg_optingiveaway_1a1' in a['href']:
        target_a = a
        break

if target_a:
    print(f"Found target A tag: {target_a}")
else:
    print("Could not find the target A tag")

