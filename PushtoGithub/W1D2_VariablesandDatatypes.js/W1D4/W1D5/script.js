//html structure
//css style
//javascript functionality

//The document object model
//what is the DOM?
//the dom is our page as an object

//

//alert("this is coming from script.js")

//console.dir(this);

var title = document.querySelector('#title');
console.log(title);
title.innerHTML = 'This is an example'

function disappear(element){
    element.remove();
}
//manipulating the DOM