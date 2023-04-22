let margin = 250;

$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
    $("#content").css("margin-left", `${margin}px`);
    $(".white-section").css("margin-left", `${margin}px`);
    margin = 250 - margin;
  });
});

const FollowButton = document.querySelector(".follow-button");

FollowButton.addEventListener("click", (e) => followunfollow(e.target));

function followunfollow(button) {
  button.classList.toggle("followed");

  
  if (button.innerText === "Follow") {
    button.innerText = "Unfollow";
  } else {
    button.innerText = "Follow";
  }
}
