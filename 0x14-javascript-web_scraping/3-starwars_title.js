#!/usr/bin/node

const REQ = require('request');
var url = "https://swapi-api.alx-tools.com/api/films/"+process.argv[2];
REQ(url, function (error, response, body){
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
