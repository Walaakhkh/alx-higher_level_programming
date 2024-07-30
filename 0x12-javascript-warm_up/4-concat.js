#!/usr/bin/node
// Get the command line arguments excluding the first two elements
const args = process.argv.slice(2);

// Print the arguments in the desired format
console.log(`${args[0]} is ${args[1]}`);
