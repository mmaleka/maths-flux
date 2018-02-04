function openNav() {
    console.log("Open Nav")
    document.getElementById("mySidenav2").style.width = "80%";
}


//document.getElementById("learn").style.width = "100%";

function closeNav() {
    document.getElementById("mySidenav2").style.width = "0";
}


var userNameHint = document.getElementById("hint_id_username")

if (userNameHint){
    userNameHint.remove();
    var regParent = document.getElementById("div_id_password1").getElementsByTagName("ul")[0];
    var Child1 = regParent.getElementsByTagName("li")[0];
    Child1.remove()
    var Child3 = regParent.getElementsByTagName("li")[1];
    Child3.remove()
}

var formRows = document.getElementsByClassName("textarea form-control")[0];

if (formRows){
    formRows.setAttribute("rows", 3);
}



var close = document.getElementsByClassName("closebtn");
console.log(close[0])

if (close[0]){
    close[0].onclick = function(){
        var div = this.parentElement;
        div.style.opacity = "0";
        setTimeout(function(){ div.style.display = "none"; }, 600);
    }
}

var facebook = document.getElementById("facebook")
if (facebook){
    facebook.onclick = function(){
        alert("Coming soon")
    }
}

var twitter = document.getElementById("twitter")
if (twitter){
    twitter.onclick = function(){
        alert("Coming soon")
    }
}

var linkedin = document.getElementById("linkedin")
if (linkedin){
    linkedin.onclick = function(){
        alert("Coming soon")
    }
}

var youtube = document.getElementById("youtube")
if (youtube){
    youtube.onclick = function(){
        alert("Coming soon")
    }
}





var x = screen.width;
if (x <= 700){
    var _submit = document.getElementById("submit");
    if (_submit){
        _submit.classList.add("btn-block");
    };
    var d = document.getElementById("ask_question");
    if(d){
        d.classList.add("btn-block");
    };
} else {

    var _submit = document.getElementById("submit");
    if (_submit){
        _submit.classList.remove("btn-block");
    };
    var d = document.getElementById("ask_question");
    if(d){
        d.classList.remove("btn-block");
    };

}


























