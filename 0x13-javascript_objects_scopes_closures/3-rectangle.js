#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++) {
        str += 'X';
      }
      console.log(str);
      str = '';
    }
  }
}
module.exports = Rectangle;
