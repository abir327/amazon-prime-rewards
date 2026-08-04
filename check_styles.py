import re
with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()
match = re.search(r'(<style>/\* Fix horizontal scroll white space for mobile.*?</style>)', content, re.DOTALL)
if match:
    print(match.group(1))

match_vp = re.search(r'<meta name="viewport".*?>', content)
if match_vp:
    print(match_vp.group(0))
