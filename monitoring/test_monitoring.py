
# Tests for monitoring microservice for web-calculator in Python #

#import testing modules and dependancies
import unittest
import random
from flask import Flask
from flask import request
import urllib.request
import func_url as fu
import json
import requests
from urllib.request import urlopen


#initialise function url's from func_url file
addURL = fu.ADD_URL
multURL = fu.MULT_URL
divURL = fu.DIV_URL
modURL = fu.MOD_URL
powerURL = fu.POWER_URL
subURL = fu.SUB_URL

#test class tests each function with random Values
#test passes if expected result of calculation matches one returned from function url
class test_mult(unittest.TestCase):


    #function to test multiply function
    def test_mult_result(self):

        x_arg = '?x='
        y_arg = '&y='

        #generate random number between 1 and 100 for x and y variables
        x = random.randrange(100)
        y = random.randrange(100)
        expected_result = x *y

        #convert x and y to strings so they can be passed to url
        x_string = str(x)
        y_string = str(y)

        #call function from mult url and pass in parameters and parse result into JSON
        func_url = multURL + x_arg + x_string + y_arg + y_string
        url_output = urlopen(func_url)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']

        #test result from function url matches expected output
        self.assertEqual(result, expected_result)

    #function to test divide function
    def test_div_result(self):

        x_arg = '?x='
        y_arg = '&y='

        #generate random number between 1 and 100 for x and y variables
        x = random.randrange(100)
        y = random.randrange(100)

        #validation to ensure x is > y and y is not equal to 0
        while (x < y) or (y == 0):
            x = random.randrange(100)           #generate random values again if while statement is true
            y = random.randrange(100)

        expected_result = int(x / y)

        #convert x and y to strings so they can be passed to url
        x_string = str(x)
        y_string = str(y)

        #call function from div url and pass in parameters and parse result into JSON
        func_url = divURL + x_arg + x_string + y_arg + y_string
        url_output = urlopen(func_url)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']

        #test if result value is equal to expected result
        self.assertEqual(result, expected_result)

    #function to test add function
    def test_add_result(self):

            x_arg = '?x='
            y_arg = '&y='

            #generate random number between 1 and 100 for x and y variables
            x = random.randrange(100)
            y = random.randrange(100)

            #convert x and y to strings
            expected_result = x + y
            x_string = str(x)
            y_string = str(y)

            #call function from add url and pass in parameters and parse result into JSON
            func_url = addURL + x_arg + x_string + y_arg + y_string
            url_output = urlopen(func_url)
            json_obj = url_output.read()
            json_data = json.loads(json_obj)
            result = json_data['answer']

            #test if answer value is equal to expected result
            self.assertEqual(result, expected_result)

    #function to test sub function
    def test_sub_result(self):

            x_arg = '?x='
            y_arg = '&y='

            #generate random number between 1 and 100 for x and y variables
            x = random.randrange(100)
            y = random.randrange(100)

            #convert x and y to strings
            expected_result = x - y
            x_string = str(x)
            y_string = str(y)

            #call function from sub url and pass in parameters and parse result into JSON
            func_url = subURL + x_arg + x_string + y_arg + y_string
            url_output = urlopen(func_url)
            json_obj = url_output.read()
            json_data = json.loads(json_obj)
            result = json_data['answer']

            #test if answer value is equal to expected result
            self.assertEqual(result, expected_result)

    #function to test power function
    def test_power_result(self):

            x_arg = '?x='
            y_arg = '&y='

            #generate random number between 1 and 10 for x and y variables
            x = random.randrange(10)
            y = random.randrange(10)

            #convert x and y to strings
            expected_result = x ** y
            x_string = str(x)
            y_string = str(y)

            #call function from power url and pass in parameters and parse result into JSON
            func_url = powerURL + x_arg + x_string + y_arg + y_string
            value = urllib.request.urlopen(func_url).read()
            value_int = int(value)

            #test if answer value is equal to expected result
            self.assertEqual(value_int, expected_result)

    #function to test mod function
    def test_mod_result(self):

            x_arg = '?x='
            y_arg = '&y='

            #generate random number between 1 and 100 for x and y variables
            x = random.randrange(100)
            y = random.randrange(100)

            #convert x and y to strings
            expected_result = x % y
            x_string = str(x)
            y_string = str(y)

            #call function from mod url and pass in parameters and parse result into JSON
            func_url = modURL + x_arg + x_string + y_arg + y_string
            url_output = urlopen(func_url)
            json_obj = url_output.read()
            json_data = json.loads(json_obj)
            result = json_data['answer']

            #test if answer value is equal to expected result
            self.assertEqual(result, expected_result)
