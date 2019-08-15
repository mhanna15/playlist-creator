
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

document.querySelectorAll('.dislike').forEach(element => {
    element.addEventListener('click', event => {
      // addSong(element.parent.previousSibling.firstChild.href)
      deleteSong(element.parentElement.previousElementSibling.previousElementSibling.childNodes[1].href)
      removeRow(element.parentElement.parentElement)
    });
});

function deleteSong(url) {
    fetch('/deletesong', {
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
function removeRow(row) {
    row.parentElement.removeChild(row)
}
// // favorite icon
// function hover(element) {
//     let sign = element.parentNode.id.toLowerCase();
//     let goldStringSign = `../media/gold-png/${sign}-gold.png`;
//     element.setAttribute('src', goldStringSign);
//     element.previousElementSibling.style.textShadow = "#FFDD20 0px 0px 3px";
//   }
  
//   function unhover(element) {
//     let sign = element.parentNode.id.toLowerCase();
//     let stringSign = `../media/png/${sign}.png`;
//     element.setAttribute('src', stringSign);
//     element.previousElementSibling.style.textShadow = "none";
//   }

//   function click(element) {
//     let sign = element.parentNode.id.toLowerCase();
//     let goldStringSign = `../media/gold-png/${sign}-gold.png`;
//     element.setAttribute('src', goldStringSign);
//     element.previousElementSibling.style.textShadow = "#FFDD20 0px 0px 3px";
//   }

// // trash icon
// function hover(element) {
//     let sign = element.parentNode.id.toLowerCase();
//     let goldStringSign = `../media/gold-png/${sign}-gold.png`;
//     element.setAttribute('src', goldStringSign);
//     element.previousElementSibling.style.textShadow = "#FFDD20 0px 0px 3px";
//   }
  
//   function unhover(element) {
//     let sign = element.parentNode.id.toLowerCase();
//     let stringSign = `../media/png/${sign}.png`;
//     element.setAttribute('src', stringSign);
//     element.previousElementSibling.style.textShadow = "none";
//   }

//   function click(element) {
//     let sign = element.parentNode.id.toLowerCase();
//     let goldStringSign = `../media/gold-png/${sign}-gold.png`;
//     element.setAttribute('src', goldStringSign);
//     element.previousElementSibling.style.textShadow = "#FFDD20 0px 0px 3px";
//   }
  