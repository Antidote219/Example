var beatles = ['Paul', 'George', 'John', 'Ringo'];// globally scoped because beatles is declared inside the file but not inside of any function
console.log(beatles)

//functions will create their own scope, if something is declared inside of a function, it is only available inside that function
// loops also create their own scope- blocked scope unless you declare the variable using var 
// function test(){
//     var goat = 

// }
// function printNames(names) {

//     function actuallyPrintingNames() {
//     for (var index = 0; index < names.length; index++) {
//       var name = names[index];
  
//       console.log(name + ' was found at index ' + index);
//     }
//     console.log('name and index after loop is ' + name + ':' + index);
//   }
//   actuallyPrintingNames();
// }
// printNames(beatles);
                     
//difference between let vs var vs const

//var is limited only by the func scope
//let is limited bt the func scope and BLOCK scope (loops and conditionals)
//const is used to declare variable that you dont want any other part of the code to reassign that variable