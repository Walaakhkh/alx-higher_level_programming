#!/usr/bin/node
// Get the command line arguments excluding the first two elements
const args = process.argv.slice(2);

// Check if the first argument exists and print it, otherwise print 'No argument'
console.log(args[0] || 'No argument');
