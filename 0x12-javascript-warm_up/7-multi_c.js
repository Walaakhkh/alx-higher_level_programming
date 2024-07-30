#!/usr/bin/node
// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer
const x = parseInt(arg);

// Check if the conversion was successful and if x is greater than 0
if (isNaN(x) || x <= 0) {
  console.log('Missing number of occurrences');
} else {
  // Loop x times to print "C is fun"
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
