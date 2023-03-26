$(document).ready(function() {
    // Set the swipe threshold and direction
    var threshold = 100;
    var direction = "";
  
    // Detect swipe gesture on the page element
    $("#page1").on("touchstart", function(event) {
      var start = event.changedTouches[0].pageX;
      $(this).on("touchmove", function(event) {
        var move = event.changedTouches[0].pageX;
        var distance = move - start;
        if (distance < -threshold) {
          direction = "left";
        } else if (distance > threshold) {
          direction = "right";
        }
      });
      $(this).on("touchend", function() {
        $(this).off("touchmove touchend");
        if (direction == "left") {
          // Animate page1 off-screen and page2 onto the screen
          $("#page1").animate({left: "-100%"}, 500);
          $("#page2").animate({left: "0%"}, 500);
        }
      });
    });
  });

  