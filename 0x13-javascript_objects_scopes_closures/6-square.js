#!/usr/bin/node
// Import the Square class from '5-square.js'
const PreviousSquare = require('./5-square');

// Define the new Square class that extends the previous Square class
class Square extends PreviousSquare {
  constructor (size) {
    super(size); // Call the constructor of the parent Square class
  }

  charPrint (c) {
    // Print the square using the character c or 'X' if c is not provided
    const char = c || 'X';
    for (let i = 0; i < this.size; i++) {
      console.log(char.repeat(this.size));
    }
  }
}

module.exports = Square;
