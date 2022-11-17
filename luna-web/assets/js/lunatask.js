const config = {
    apiKey: "AIzaSyA0jC3DUFl4jxjth4vwmbKNzYFLSt1YaVA",
    authDomain: "luna-fdb.firebaseapp.com",
    databaseURL: "https://luna-fdb-default-rtdb.firebaseio.com",
    projectId: "luna-fdb",
    storageBucket: "luna-fdb.appspot.com",
    messagingSenderId: "167131896270",
    appId: "1:167131896270:web:0b524202c8afad005c339f",
    measurementId: "G-282S7D224C"
};


firebase.initializeApp(config);
var database = firebase.database();

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Will work based on lunacore line 130 code - (var parseresult() - last line)
function showcommandinui(commandText) {

    var lunaai = document.getElementById("lunaquestion");
    lunaai.innerText = commandText;

}


function nocommandmatch() {

    var lunaai = document.getElementById("lunaquestion");
    lunaai.innerText = "Sorry , I don't Know That Yet !";
    speakout("Sorry , I don't Know That Yet !");

}


function lunacommands(command) {
    // var lunaai = document.getElementById("lunaai");
    // lunaai.style.visibility = "visible";
    // var lunaai = document.getElementById("lunaresponse");
    // lunaai.innerText = "luna";

    if(command == 'pause')
    {
    luna.pause();
    }
}


function speakout(text) {

    luna.abort();

    var utterance = new SpeechSynthesisUtterance(text);
    var voices = window.speechSynthesis.getVoices();
    utterance.voice = voices.filter(function (voice) { return voice.name == 'Google US English'; })[0];
    window.speechSynthesis.speak(utterance);

    var lunaai = document.getElementById("lunaresponse");
    lunaai.innerText = text;
    luna.start();
}


function currtime() {
    var date = new Date();
    var hours = date.getHours() > 12 ? date.getHours() - 12 : date.getHours();
    var am_pm = date.getHours() >= 12 ? "PM" : "AM";
    hours = hours < 10 ? "0" + hours : hours;
    var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
    var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
    var ctime = hours + ":" + minutes + " " + am_pm;
    console.log(ctime);
    return ctime;
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


var whatcommands = function (command) {

    command = command.toLowerCase();

    if (command == "is the time") {
        var nowtime = currtime();
        speakout("The time is " + nowtime);

    }

    if (command == "is your name") {

        commandout = 'Central AI of Raven Systems ! , Name is Luna !'
        speakout(commandout);

    }

}



var whocommands = function (command) {

    // command.split(" ").includes("up")
    // {
    //     speakout("Nothing Much !")
    // }
    // console.log(command.split(" "))

    if (command == "is up") {
        speakout("Nothing Much !");

    }


    if (command == "created you") {
        speakout("I was coded by Infiniti ! but few of my abilities are from open source!");

    }

    if (command == "are you") {

        commandout = "Hello , I'm Luna ! , Raven Systems Central Controll !";
        speakout(commandout);

    }

}



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


calltask = function (command) {
    // updatetask('call ' + command);
    speakout('Calling ' + command + ' !')
}



function deviceon(device) {
    firebase.database().ref("luna/devices/device4").set(0)
    speakout('Turning on ' + device + ' !')
}



function deviceoff(device) {
    firebase.database().ref("luna/devices/device4").set(1)
    speakout('Turning off ' + device + ' !')
}

