let happy = document.querySelector("#happy");

happy.addEventListener('mouseenter', e => {
  happy.innerHTML = "😃"
});

happy.addEventListener('mouseleave', e => {
  happy.innerHTML = "Happy"
});
