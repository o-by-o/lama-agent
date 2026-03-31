const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();

  const filePath = 'file://' + path.resolve(__dirname, 'апрель_2026.html');
  await page.goto(filePath, { waitUntil: 'networkidle0' });

  // Get full page size
  const bodyHandle = await page.$('.page');
  const box = await bodyHandle.boundingBox();

  await page.setViewport({
    width: Math.ceil(box.width) + 80,
    height: Math.ceil(box.height) + 80,
    deviceScaleFactor: 2
  });

  await page.goto(filePath, { waitUntil: 'networkidle0' });

  await page.screenshot({
    path: 'апрель_2026.jpg',
    type: 'jpeg',
    quality: 95,
    fullPage: true
  });

  await browser.close();
  console.log('Done: апрель_2026.jpg');
})();
