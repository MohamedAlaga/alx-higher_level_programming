#!/usr/bin/node

const REQ = require('request');
var url = process.argv[2];
REQ(url, function (error, response, body){
  if (error) {
    console.log(error);
    return;
  }
  var count = 0;
  for (let film of JSON.parse(body).results) {
    let characters = film.characters;
    for (let character of characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});