#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let char = '';
  for (let y = 0; y < process.argv[2]; y++) {
    char += '*';
  }
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(char);
  }
}
