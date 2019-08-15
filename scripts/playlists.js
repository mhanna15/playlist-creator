
// for (let i=0;i<favorited_songs.length;i++){
//     favorited_songs[i].addEventListener('click', e => addSong)
// }

document.querySelectorAll('.like').forEach(element => {
    element.addEventListener('click', event => {
      // addSong(element.parent.previousSibling.firstChild.href)
      addSong(element.parentElement.previousElementSibling.childNodes[1].href)
    });
});

function addSong(url) {
    fetch('/addsong', {
        method: 'POST',
        body: JSON.stringify({url: url}),
        headers: {
            'Content-Type': 'application/json'
        },
     })
      .then((resp) => resp.text())
      .then(data => {
        console.log(data);
    });

  }