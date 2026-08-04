const fs = require('fs');
const cheerio = require('cheerio');

const content = fs.readFileSync('public/amazon.html', 'utf-8');
const $ = cheerio.load(content, { decodeEntities: false });

let targetA = null;
$('a').each((i, el) => {
    const href = $(el).attr('href');
    if (href && href.includes('cct_cg_optingiveaway_1a1')) {
        targetA = el;
    }
});

if (targetA) {
    const css = `
<style>
@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.neon-btn-container {
    text-align: center;
    margin-top: 15px;
    margin-bottom: 20px;
    position: relative;
    z-index: 10;
}

.neon-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 200px;
  height: 50px;
  background: #111;
  color: #fff !important;
  font-family: "Amazon Ember", Arial, sans-serif;
  font-size: 18px;
  font-weight: bold;
  text-transform: uppercase;
  text-decoration: none !important;
  border-radius: 0px;
  z-index: 1;
  border: none;
  cursor: pointer;
  box-sizing: border-box;
}

.neon-btn:hover {
  text-decoration: none !important;
  color: #fff !important;
}

.neon-btn::before, .neon-btn::after {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 0px;
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
  border-radius: 0px;
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
<div class="neon-btn-container">
  <a href="https://www.amazon.com/gp/gss/direct-optin?ie=UTF8&amp;ref_=cct_cg_optingiveaway_1a1" class="neon-btn">
    <span class="neon-btn-inner"></span>
    Claim Now
  </a>
</div>
`;
    $(targetA).parent().after(css);
    fs.writeFileSync('public/amazon.html', $.html());
    console.log("Success");
} else {
    console.log("Not found");
}
