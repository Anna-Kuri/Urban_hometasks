# Library #1 - Requests

import requests

""" Requests is the most used library for HTTP requests in Python, 
it allows to get various types of information from the webpage, send data to the webpage, trace requests """

""" GET is method allows us to retrive data from the webpage"""
get_response = requests.get('https://realpython.com/python-requests/')
print(get_response)

""" .status_code - parameter that shows if the request was successful, it can be used as boolean because
Response has overloaded .__bool__() method and takes .status_code into account when determining Truth value
Types of codes:
1xx informational response – the request was received, continuing process
2xx successful – the request was successfully received, understood, and accepted
3xx redirection – further action needs to be taken in order to complete the request
4xx client error – the request contains bad syntax or cannot be fulfilled
5xx server error – the server failed to fulfil an apparently valid request """

if get_response:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {get_response.status_code}")

""" .content gives  access to the raw bytes of the response and .text converts it into utf-8 encoded string"""

with open('Text_from_webpage.txt', 'w', encoding='utf-8') as file:
    file.write(f'{get_response.text}')

"""In many cases response is JSON content, so it can be decoded with .jason(). 
However, success of the call to .json() does not indicate the success of the response 
and vice versa - the response might me not in json format"""
try:
    response_dict = requests.get('https://jsonplaceholder.typicode.com/users').json()
    print(response_dict)
except Exception:
    pass

# Library #2 - Numpy
"""Numpy is a library that's extremly convenient for operating with arrays of data"""

import numpy as np #Importing numpy as np is genral common practice

"""Arrays can be created from scratch or from Python sequences, like a list, but unlike lists  arrays are homogeneous - they consist of elements of one data type"""
sin_angle = np.array([1, 200, 270, 50, 120, 10, 13, 210, 60, 240, 78, 300, 30, 9,
                      330, 22, 14, 70, 180, 90, 80, 360, 95, 100, 150])
print(f'sin_angle = {sin_angle}')

""" Arrays have parameters: 
1) dimention - also referred as axis. ndim attribute - number of dimentions 
2) shape - a tuple of non-negative integers that specify the number of elements along each dimension
3) size - number of elements
"""
print(f'Number of dimentions of sin_angle array: {sin_angle.ndim}')
print(f'Shape of sin_angle array: {sin_angle.shape}')
print(f'Size of sin_angle array: {sin_angle.size}')

""" Elements in arrays can be adressed by their indexes, same as elements in lists"""
print(f'First element in sin_angle array has index 0 and value: {sin_angle[0]}')

""" We can select elements that satisfy one or two conditions"""
sin_angle_between_10_and_100 = sin_angle[(sin_angle > 10) & (sin_angle < 100)]
print(f'sin_angle array values between 10 and 100: {sin_angle_between_10_and_100}')

""" Arrays can be sorted: basic type of sorting is in ascending order. 
There are also:
1) argsort - indirect sort along a specified axis
2) lexsort - indirect stable sort on multiple keys
3) searchsorted - find elements in a sorted array
4) partition - which is a partial sort 
"""
sin_angle = np.sort(sin_angle)
print(f'sin_angle = {sin_angle}')

"""Arrays can have slices, just like lists. 
Also arrays have views that are creted by slicing original array. If we change a value in a view, 
value in original array will change as well"""

array_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'Array 1 has values: {array_1}')
array_2 = array_1[0, :]
array_2[0] = 1000
print(f'Array 2 has values: {array_2}')
print(f'And now array 1 has values: {array_1}')


""" Two arrays can be concatenated together along existing axis"""

sin_value_1 = np.array([0.01745241, 0.15643447, 0.17364818, 0.22495105,
                      0.2419219, 0.37460659, 0.5,  0.76604444, 0.8660254])

sin_value_2 = np.array([0.93969262, 0.9781476, 0.98480775, 1.0,  0.9961947,
                      0.98480775, 0.8660254, 0.5, 0.0, -0.34202014, -0.8660254,
                      -1.0, -0.8660254, -0.5, 0.0])

print(f'sin_value_1 = {sin_value_1}')
print(f'sin_value_2 = {sin_value_2}')
sin_value = np.concatenate((sin_value_1, sin_value_2))
print(f'sin_value = {sin_value}')

"""" We can create arrays from scratch: fill them with 1, 0, make empty array with random content, 
Also we can create an array with range of elements, set up their type, step size """
zeros = np.zeros(10)
ones = np.ones(2, dtype = int)
empty = np.empty(5)
ranged_array = np.arange(1, 100, 2)

print(f'Array filled with 10 zeros: {zeros}')
print(f"Array filled with 2 1's: {ones}")
print(f'Empty array filled with 5 random elements: {empty}')
print(f'Array with elements in range from 1 to 100 with step 2: {ranged_array}')

"""" Arrays can be stack horizontally and verically """

vertical_stack = np.vstack((array_1, array_2))
print(f"Vertical stack: {vertical_stack}")
horizontal_stack = np.hstack((ones, array_2))
print(f"Horizontal stack: {horizontal_stack}")

""" Arrays support various operations """

data = np.array([1, 7])

data_plus_ones = data + ones # Adding arrays
print(f"Adding data and ones arrays: {data_plus_ones}")

multiply = data * data_plus_ones # Multiplying arrays
print(f"Multiplying ones and data+ones arrays: {multiply}")

division = data / data_plus_ones # Dividing arrays
print(f"Dividing ones and data+ones arrays: {division}")

total = data.sum() # Sum of elements of the array
print(f"The sum of elements in data array: {total}")

print(f"Max value in data array: {data.max()}") #Max value in the array

print(f"Min value in data array: {data.min()}") #Min value in the array

double_data = data * 2 #Broadcasting - an operation between an array and singular number or arrays of different size

print(f"Broadcating: {double_data}")

""" Arrays can be saved as.npy files and loaded """

np.save('sin_value_array', sin_value)

