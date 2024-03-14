#!/usr/bin/node 

function fact (a) {
  if (a === 1 || isNaN(a)) {
    return (1);
  } else {
    return (a * fact (a-1));
  }
}
console.log(fact(Number(process.argv[2])));
