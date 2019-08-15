const DELAY = 500;

function layoutTitle() {
  const instru = document.querySelector("#instru")
  const mental = document.querySelector("#mental")
  const instruString = "Instru"
  // const mentalString = "mental"

  spellout(instru, instruString, 0)
  // spellout(mental, mentalString, (DELAY * instruString.length))
}

function spellout(element, string, startDelay) {
  for (let i in string) {
    const char = string[i]
    function addChar() {
      element.textContent = element.textContent + char;
    }
    setTimeout(addChar, startDelay + (DELAY * i))
  }
}



window.onload = function() {
  layoutTitle()
}
