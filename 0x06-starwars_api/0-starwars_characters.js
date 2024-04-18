#!/usr/bin/node


const request = require('request');

function stwCharacters(filmId) {
  const mainUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`

  request(mainUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      } else if (response.statusCode !== 200) {
        console.error('Status:', response.statusCode);
      } else {
        const filmData = JSON.parse(body);
        filmData.characters.forEach(charUrl => {
          request(charUrl, (error, response, body) => {
            if (error) {
              console.error('Error:', error);
            } else if (response.statusCode !== 200) {
              console.error('Status:', response.statusCode);
            } else {
              const charData = JSON.parse(body);
              console.log(charData.name);
            }
          });
        });
      }
  });
}


const filmId = process.argv[2]
if (filmId) {
	stwCharacters(filmId);
}
