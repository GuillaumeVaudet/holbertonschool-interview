#!/usr/bin/env node
// #!/usr/bin/node

const request = require('request');
const MOVIE_ID = Number(process.argv[2]);
const API_URL = `https://swapi-api.hbtn.io/api/films/${MOVIE_ID}`;

if (isNaN(MOVIE_ID)) {
  console.log('Le movie id n\'est pas correct');
  process.exit(1);
}

request(API_URL, function (err, response, body) {
  if (err) return console.error(err);

  const movieData = JSON.parse(body);
  const charactersList = movieData.characters;

  function printCharacter (index) {
    if (index >= charactersList.length) return;

    request(charactersList[index], function (err, response, body) {
      if (err) return console.error(err);

      const charactersData = JSON.parse(body);
      console.log(charactersData.name);

      printCharacter(index + 1);
    });
  }

  printCharacter(0);
});
