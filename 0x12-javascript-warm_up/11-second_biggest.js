#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
}
