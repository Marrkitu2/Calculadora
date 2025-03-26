let display = document.getElementById('display');
let currentoperation = '' ;
let firstOperand = '';
let secondOperand = '';

function appendNumber(number) {
  display.value += number;
}

function setOperation(operation) {
  firstOperand = display.value;
  currentOperation = operation;
  display.value = '';
}

function calculate() {
  secondOperand = display.value;
  let result;
  switch (currentOperation) {
      case '+':
          result = parseFloat(firstOperand) + parseFloat(secondOperand);
          break;
      case '-':
          result = parseFloat(firstOperand) - parseFloat(secondOperand);
          break;
      case '*':
          result = parseFloat(firstOperand) * parseFloat(secondOperand);
          break;
      case '/':
          result = parseFloat(firstOperand) / parseFloat(secondOperand);
          break;
      case '^':
          result = Math.pow(parseFloat(firstOperand), parseFloat(secondOperand));
          break;
      default:
          return;
  }
  display.value = result;
  currentOperation = '';
  firstOperand = '';
  secondOperand = '';
}

function clearDisplay() {
  display.value = '';
  currentOperation = '';
  firstOperand = '';
  secondOperand = '';
}

function sqrt() {
  display.value = Math.sqrt(parseFloat(display.value));
}

function log() {
  display.value = Math.log(parseFloat(display.value));
}

function sin() {
  display.value = Math.sin(parseFloat(display.value) * Math.PI / 180);
}

function cos() {
  display.value = Math.cos(parseFloat(display.value) * Math.PI / 180);
}

function tan() {
  display.value = Math.tan(parseFloat(display.value) * Math.PI / 180);
}

function factorial() {
  let num = parseInt(display.value);
  let result = 1;
  for (let i = 1; i <= num; i++) {
      result *= i;
  }
  display.value = result;
}

function setMode(mode) {
  const calculator = document.querySelector('.calculator');
  if (mode === 'scientific') {
      calculator.classList.add('scientific-mode');
  } else {
      calculator.classList.remove('scientific-mode');
  }
}
