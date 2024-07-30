#!/usr/bin/node
/**
 * Counts the number of occurrences of `searchElement` in `list`.
 * @param {Array} list - The array to search within.
 * @param {*} searchElement - The element to count occurrences of.
 * @returns {number} The number of occurrences of `searchElement`.
 */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(element => element === searchElement).length;
};
