#!/usr/bin/node

const Sqr = require('./5-square');
class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) {
        c = 'X';
    }
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++) {
        str += c;
      }
      console.log(str);
      str = '';
    }
  }
}
module.exports = Square;
