// This is javascript code that adds the class "scroll-top" to the body whenever the body is at the top of the page and removes it otherwise.

window.onscroll = onScroll;

function onScroll() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.body.classList.remove("scroll-top");
  } else {
    document.body.classList.add("scroll-top");
  }
}

$(document).ready(function() {
  $('#gg').click(function() {
    checked = $("input[type=checkbox]:checked").length;

    if (!checked) {
      alert("You must check at least one Model.");
      return false;
    }
  });
});

function TestsFunction() {

  if (document.getElementById('demo').checked || document.getElementById('demo2').checked) {


    var T = document.getElementById("gg");

    if (window.innerWidth <= 415) {
      T.style.display = "none";

      var N = document.getElementById("wait_text");
      N.style.position = "relative";
      N.style.left = "20px";
    }

    else if (window.innerWidth <= 1180) {
      T.style.marginLeft = "-40vw";

      var N = document.getElementById("wait_text");
      N.style.position = "relative";
      N.style.top = "-40px";
      N.style.left = "45px";

      var Z = document.getElementById("loader");
      Z.style.position = "relative";
      Z.style.top = "-40px";
      Z.style.left = "45px";
    }

    else {
      T.style.marginLeft = "-40vw";

      var N = document.getElementById("wait_text");
      N.style.position = "relative";
      N.style.top = "-40px";
      N.style.left = "25px";

      var Z = document.getElementById("loader");
      Z.style.position = "relative";
      Z.style.top = "-40px";
      Z.style.left = "25px";
    }


    var Y = document.getElementById("hide");
    Y.style.display = "block";  // <-- Set it to block
  }
  else {
    return false;
  }
}
