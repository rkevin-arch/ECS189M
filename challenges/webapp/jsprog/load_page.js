// Load libs
var system = require('system');
var webPage = require('webpage');
var TIMER_EXIT = 10000;

// Command line arguments
if (system.args.length < 2){
  console.log('Usage: ' + system.args[0] +  ' <js code to test>');
  phantom.exit(1);
}

var page = webPage.create();
var url = 'http://localhost:8080/reflect';

//page.onLoadFinished = function(){
//  console.log(page.content);
//}

page.onConsoleMessage = function(msg) {
    console.log(msg);
};

setTimeout(function(){
    console.log("WARNING: Your code has timed out! Check for infinite loops or other nasty stuff in your code!");
    phantom.exit();}, TIMER_EXIT);

page.open(url, function(status) {
    if(status!=="success"){
        console.log("Load internal reflect page failed! This should never happen. Contact Kevin.");
        phantom.exit();
    }
    page.evaluate(function(jscode) {
        try{
            console.log("Evaluating your code...")
            eval(jscode);
            console.log("Starting to grade your code...")
            if(add(1,1)!==2){
                console.log("add(1,1) is not 2! Exiting.")
                return;
            }
            if(add(1,2)!==3){
                console.log("add(1,2) is not 3! Exiting.")
                return;
            }
            if(add(12345,67890)!==80235){
                console.log("add(12345,67890) is not 80235! Exiting.")
                return;
            }
            console.log("The add function passed all tests!");
            console.log("Now trying to visit the page with the flag with your visit function...");
            console.log("Your function returned: "+visit("/flag"));
            console.log("All done!")
        } catch(e) {
            console.log("There is an error when testing your code!");
            console.log(e.message);
        }
    }, system.args[1]);
    phantom.exit();
});
