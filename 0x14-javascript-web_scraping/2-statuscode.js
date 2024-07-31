#!/usr/bin/node

const REQ = require('require');
REQ(process.argv[2], process.argv[3], 'utf8', (error,response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
