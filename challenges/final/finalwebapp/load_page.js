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
var url = 'https://finalwebapp.webchal.twinpeaks.cs.ucdavis.edu/plans';
var cookie = system.args[1];

console.log("parsed cookie: " + cookie);

phantom.addCookie({
  name: "webchal_final_sessid",
  value: cookie,
  domain: "finalwebapp.webchal.twinpeaks.cs.ucdavis.edu",
  secure: false,
  httponly: false,
  path: "/"
});

phantom.addCookie({
  name: "beamsplitter_finalwebapp",
  value: system.env["beamsplitter_cookie"],
  domain: "finalwebapp.webchal.twinpeaks.cs.ucdavis.edu",
  secure: false,
  httponly: true,
  path: "/"
});

page.open(url, function(status) {
  page.evaluate(function() {
    console.log(document.title);
  });
});

setTimeout(function(){phantom.exit()}, TIMER_EXIT);
