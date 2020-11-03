const addButton = document.querySelector("button");
const inputOne = document.getElementById("num1")! as HTMLInputElement;
const inputTwo = document.getElementById("num2")! as HTMLInputElement;

function addNumbers (num1: number, num2: number) {
    return num1 + num2;
}

addButton.addEventListener("click", function() {
    console.log(addNumbers(+inputOne.value, +inputTwo.value));
});