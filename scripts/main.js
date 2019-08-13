let happy = document.querySelector("#happy");

happy.addEventListener('mouseenter', e => {
  happy.innerHTML = "😃"
});

happy.addEventListener('mouseleave', e => {
  happy.innerHTML = "Happy"
});

let sad = document.querySelector("#sad");

sad.addEventListener('mouseenter', e => {
  sad.innerHTML = "😔"
});

sad.addEventListener('mouseleave', e => {
  sad.innerHTML = "Sad"
});

let angry = document.querySelector("#angry");

angry.addEventListener('mouseenter', e => {
  angry.innerHTML = "😡"
});

angry.addEventListener('mouseleave', e => {
  angry.innerHTML = "Angry"
});
