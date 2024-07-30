#!/usr/bin/node
// Get the command line arguments excluding the first two elements
const args = process.argv.slice(2);

// Determine the output message based on the number of arguments
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
