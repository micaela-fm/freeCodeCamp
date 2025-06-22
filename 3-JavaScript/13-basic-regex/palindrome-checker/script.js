const input = document.getElementById("text-input");
const checkBtn = document.getElementById("check-btn"); 
const result = document.getElementById("result"); 

const cleanString = input => {
    const nonAlphaNumeric = /[\W_]/g; 
    return input.replace(nonAlphaNumeric, "").toLowerCase(); 
}

const reverseString = cleanInput => cleanInput.split("").reverse().join("")

const isPalindrome = (input) => {
    const cleanInput = cleanString(input); 
    if (cleanInput.length < 1) {
        return false; 
    }
    if (cleanInput.length === 1) {
        return true; 
    }
    const reversedInput = reverseString(cleanInput); 
    return reversedInput === cleanInput; 
}

const checkPalindrome = () => {
    const inputToCheck = input.value.trim();
    if (!inputToCheck) {
        alert("Please input a value");
        return;
    }
    result.innerText = `${inputToCheck} ${isPalindrome(inputToCheck) ? "is" : "is not"} a palindrome`;
}

checkBtn.onclick = checkPalindrome;
