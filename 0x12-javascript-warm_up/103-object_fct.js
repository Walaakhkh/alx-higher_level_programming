#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value += 1;
  }
};

console.log(myObject);

// Define an anonymous function for incr
myObject.incr = function () {
  this.value += 1;
};

// Use the incr function to increment the value
myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
