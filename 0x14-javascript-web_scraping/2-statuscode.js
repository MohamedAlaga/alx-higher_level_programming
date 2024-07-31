#!/usr/bin/node

const REQ = require('request');
REQ(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
