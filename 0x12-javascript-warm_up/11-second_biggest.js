#!/usr/bin/node
// Get all arguments except the first two (node executable and script name)
const args = process.argv.slice(2);

// Convert arguments to integers
const numbers = args.map(arg => parseInt(arg));

// Function to find the second largest number
function findSecondBiggest(nums) {
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const num of nums) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }

  return secondLargest === -Infinity ? 0 : secondLargest;
}

// Compute and print the second biggest integer
if (numbers.length < 2) {
  console.log(0);
} else {
  console.log(findSecondBiggest(numbers));
}
