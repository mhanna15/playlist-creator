document.querySelectorAll('.dislike').forEach(element => {
    element.addEventListener('click', event => {
      // addSong(element.parent.previousSibling.firstChild.href)
      console.log(element.parentElement)
      deleteSong(element.parentElement.previousElementSibling.childNodes[1].href)
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