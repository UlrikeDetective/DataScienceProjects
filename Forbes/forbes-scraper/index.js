const puppeteer = require('puppeteer');
const fs = require('fs');

async function scrapeBillionaires() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  // Go to Forbes Billionaires list
  await page.goto(
    'https://www.forbes.com/billionaires/',
    {
      timeout: 0,
    },
  );

  const links = await page.$$eval('a.color-link', (links) => links.slice(2).map((link) => link.href));
  const billionaireList = [];

  for (let link of links) {
    try {
      await page.goto(link, { timeout: 10 });

      // Get rank
      const rank = await page.$eval('.listuser-item__list--rank', (el) => el.innerText.trim()).catch(() => 'N/A');

      // Get name
      const name = await page.$eval('h1.listuser-header__name', (el) => el.innerText.trim()).catch(() => 'N/A');

      // Get title
      const title = await page
        .$eval('div.listuser-header__headline-default', (el) => el.innerText.trim())
        .catch(() => 'N/A');

      // Get organization
      const organization = await page
        .$eval('a.listuser-header__organization', (el) => el.innerText.trim())
        .catch(() => 'N/A');

      // Get net worth
      const netWorth = await page.$eval('div.profile-info__item-value', (el) => el.innerText.trim()).catch(() => 'N/A');

      // Get biography text
      const bio = await page.$eval('ul', (el) => el.innerText.trim()).catch(() => 'N/A');

      // Get additional stack data
      const stackData = await page.evaluate(() => {
        let data = {};
        const titles = Array.from(document.querySelectorAll('.profile-stats__title'));
        const texts = Array.from(document.querySelectorAll('.profile-stats__text'));
        titles.forEach((title, i) => (data[title.innerText.trim()] = texts[i].innerText.trim()));
        return data;
      });

      // Push data to billionaireList
      billionaireList.push({
        Rank: rank,
        Name: name,
        Title: title,
        Organization: organization,
        NetWorth: netWorth,
        Stack: stackData,
        Bio: bio,
      });
    } catch (err) {
      console.log(`Error scraping ${link}: ${err}`);
    }
  }

  await browser.close();
  return billionaireList;
}

scrapeBillionaires().then((data) => {
  console.log(data); // Output data to console
});

async function saveDataToFile(data, filename = 'forbes_billionaires.json') {
  fs.writeFileSync(filename, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`Data saved to ${filename}`);
}

scrapeBillionaires().then((data) => {
  saveDataToFile(data);
});