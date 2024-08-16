#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
  /**
   * Prints the square using the character `c`.
   * If `c` is not provided, defaults to 'X'.
   * 
   * @param {string} [c='X'] - The character to print the square with.
   */
  charPrint(c) {
    const char = c || 'X'; // Default to 'X' if no character is provided
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
