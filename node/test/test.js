var chai = require('chai');
var expect = chai.expect; // we are using the "expect" style of Chai

const util = require('../src/addTwoNumbers')

// console.log(util.addTwoNumbers(5,4));

describe('src', function() {
  it('this is the desc', function() {
      expect(util.addTwoNumbers(2,3)).to.equal = 6
  });
});
