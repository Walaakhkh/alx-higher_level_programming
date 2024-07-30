#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Check if the size is a valid positive number
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Loop to print the square of the given size
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
