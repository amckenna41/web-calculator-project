
// Testing for subtract microservice in JS //

//import JS dependancies and chai testing framework
var expect  = require('chai').expect;
var sub = require('../subtract');

it('Subtraction Test', function(done) {
        var x = 10;
        var y = 5;
        var a = x-y;
        expect(sub.subtract(x,y)).to.equal(a);

        var x = 102;
        var y = 40;
        var a = x-y;
        expect(sub.subtract(x,y)).to.equal(a);

        var x = 30;
        var y = 12;
        var a = x-y;
        expect(sub.subtract(x,y)).to.equal(a);

        var x = 387;
        var y = 126;
        var a = x-y;
        expect(sub.subtract(x,y)).to.equal(a);

        done();
});
