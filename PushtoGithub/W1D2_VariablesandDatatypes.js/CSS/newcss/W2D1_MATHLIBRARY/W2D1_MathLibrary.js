function d6() {
    var roll = Math.random();
    // your code here
    roll = Math.ceil(6*roll)
    //your code ends
    return roll;
}
    
var playerRoll = d6();
console.log("The player rolled: " + playerRoll);


var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];
//0 to 19
var roll = Math.random();
roll = Math.floor(19*roll)+ 1;
console.log(lifesAnswers[roll]);

roll = Math.ceil(19*roll);
roll = roll =1;