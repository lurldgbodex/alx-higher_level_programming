#!/usr/bin/node
exports.esrever = function (list) {
  const arry = [];
  for (let i = list.length - 1; i >= 0; i--) {
    arry.push(list[i]);
  }
  return (arry);
};
