
# Tests for modulus microservice in Python #

#import python modules for testing
import unittest
import mod
import urllib.request
import json
from urllib.request import urlopen
from flask import Flask
from flask import request

#test class for mod function
class test_mod(unittest.TestCase):

    #test if the correct result is produced from two inputted values
    def test_mult_result(self):

        result = mod.mod(10, 4)
        self.assertEqual(result, 2)

        result = mod.mod(20, 8)
        self.assertEqual(result, 4)

        result = mod.mod(30, 11)
        self.assertEqual(result, 8)

        result = mod.mod(10, 3)
        self.assertNotEqual(result, 5)

        result = mod.mod(14, 3)
        self.assertNotEqual(result, 35)

        result = mod.mod(45, 4)
        self.assertNotEqual(result, 2)

        result = mod.mod(120, 25)
        self.assertNotEqual(result, 6)

    #test if the result data type is an instance of int or not
    def test_mod_type(self):

        result = mod.mod(30, 4)
        self.assertIsInstance(result ,int)

        result = mod.mod(10, 6)
        self.assertIsInstance(result ,int)

        result = mod.mod(12, 6.5)
        self.assertFalse(type(result) is int)

        result = mod.mod(100, 2.5)
        self.assertFalse(type(result) is int)

        result = mod.mod(10, 1.5)
        self.assertFalse(type(result) is int)

    #test the modulus function url to see if it produces the expected_result
    def test_endpoint(self):

        #assign the x, y and modulus url variables
        x_arg = '?x='
        y_arg = '&y='
        modURL = 'http://mod.40175607.qpc.hal.davecutting.uk/' #internal private cloud endpoint

        #set the x and y values and the expected result from their mod calculation
        x_string = '100'
        y_string = '11'
        expected_result = mod.mod(100,11)

        #combine the above variables into one url string
        http_output = modURL + x_arg + x_string + y_arg + y_string

        #use the urllib module to call the mod url and parse the result value from the json object
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']

        #assert that the produced result == expected_result
        self.assertEqual(result, expected_result)

        x_string = '10'
        y_string = '6'
        expected_result = mod.mod(10, 6)
        http_output = modURL + x_arg + x_string + y_arg + y_string

        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']

        self.assertEqual(result, expected_result)

        x_string = '39'
        y_string = '26'
        expected_result = mod.mod(39,26)
        http_output = modURL + x_arg + x_string + y_arg + y_string

        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']

        self.assertEqual(result, expected_result)

        x_string = '59'
        y_string = '3'
        expected_result = mod.mod(59,14)
        http_output = modURL + x_arg + x_string + y_arg + y_string

        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']

        self.assertNotEqual(result, expected_result)

        x_string = '400'
        y_string = '9'
        expected_result = mod.mod(400,21)
        http_output = modURL + x_arg + x_string + y_arg + y_string

        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']

        self.assertNotEqual(result, expected_result)

        x_string = '22'
        y_string = '10'
        expected_result = mod.mod(22,8)
        http_output = modURL + x_arg + x_string + y_arg + y_string

        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']

        self.assertNotEqual(result, expected_result)

#main function to call unit tests
if __name__ =='__main__':
    unittest.main()
