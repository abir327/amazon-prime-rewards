import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = '<a href="https://www.amazon.com/gp/gss/direct-optin?ie=UTF8&amp;ref_=cct_cg_optingiveaway_1a1" class="neon-btn">'
new_str = '<a href="https://app.hawktrk.com/click?pid=2&amp;offer_id=22011&amp;sub2=u653724&amp;sub5=Rocky" class="neon-btn">'

if old_str in content:
    new_content = content.replace(old_str, new_str)
    with open('public/amazon.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Link updated successfully!")
else:
    print("Could not find the target string to replace.")

