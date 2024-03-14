#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let y = 0; y < process.argv[2]; y++) {
      console.log('*');
    }
    console.log('\n');
  }
}
