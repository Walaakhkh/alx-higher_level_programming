#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const x = parseInt(arg);

// Check if the argument is a valid number and greater than zero
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  // Loop x times to print "C is fun"
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
