var addButton = document.querySelector("button");
var inputOne = document.getElementById("num1");
var inputTwo = document.getElementById("num2");
function addNumbers(num1, num2) {
    return num1 + num2;
}
addButton.addEventListener("click", function () {
    console.log(addNumbers(+inputOne.value, +inputTwo.value));
});
