const fs = require('fs');
const cheerio = require('cheerio');

const content = fs.readFileSync('public/amazon.html', 'utf-8');
const $ = cheerio.load(content);

let targetA = null;
$('a').each((i, el) => {
    const href = $(el).attr('href');
    if (href && href.includes('cct_cg_optingiveaway_1a1')) {
        targetA = el;
    }
});

if (targetA) {
    console.log("Found target A tag:");
    console.log($.html(targetA));
} else {
    console.log("Could not find the target A tag");
}
