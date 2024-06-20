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

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
