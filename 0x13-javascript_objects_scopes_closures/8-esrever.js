#!/usr/bin/node

exports.esrever = function (list) {
  let list2 = [];
  for (let i = list.length - 1; i >= 0; i--) {
    list2.push(list[i]);
  }
  return (list2);
};
