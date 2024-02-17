from dataclasses import replace
from posixpath import split
from pydoc import stripid
import re


text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

def change_array(text):
    strip_text = text.strip()
    list_text = re.split('[,. ]+',strip_text)
    delete_space = [s for s in list_text if s]
    return  delete_space

def count_element(array_text):
    int_list = map(len,array_text)
    str_list = [str(a) for a in int_list]
    join_list = ''.join(str_list)
    return join_list

    

array_text = change_array(text)
result = count_element(array_text)         
print(result)