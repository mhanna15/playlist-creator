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

let romantic = document.querySelector("#romantic");

romantic.addEventListener('mouseenter', e => {
  romantic.innerHTML = "😘"
});

romantic.addEventListener('mouseleave', e => {
  romantic.innerHTML = "Romantic"
});

let lonely = document.querySelector("#lonely");

lonely.addEventListener('mouseenter', e => {
  lonely.innerHTML = "😞"
});

lonely.addEventListener('mouseleave', e => {
  lonely.innerHTML = "Lonely"
});

let hype = document.querySelector("#hype");

hype.addEventListener('mouseenter', e => {
  hype.innerHTML = "🤪"
});

hype.addEventListener('mouseleave', e => {
  hype.innerHTML = "Hype"
});
