function passwordChecker(password) {
  const lengthError = "Password must be at least 8 characters long.";
  const complexityError = "Password must contain at least 1 lowercase letter, 1 uppercase letter, 1 digit and 1 special character.";
  const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  
  if (password.length < 8) {
    return lengthError;
  } else if (!regex.test(password)) {
    return complexityError;
  } else {
    return "Password is valid.";
  }
}

const password = prompt("Enter a password: ");
console.log(passwordChecker(password));
