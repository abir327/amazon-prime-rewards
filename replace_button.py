import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS for the neon button
css = """
<style>
@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.neon-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 400px;
  height: 100px;
  background: #111;
  color: #fff;
  font-family: Arial, sans-serif;
  font-size: 32px;
  font-weight: bold;
  text-transform: uppercase;
  text-decoration: none;
  border-radius: 50px;
  z-index: 1;
  margin: 40px auto;
  border: none;
  cursor: pointer;
  box-sizing: border-box;
}

.neon-btn::before, .neon-btn::after {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: 60px;
  background: conic-gradient(from var(--angle), transparent 20%, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
  z-index: -1;
  animation: 3s spin linear infinite;
}

.neon-btn::after {
  filter: blur(25px);
}

.neon-btn-inner {
  position: absolute;
  inset: 4px;
  background: #131921;
  border-radius: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: -1;
}

@keyframes spin {
  from {
    --angle: 0deg;
  }
  to {
    --angle: 360deg;
  }
}
</style>
<a href="https://www.amazon.com/gp/gss/direct-optin?ie=UTF8&amp;ref_=cct_cg_optingiveaway_1a1&amp;pf_rd_p=34d0e971-d849-4a1f-8420-86e641393c56&amp;pf_rd_r=VR4B35H59H0XTZHNY1H4" class="neon-btn">
  <span class="neon-btn-inner"></span>
  Claim Now
</a>
"""

# The target to replace
# We need to find the <a ...><img ... src="...OPT-in_Sweepstakes_LP_Desktop_V2...gif" ...></a>
pattern = re.compile(r'<a href="[^"]*cct_cg_optingiveaway_1a1[^"]*">.*?OPT-in_Sweepstakes_LP_Desktop_V2.*?</a>', re.DOTALL)

if pattern.search(content):
    new_content = pattern.sub(css, content)
    with open('public/amazon.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully!")
else:
    print("Could not find the target string to replace.")

