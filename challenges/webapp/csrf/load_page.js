// Load libs
var system = require('system');
var webPage = require('webpage');
var TIMER_EXIT = 5000;

// Command line arguments
if (system.args.length < 2){
  console.log('Usage: ' + system.args[0] +  ' <Cookie>');
  phantom.exit(1);
} 

var page = webPage.create();
var url = 'https://csrf.webchal.twinpeaks.cs.ucdavis.edu/posts';
var cookie = system.args[1];

console.log("parsed cookie: " + cookie);

phantom.addCookie({
  name: "webchal_csrf_forum_sessid",
  value: cookie,
  domain: "csrf.webchal.twinpeaks.cs.ucdavis.edu",
  secure: false,
  httponly: true,
  path: "/"
});

phantom.addCookie({
  name: "beamsplitter_csrf",
  value: system.env["beamsplitter_cookie"],
  domain: "csrf.webchal.twinpeaks.cs.ucdavis.edu",
  secure: false,
  httponly: true,
  path: "/"
});

phantom.addCookie({
  name: "message",
  value: "Nice_try!_But_this_isn't_a_XSS_challenge_so_try_a_CSRF_attack_instead!",
  domain: "csrf.webchal.twinpeaks.cs.ucdavis.edu",
  secure: false,
  httponly: false,
  path: "/"
});

// Setup web page to handle alert
//page.onAlert = function(msg) {
//  flag = 0;
  //console.log("from alert: " + msg)
//}

//var userCode = 'alert(32)';
//var userCode = system.args[1];
//page.evaluateJavaScript('function() {' + userCode + '}')
//page.open(url, function(status) {
//  if (status !== 'success') {
//    console.log('FAIL to load the address');
//  } else {
//    t = Date.now() - t;
//    console.log('Loading ' + system.args[1]);
//    console.log('Loading time ' + t + ' msec');
//  }
//  phantom.exit();
//});


page.onNavigationRequested = function(newurl, navigationType, navigationLocked, isMainFrame) {
    //page.onNavigationRequested = null;

    console.log('Navigation requested: ' + navigationType + '; ' + newurl);
    console.log('Navigation locked: ' + navigationLocked);
    console.log('nav type: ' + navigationType);
    console.log('ismain: ' + isMainFrame);

};

page.onLoadFinished = function(){
  console.log(page.content);
}

page.open(url, function(status) {
  page.evaluate(function() {
    console.log(document.title);
  });
});

setTimeout(function(){phantom.exit()}, TIMER_EXIT);


//console.log(flag);
