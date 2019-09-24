var chai = require('chai');
var expect = chai.expect; // we are using the "expect" style of Chai
var src = require('../src/addTwoNumbers');

describe('src', function() {
  it('this is the desc', function() {
      let actual = addTwoNumbers()
      expect(src.addTwoNumbers(2,3)).to.equal = 6
  });
});