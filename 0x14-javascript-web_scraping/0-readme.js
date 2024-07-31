#!/usr/bin/node

Req = require('request');
Req(process.argv[2], function (error, response, body) {
  console.log(response);
  if (error) {
    console.error('error:', error);
  }
});
