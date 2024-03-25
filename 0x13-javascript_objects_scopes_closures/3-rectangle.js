#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof w === 'number' && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let eof = '';
      for (let j = 0; j < this.width; j++) {
        eof += 'X';
      }
      console.log(eof);
    }
  }
}
module.exports = Rectangle;
