#!/usr/bin/node
const list = require('./100-data').list;
const arry = list.map((x, i) => x * i);

console.log(list);
console.log(arry);
