//JS 90s way to make websites interactive node to interact outside websites
//""= string var - variable all languages have keywords that perform actions ex var

var myName = "Matt Morris";

// JS name rules
/*
JS Name rules 
Cannot use reserved keywords
cannot have hyphends/spaces
cannot start with number
can contain number
predict the outcome / loops
suggested naming comvention is camel case 


JavaScript Datatpes
-- primitive datatypes
--strings: strings of characters delimited by quotation marks
*/

var myString = "";''

var question = "will he or won't he"
//numbers - integers (whole numbers) and decimal numbers
var timeOfDay = 928;
var percentage = .50;
//booleans - true or false
var isOld = true;
// null and undefined
// null is usually intentional value while undefined is unintentional 

//only necessary to use var keyword when instantiating or creating a variable
var a = 25;
a = a - 13; a = 12
//console log means print
console.log(a/2); // --> 6
    
a = "hello";
console.log(a + " hello");//6 , hello hello


//variables values
//a          25
//a          12

//predict loops
// keep our code dry = Dont Repeat Yourself
//four things to create loop
//1. a named sentry to do our bidding
//2. where the sentry starts
//3.where or how sentry ends
//4.how the sentry ends

for (var i = 1; i<=10; i = i + 1) i++{
//code block for the loop
    console.log(i);
}
console.log("Final value of i is:",i); // --> 11    
for(var i=0; i<10; i++) {
    console.log(i);
    i = i + 3; 
}
    
console.log("outside of the loop " + i);


