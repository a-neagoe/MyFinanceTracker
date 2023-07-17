var myInput = document.getElementById("passInput");
var myInput2 = document.getElementById("passConfirm");
var spaces = document.getElementById("spaces");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var special = document.getElementById("special");
var confirmation = document.getElementById("password-does-not-match-text")
var register = document.getElementById("submitBtn")
var username = document.getElementById("usernameReg")


username.onkeyup = function() {
    var spc = ' ';
    if (!username.value.match(spc) && username.value.length > 3) {
        username.classList.add("custom-select", "is-valid")
    } else {
        username.classList.remove("custom-select", "is-valid")
    }
}


// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
    document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
    document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
    // Validate lowercase letters
    var Spaces = ' ';
    if (myInput.value.match(Spaces)) {
        spaces.classList.remove("valid");
        spaces.classList.add("invalid");
    } else {
        spaces.classList.remove("invalid");
        spaces.classList.add("valid");
    }

    // Validate capital letters
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
        capital.classList.remove("invalid");
        capital.classList.add("valid");
    } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
    }

    // Validate numbers
    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers)) {
        number.classList.remove("invalid");
        number.classList.add("valid");
    } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
    }

    // Validate length
    if (myInput.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
    }

    // Validate numbers
    var specialChars = /[#?!@$%^&*-]/g;
    if (myInput.value.match(specialChars)) {
        special.classList.remove("invalid");
        special.classList.add("valid");
    } else {
        special.classList.remove("valid");
        special.classList.add("invalid");
    }

    if (!myInput.value.match(Spaces) && myInput.value.match(upperCaseLetters) && myInput.value.match(numbers) && myInput.value.length >= 8 && myInput.value.match(specialChars)) {
        myInput.classList.add("custom-select", "is-valid")
    } else {
        myInput.classList.remove("custom-select", "is-valid")
    }
}


myInput2.onkeyup = function() {
    if (myInput2.value == myInput.value) {
        myInput2.classList.add("custom-select", "is-valid")
        register.disabled = false;
    } else {
        myInput2.classList.remove("custom-select", "is-valid")
        register.disabled = true
    }
}