// This is javascript code that adds the class "scroll-top" to the body whenever the body is at the top of the page and removes it otherwise.

window.onscroll = onScroll;

function onScroll() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.body.classList.remove("scroll-top");
  } else {
    document.body.classList.add("scroll-top");
  }
}
var I = document.getElementById("m_info_btn");
if (window.innerWidth <= 385) {
  I.style.position = "relative";
  I.style.top = "-35px";
  I.style.right = "-100px";

}
else if (window.innerWidth <= 390) {
  I.style.position = "relative";
  I.style.right = "-110px";
}

else if (window.innerHeight <= 882) {
  I.style.position = "relative";
  I.style.top = "-10px";

}



if (window.innerWidth >= 750) {//larger screens get different dimensions of background of prediction
  var Z = document.getElementById("prediction");
  Z.style.height = "30vh";
  Z.style.top = "-100px";
}

function Test(perf_m, perf_w, perf_d, month_pred, week_pred, day_pred){
  //month icon setter
  if (perf_m == 'Underperformed') {
    //we dont do anything bc its already set
  }
  else if (perf_m == 'Outperformed' && month_pred == 'Buy') { //if buy
    document.getElementById("month_icon").classList.remove('bi-slash-circle');
    document.getElementById("month_icon").classList.add('bi-arrow-up');
    document.getElementById("month_icon").style.color = "limegreen";
  }
  else {//if sell
    document.getElementById("month_icon").classList.remove('bi-slash-circle');
    document.getElementById("month_icon").classList.add('bi-arrow-down');
    document.getElementById("month_icon").style.color = "red";
  }

  //week icon setter
  if (perf_w == 'Underperformed') {
    document.getElementById("week_icon").classList.remove('bi-arrow-up');
    document.getElementById("week_icon").classList.add('bi-slash-circle');
    document.getElementById("week_icon").style.color = "gray";
  }
  else if (perf_w == 'Outperformed' && week_pred == 'Buy') { //if buy
    //already set
  }
  else {//if sell
    document.getElementById("week_icon").classList.remove('bi-arrow-up');
    document.getElementById("week_icon").classList.add('bi-arrow-down');
    document.getElementById("week_icon").style.color = "red";
  }

  //day icon setter
  if (perf_d == 'Underperformed') {
    document.getElementById("day_icon").classList.remove('bi-arrow-down');
    document.getElementById("day_icon").classList.add('bi-slash-circle');
    document.getElementById("day_icon").style.color = "gray";
  }
  else if (perf_d == 'Outperformed' && day_pred == 'Buy') { //if buy
    document.getElementById("day_icon").classList.remove('bi-arrow-down');
    document.getElementById("day_icon").classList.add('bi-arrow-up');
    document.getElementById("day_icon").style.color = "limegreen";
  }
  else {//if sell
    //already set
  }

}


var clicked = false;
function my_own() {
  if (clicked == false) {
    var Z = document.getElementById("more_info");

    if (window.innerWidth <= 385) {
      Z.style.position = "relative";
      Z.style.top = "-40px";
      Z.style.display = "block";
      document.getElementById("icon").classList.remove('bi-chevron-bar-down');
      document.getElementById("icon").classList.add('bi-arrow-bar-up');
      clicked = true;
    }
    else {
      Z.style.position = "relative";
      Z.style.top = "50px";
      Z.style.display = "block";
      document.getElementById("icon").classList.remove('bi-chevron-bar-down');
      document.getElementById("icon").classList.add('bi-arrow-bar-up');
      clicked = true;
    }
  }
  else {
    var Z = document.getElementById("more_info");
    Z.style.position = "relative";
    Z.style.top = "-210px";
    Z.style.display = "block";
    document.getElementById("icon").classList.add('bi-chevron-bar-down');
    document.getElementById("icon").classList.remove('bi-arrow-bar-up');
    clicked = false;
  }

}