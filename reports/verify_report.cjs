/* Offline browser validation of the standalone report. See README for dependencies. */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
let playwright;
for (const candidate of ['playwright','/tmp/qaag-report-tools/node_modules/playwright']) {
  try { playwright=require(candidate); break; } catch (error) {
    if (error.code!=='MODULE_NOT_FOUND') throw error;
  }
}
if (!playwright) throw new Error('Install Playwright 1.55.0 and its Chromium browser; see README.');
const artifact=path.resolve(process.argv[2]||path.join(__dirname,'research-report.html'));
const screenshotDir=process.argv[3]&&path.resolve(process.argv[3]);
const checks=[];
function check(condition,message){if(!condition)throw new Error(message);checks.push(message);}
(async()=>{
 const browser=await playwright.chromium.launch({headless:true,args:['--no-sandbox'],
  ...(process.env.QAAG_CHROMIUM_PATH?{executablePath:process.env.QAAG_CHROMIUM_PATH}:{})});
 try {
  const context=await browser.newContext({viewport:{width:1440,height:1000},reducedMotion:'reduce',offline:true});
  const page=await context.newPage();const errors=[],requests=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('request',r=>{if(/^https?:/i.test(r.url()))requests.push(r.url());});
  await page.goto(pathToFileURL(artifact).href,{waitUntil:'load'});
  await page.waitForSelector('#atlas-grid .route-card');
  const data=await page.locator('#report-data').evaluate(el=>JSON.parse(el.textContent));
  check(data.routes.length>=69,'All 69 documented route records are embedded');
  check(data.claims.length>=364,'All 364 registered claims are embedded');
  check(data.sources.length>50,'The scientific source archive is embedded');
  check(data.claims.find(c=>c.id==='C-364')?.status==='REFUTED','Rejected originality remains explicit');
  check(await page.locator('main .katex').count()>30,'Main article mathematics renders offline');
  check(await page.locator('main .katex-error').count()===0,'Main article has no KaTeX parse failures');
  const texts=async selector=>(await page.locator(selector).textContent()).trim();
  const set=async(id,value)=>page.locator('#'+id).evaluate((el,v)=>{el.value=String(v);el.dispatchEvent(new Event('input',{bubbles:true}));},value);
  for(const[t,count]of[[-1.2,0],[-1,1],[0,2],[1,3],[1.1,4],[1.25,2],[1.4,0]]){
   await set('geometry-t',t);check(await texts('#geometry-count')===String(count),'Real intersection count at t='+t);
  }
  await set('geometry-t',.4);
  await page.locator('#geometry-play').click();
  await page.waitForFunction(()=>document.getElementById('geometry-t').value!=='0.4');
  await page.locator('.sidebar .motion-toggle').click();
  const pausedValue=await page.locator('#geometry-t').inputValue();
  await page.evaluate(()=>new Promise(resolve=>setTimeout(resolve,120)));
  check(await page.locator('#geometry-t').inputValue()===pausedValue,'Global pause stops the running geometry animation');
  await page.locator('#geometry-play').click();await set('geometry-t',.4);
  await set('normal-scale',4);
  check(await texts('#normal-gap')==='16.00'&&await texts('#normal-alpha')==='32.00','Scaling preserves the normalized gap');
  await set('normal-scale',1);
  await page.locator('#normal-play').click();
  await page.waitForFunction(()=>document.getElementById('normal-scale').value!=='1');
  check((await texts('#normal-svg')).includes('normalized gap = ½'),'Rescaling animation preserves its normalized spectrum');
  await page.locator('#normal-play').click();await set('normal-scale',1);
  await set('copy-depth',4);await page.locator('#schur-preset').click();
  check((await texts('#copy-svg')).length>0,'Copy-cost illustration renders');
  for(const c of [0,1]){
   await page.locator('#dpp-case-'+c).click();
   for(const[a,b]of[[0,0],[25,65],[90,180],[133,71]]){
    await set('dpp-angle-a',a);await set('dpp-angle-b',b);
    check(await texts('#dpp-total')==='1.00','DPP weights normalize for case '+c+', frames '+a+'/'+b);
    check(await texts('#dpp-cross')===(c?'0.50':'1.00'),'Cross-block volume mass is frame-independent for case '+c);
   }
  }
  await page.locator('#dpp-case-0').click();await set('dpp-angle-a',25);await set('dpp-angle-b',65);
  await page.locator('#conversion-reset').click();
  for(let i=0;i<4;i++)await page.locator('#conversion-next').click();
  check((await texts('.step-detail')).includes('7/16'),'Three-copy final branch explains the success law');
  await page.locator('#conversion-prev').click();await page.locator('#conversion-reset').click();
  await page.locator('#conversion-simulate').click();
  check((await texts('#conversion-trials')).includes('/ 100 trials'),'Illustrative trial simulation updates its counters');
  await page.locator('#conversion-clear').click();
  for(const n of [2,12,24]){
   await set('dpp-dimension',n);
   const actual=Number((await texts('#dimension-lower')).replace(/[^0-9]/g,''));
   check(actual===Math.ceil((1+Math.sqrt(1+3*2**n/4))/2),'Classical lower-bound curve at n='+n);
  }
  await set('dpp-dimension',12);
  await set('disk-degree',60);
  check((await texts('#disk-infidelity')).includes('e-'),'Disk sensitivity remains finite at D=60');
  await page.locator('#disk-bits').click();check(await page.locator('#disk-bounds').isHidden(),'Coefficient access changes the displayed comparison');
  await page.locator('#disk-copies').click();await set('disk-degree',15);
  await page.locator('#atlas-search').fill('Schur');
  check(await page.locator('#atlas-grid .route-card').count()>0&&await page.locator('#atlas-grid .route-card').count()<69,'Route search filters the full archive');
  await page.locator('#atlas-grid .route-card button').first().click();
  check(await page.locator('#reader-dialog').isVisible(),'Route detail opens accessibly');
  await page.keyboard.press('Escape');check(await page.locator('#reader-dialog').isHidden(),'Escape closes the offline reader');
  await page.locator('#atlas-search').fill('');
  await page.locator('#claim-search').fill('C-361');await page.locator('#claim-list button').first().click();
  check((await texts('#reader-body')).includes('BN'),'Registered theorem opens with its full resource statement');
  await page.locator('#reader-close').click();await page.locator('#claim-search').fill('');
  await page.locator('#sources-tab').click();await page.locator('#source-search').fill('support-plucker-r9.md');
  check(await page.locator('#source-list button').count()>=2,'Independent proof and audit are searchable');
  await page.locator('#source-list button').first().click();
  check(!(await texts('#reader-body')).includes('Source not embedded'),'Full scientific source opens offline');
  await page.locator('#reader-close').click();await page.locator('#source-search').fill('');await page.locator('#claims-tab').click();
  await page.locator('[data-source="scouting/support-plucker-r9.md"]').click();
  await page.locator('#reader-body a[href="../verdicts/support-plucker-r9.md"]').click();
  check((await texts('#reader-title')).includes('independent'),'Relative source links open the embedded independent audit');
  await page.locator('#reader-back').click();
  check((await texts('#reader-title')).includes('measured tableau'),'Reader history returns to the originating proof');
  await page.keyboard.press('Escape');
  // Every article-level source action must resolve to a real embedded document.
  const direct=await page.locator('[data-source]').evaluateAll(els=>els.map(el=>el.dataset.source));
  const paths=new Set(data.sources.flatMap(s=>[s.id,s.path]));
  check(direct.every(p=>paths.has(p)),'All main-article source links resolve');
  const routeLinks=data.routes.flatMap(r=>r.sources||[]).map(s=>typeof s==='string'?s:s.path||s.id);
  check(routeLinks.every(p=>paths.has(p)),'All research-route source links resolve');
  check(data.routes.every(r=>(r.claimIds||[]).every(id=>data.claims.some(c=>c.id===id))),'All route claim links resolve');
  await page.evaluate(()=>scrollTo(0,0));
  await page.waitForFunction(()=>document.querySelector('#chapter-nav a[aria-current="true"]')?.hash==='#verdict');
  check(await page.locator('#chapter-select').inputValue()==='#verdict','Returning to the hero resets the current chapter');
  if(screenshotDir){fs.mkdirSync(screenshotDir,{recursive:true});await page.screenshot({path:path.join(screenshotDir,'desktop.png')});}
  await page.setViewportSize({width:390,height:844});await page.evaluate(()=>scrollTo(0,0));
  check(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'Mobile article has no horizontal overflow');
  check(await page.locator('#chapter-select').isVisible(),'Mobile chapter navigation is available');
  if(screenshotDir)await page.screenshot({path:path.join(screenshotDir,'mobile.png')});
  await page.locator('#chapter-select').selectOption('#dpp');
  if(screenshotDir)await page.screenshot({path:path.join(screenshotDir,'mobile-dpp.png')});
  await page.emulateMedia({media:'print'});
  check(await page.locator('main').isVisible(),'Article remains available in print mode');
  check(errors.length===0,'No browser runtime errors: '+errors.join('; '));
  check(requests.length===0,'No network requests are needed to render or read the report');
  console.log(JSON.stringify({artifact,checks:checks.length,routes:data.routes.length,claims:data.claims.length,sources:data.sources.length,errors,networkRequests:requests},null,2));
 } finally {await browser.close();}
})().catch(error=>{console.error(error.stack);process.exitCode=1;});
