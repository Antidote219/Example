var title = document.querySelector('#title');
var box = document.getElementById('box');
//console.log(box)
var counter = 0;
box.innerText


function display(element){
    console.log(element.innerText);
}

function changeText(element){
    element.innerText = "You Clicked Me"
}
function changeBg(element){
//element.style    
    title.style.backgroundColor = "green"
}
function hoverOver(element){
    element.style.backgroundColor = "purple"
}

function hoverOut(element){
    element.style.backgroundColor = "blue"
}

function increment(){
    counter++
    box.innerText = counter;
}