// Dynamic Field Creation with javascript

const addBtn = document.querySelector(".add")

const input = document.querySelector(".inp-group")

function removeInput(){
    this.parentElement.remove();
}

function addInput(){
    const word = document.createElement("input")
    word.type="text";
    word.placeholder = "Enter a word";
    
    const clue = document.createElement("input");
    clue.type="email";
    clue.placeholder="Enter clue for the word";

    const btn=document.createElement("a");
    btn.className = "delete";
    btn.innerHTML = "-";

    btn.addEventListener("click", removeInput);

    const flex=document.createElement("div");
    flex.className = "flex";

    input.appendChild(flex);
    flex.appendChild(word);
    flex.appendChild(clue);
    flex.appendChild(btn);

}

addBtn.addEventListener("click",addInput);

