#!/usr/bin/node

const REQ = require('request');
const url = process.argv[2];
REQ(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  let count = 0;
  for (const film of JSON.parse(body).results) {
    const characters = film.characters;
    for (const character of characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
