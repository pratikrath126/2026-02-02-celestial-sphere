const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Navigate to the local index.html file
  const filePath = `file://${path.resolve('index.html')}`;
  console.log(`Navigating to ${filePath}`);
  await page.goto(filePath, { waitUntil: 'networkidle' });

  // Wait a moment for canvas animation to render
  await page.waitForTimeout(1000);

  // Take a screenshot to verify
  await page.screenshot({ path: 'screenshot_verify.png', fullPage: true });
  console.log('Screenshot saved to screenshot_verify.png');

  await browser.close();
})();
