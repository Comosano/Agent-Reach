const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:1600},deviceScaleFactor:2});
await p.goto('file://'+__dirname+'/poster.html');await p.waitForTimeout(300);
await p.screenshot({path:__dirname+'/agent-reach-poster.png'});await b.close();})();
