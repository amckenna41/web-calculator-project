
# Testing functions for multiply microservice #

#import testing modules and dependancies
import unittest
import mult
from flask import Flask
from flask import request
import urllib.request
import json
from urllib.request import urlopen
#import urllib

#testing class for multiply function
class test_mult(unittest.TestCase):

    #test if correct result is produced when two x and y values are inputted into multiply function
    def test_mult_result(self):

        result = mult.multiply(10, 5)
        self.assertEqual(result, 50)

        result = mult.multiply(4, 8)
        self.assertEqual(result, 32)

        result = mult.multiply(2, 32)
        self.assertEqual(result, 64)

        result = mult.multiply(10, 3)
        self.assertNotEqual(result, 123)

        result = mult.multiply(10, 3)
        self.assertNotEqual(result, 123)

        result = mult.multiply(45, 4)
        self.assertNotEqual(result, 6)

        result = mult.multiply(6, 72)
        self.assertNotEqual(result, 49)

    #test if result produced from function is of the desired data type
    def test_mult_type(self):

        result = mult.multiply(30, 4)
        self.assertIsInstance(result ,int)

        result = mult.multiply(2, 6)
        self.assertIsInstance(result ,int)

        result = mult.multiply(2, 6.5)
        self.assertFalse(type(result) is int)

        result = mult.multiply(100, 'trump2020')
        self.assertFalse(type(result) is int)

        result = mult.multiply(2, 'kanye2020')
        self.assertFalse(type(result) is int)

    #testing multiplcation endpoints
    def test_mult_endpoint(self):

        #testing result is equal to http output
        result = mult.multiply(2,2)
        http_output = "http://mult.40175607.qpc.hal.davecutting.uk/?x=2&y=2"
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        http_result = json_data["answer"]
        self.assertEqual(result, http_result)

        result = mult.multiply(14,4)
        http_output = "http://mult.40175607.qpc.hal.davecutting.uk/?x=14&y=4"
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        http_result = json_data['answer']
        self.assertEqual(result, http_result)

        result = mult.multiply(21,3)
        http_output = "http://mult.40175607.qpc.hal.davecutting.uk/?x=21&y=3"
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        http_result = json_data['answer']
        self.assertEqual(result, http_result)

        #testing result is not equal to http output
        result = mult.multiply(444,2)
        http_output = "http://mult.40175607.qpc.hal.davecutting.uk/?x=55&y=2"
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        http_result = json_data['answer']
        self.assertNotEqual(result, http_result)

        result = mult.multiply(29,3)
        http_output = "http://mult.40175607.qpc.hal.davecutting.uk/?x=4&y=1"
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        http_result = json_data['answer']
        self.assertNotEqual(result, http_result)

        result = mult.multiply(31,9)
        http_output = "http://mult.40175607.qpc.hal.davecutting.uk/?x=17&y=89"
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        http_result = json_data['answer']
        self.assertNotEqual(result, http_result)

#main function to call unit tests
if __name__ =='__main__':
    unit_test.main()
