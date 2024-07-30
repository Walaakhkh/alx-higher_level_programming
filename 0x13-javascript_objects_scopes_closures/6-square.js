#!/usr/bin/node
// Import the Square class from 5-square.js
const SquareBase = require('./5-square');

class Square extends SquareBase {
  constructor(size) {
    super(size); // Call the parent constructor
  }

  // Method to print the square with the specified character
  charPrint(c) {
    const char = c || 'X'; // Use 'X' if c is not provided
    for (let i = 0; i < this.size; i++) {
      console.log(char.repeat(this.size)); // Print each row
    }
  }
}

module.exports = Square;
