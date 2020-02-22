// Main app for subtract microservice in Javascript //

'use strict';

// Import JS dependancies
const express = require('express');

// Microservice able to run from anywhere on port 80
const PORT = 80;
const HOST = '0.0.0.0';

//import main subtract function
var sub = require('./subtract');

//main microservice function
const app = express();
app.get('/', (req,res) => {

    var output = {
        'error': false,
        'string': '',
        'answer': 0
    };

    //implement CORS
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*')

    //get header parameters
    var x = req.query.x;
    var y = req.query.y;

    //call subtrac function
    var answer = sub.subtract(x,y);

    //convert result into string
    output.string = x + '-' + y + '=' + answer;
    output.answer = answer;

    //format string into JSON object
    res.end(JSON.stringify(output));
});

app.listen(PORT, HOST);
