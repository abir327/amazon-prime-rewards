import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS and HTML for the new hero section
new_hero = """
<style>
@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.hero-container {
  width: 100%;
  max-width: 1500px;
  margin: 0 auto;
  background: linear-gradient(135deg, #004d80 0%, #0099cc 100%);
  color: white;
  text-align: center;
  padding: 60px 20px;
  border-radius: 8px;
  box-sizing: border-box;
  font-family: "Amazon Ember", Arial, sans-serif;
}

.hero-title {
  font-size: 48px;
  font-weight: 800;
  margin-bottom: 10px;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 28px;
  font-weight: 400;
  margin-bottom: 40px;
}

.neon-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 250px;
  height: 60px;
  background: #111;
  color: #fff;
  font-family: "Amazon Ember", Arial, sans-serif;
  font-size: 22px;
  font-weight: bold;
  text-transform: uppercase;
  text-decoration: none;
  border-radius: 30px;
  z-index: 1;
  margin: 0 auto;
  border: none;
  cursor: pointer;
  box-sizing: border-box;
}

.neon-btn::before, .neon-btn::after {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 40px;
  background: conic-gradient(from var(--angle), transparent 20%, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
  z-index: -1;
  animation: 3s spin linear infinite;
}

.neon-btn::after {
  filter: blur(15px);
}

.neon-btn-inner {
  position: absolute;
  inset: 3px;
  background: #131921;
  border-radius: 28px;
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
<div class="hero-container">
  <div class="hero-title">Sign up for texts</div>
  <div class="hero-subtitle">for a chance to win $1,000</div>
  <a href="https://www.amazon.com/gp/gss/direct-optin?ie=UTF8&amp;ref_=cct_cg_optingiveaway_1a1&amp;pf_rd_p=34d0e971-d849-4a1f-8420-86e641393c56&amp;pf_rd_r=VR4B35H59H0XTZHNY1H4" class="neon-btn">
    <span class="neon-btn-inner"></span>
    Claim Now
  </a>
</div>
"""

pattern = re.compile(r'<a href="[^"]*cct_cg_optingiveaway_1a1[^"]*">.*?OPT-in_Sweepstakes_LP_Desktop_V2.*?</a>', re.DOTALL)

if pattern.search(content):
    new_content = pattern.sub(new_hero, content)
    with open('public/amazon.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully!")
else:
    print("Could not find the target string to replace.")
