/*!
* Start Bootstrap - Clean Blog v6.0.7 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})


//your javascript goes here
var currentTab = 0;
document.addEventListener("DOMContentLoaded", function(event) {


showTab(currentTab);

});

function showTab(n) {
var x = document.getElementsByClassName("tab");
x[n].style.display = "block";
if (n == 0) {
document.getElementById("prevBtn").style.display = "none";
} else {
document.getElementById("prevBtn").style.display = "inline";
}
if (n == (x.length - 1)) {
document.getElementById("nextBtn").innerHTML = "Submit";
} else {
document.getElementById("nextBtn").innerHTML = "Next";
}
fixStepIndicator(n)
}

function hanche(){
    var element = document.getElementById("id_okane");
    element.min="0"
    element.max="1000000";
    element.placeholder="(0~1000000)";
}
hanche();

function nextPrev(n) {
var x = document.getElementsByClassName("tab");

if (n == 1 && !validateForm()) return false;
x[currentTab].style.display = "none";
currentTab = currentTab + n;
if (currentTab >= x.length) {
document.getElementById("regForm").submit();
document.getElementById("nextBtn").style.cssText =" color: rgb(50, 50, 50); background-color: #ffc000; border-color: #ffc000;position: absolute ;top : 22vw ; left : 62.1vw ;width: 8vw;height: 3vw;font-size: 20px;display: flex;justify-content: center;align-items: center;border: 1px solid;border-color: #555454;border-radius:5px;transition: 0.5s;";
return false;
// alert("sdf");
// document.getElementById("nextprevious").style.display = "none";
// document.getElementById("all-steps").style.display = "none";
// document.getElementById("register").style.display = "none";
// document.getElementById("text-message").style.display = "block";


}
showTab(currentTab);
}

function validateForm() {
var element = document.getElementById("id_okane");
var x, y, i,b,c, valid = true;
x = document.getElementsByClassName("tab");
b = x[currentTab].getElementsByClassName("fieldWrapper1");
for(a=0;a<b.length;a++) {
    y = b[a].getElementsByTagName("input");
    for (i = 0; i < y.length; i++) {
        if (y[i].value=="" ) { y[i].className +=" invalid" ; valid=false; y[i].style.background="pink"; } } 
}
for(a=0;a<b.length;a++) {
    c = b[a].getElementsByTagName("select");
    for (i = 0; i < c.length; i++) {
        if (c[i].value=="" ) { c[i].className +=" invalid" ; valid=false; c[i].style.background="pink"; } } 
}
if (element.value>1000000 | element.value<0 ) { element.className +=" invalid" ; valid=false; element.style.background="pink"; } ;

     
if (valid) { document.getElementsByClassName("step")[currentTab].className +=" finish" ; } return valid; }

function fixStepIndicator(n) { var i, x=document.getElementsByClassName("step"); for (i=0; i < x.length; i++) { x[i].className=x[i].className.replace(" active", "" ); } x[n].className +=" active" ; }


// kensakukekkaformmikata
var x = document.getElementById("myDIV1");
var y = document.getElementById("myDIV2");

function myFunction1() {
    x.style.display = "block";
    y.style.display = "none";
  }

function myFunction2() {
x.style.display = "none";
y.style.display = "block";
}
