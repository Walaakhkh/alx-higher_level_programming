#!/usr/bin/node
// Define the add function
function add(a, b) {
  return a + b;
}

// Get the command line arguments excluding the first two elements
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Convert arguments to integers
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

// Print the result of the addition
console.log(add(num1, num2));
