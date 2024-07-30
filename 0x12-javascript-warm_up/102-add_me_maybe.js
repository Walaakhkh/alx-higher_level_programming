#!/usr/bin/node
// Define the addMeMaybe function
function addMeMaybe (number, theFunction) {
  // Increment the number
  const incrementedNumber = number + 1;
  // Call the provided function with the incremented number
  theFunction(incrementedNumber);
}

// Export the function to make it visible from outside
module.exports = { addMeMaybe };
