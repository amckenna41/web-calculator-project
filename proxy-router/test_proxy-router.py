
#Testing for proxy router microservice #

#import testing modules and dependancies
import unittest
from flask import Flask
from flask import request
import urllib.request
import func_url as fu
import json
from urllib.request import urlopen

#initialise function url's from func_url file
addURL = fu.ADD_URL
multURL = fu.MULT_URL
divURL = fu.DIV_URL
modURL = fu.MOD_URL
powerURL = fu.POWER_URL
subURL = fu.SUB_URL

#testing class for proxy service
class test_proxy(unittest.TestCase):

    #test result of multiply function on the proxy server
    def test_mult_result(self):

        x_arg = '?x='
        y_arg = '&y='
        #multURL = 'https://mult.40175607.qpc.hal.davecutting.uk/'

        result = 10 * 10
        x = '10'
        y = '10'
        http_output = multURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 100)

        result = 5 * 4
        x = '5'
        y = '4'
        http_output = multURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 20)

        result = 14 * 2
        x = '14'
        y = '2'
        http_output = multURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 28)

    #test result of divide function on the proxy server
    def test_div_result(self):
        x_arg = '?x='
        y_arg = '&y='

        result = 40 / 8
        x = '40'
        y = '8'
        http_output = divURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['Answer']
        self.assertEqual(result, 5)

        result = 120 / 2
        x = '120'
        y = '2'
        http_output = divURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['Answer']
        self.assertEqual(result, 60)

        result = 80 / 4
        x = '80'
        y = '4'
        http_output = divURL + x_arg + x + y_arg + y
        #result = urllib.request.urlopen(http_output).read()
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['Answer']
        self.assertEqual(result, 20)

    #test result of add function on the proxy server
    def test_add_result(self):
        x_arg = '?x='
        y_arg = '&y='

        result = 60 + 49
        x = '60'
        y = '49'
        http_output = addURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 109)

        result = 12 + 24
        x = '12'
        y = '24'
        http_output = addURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 36)

        result = 412 + 564
        x = '412'
        y = '564'
        http_output = addURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 976)

    #test result of sub function on the proxy server
    def test_sub_result(self):
        x_arg = '?x='
        y_arg = '&y='

        result = 20 - 10
        x = '20'
        y = '10'
        http_output = subURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 10)

        result = 48 - 47
        x = '48'
        y = '47'
        http_output = subURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 1)

        result = 412 - 12
        x = '412'
        y = '12'
        http_output = subURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 400)

    #test result of mod function on the proxy server
    def test_mod_result(self):
        x_arg = '?x='
        y_arg = '&y='

        result = 21 % 6
        x = '21'
        y = '6'
        http_output = modURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 3)

        result = 10 % 3
        x = '10'
        y = '3'
        http_output = modURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 1)

        result = 49 % 10
        x = '49'
        y = '10'
        http_output = modURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 9)

    #test result of power function on the proxy server
    def test_power_result(self):
        x_arg = '?x='
        y_arg = '&y='

        result = 2 ^ 8
        x = '2'
        y = '8'
        http_output = powerURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 256)

        result = 16 ^ 4
        x = '16'
        y = '4'
        http_output = powerURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 65536)

        result = 10 ^ 5
        x = '10'
        y = '5'
        http_output = powerURL + x_arg + x + y_arg + y
        url_output = urlopen(http_output)
        json_obj = url_output.read()
        json_data = json.loads(json_obj)
        result = json_data['answer']
        self.assertEqual(result, 100000)
