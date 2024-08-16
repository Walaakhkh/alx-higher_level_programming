#!/usr/bin/node

class Square {
  /**
   * Initializes the square with a given size.
   * 
   * @param {number} size - The size of the square.
   */
  constructor(size) {
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
