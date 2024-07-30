#!/usr/bin/node
// Define the recursive factorial function
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial (n - 1);
}

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Compute and print the factorial
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial (num));
}
