#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (err, res, characterBody) => {
        if (err) {
          console.error(err);
        } else if (res.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.log('Error: Unable to fetch data');
  }
});
