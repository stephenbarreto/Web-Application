/* eslint-disable */

// when input is focused add focused class for style
function focused(el) {
  el.closest('.input-group').classList.add('is-focused');
}

// when input is focused remove focused class for style
function defocused(el) {
  el.closest('.input-group').classList.remove('is-focused');
}

// check if the input is filled and toggles the 'is-filled' class
// function checkFilled(el) {
//   el.closest('.input-group').classList.toggle('is-filled', el.value && el.value !== "");
// }

export default function setMaterialInput() {
  // Material Design Input function
  let inputList = [...document.querySelectorAll('.input-group .form-control')];

  inputList.forEach(inputEl => {
    // checkFilled(inputEl);

    inputEl.addEventListener('focus', function () {
      focused(this);
    }, false);

    // inputEl.addEventListener('keyup', function () {
    //   checkFilled(this);
    // });

    inputEl.addEventListener('focusout', function () {
      // checkFilled(this);
      defocused(this);
    }, false);
  });
}
