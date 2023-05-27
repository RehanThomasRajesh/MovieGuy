new Card({
    form: 'form',
    container: '.card',
    formSelectors: {
      numberInput: 'input[name=number]',
      expiryInput: 'input[name=expiry]',
      cvcInput: 'input[name=cvv]',
      nameInput: 'input[name=name]'
    },
  
    width: 390, // optional — default 350px
    formatting: true,
  
    placeholders: {
      number: '•••• •••• •••• ••••',
      name: 'Full Name',
      expiry: '••/••',
      cvc: '•••'
    }
  })
  const cardNumberInput = document.getElementById("card-number");
const cardNumberError = document.getElementById("card-number-error");

cardNumberInput.addEventListener("input", function (event) {
  if (cardNumberInput.validity.patternMismatch) {
    cardNumberError.textContent = "Please enter a valid 15-digit card number";
  } else {
    cardNumberError.textContent = "";
  }
});

function phonenumber(inputtxt)
{
  var phoneno = /^\d{10}$/;
  if(inputtxt.value.match(phoneno))
  {
      return true;
  }
  else
  {
     alert("Not a valid Phone Number");
     return false;
  }
  }
