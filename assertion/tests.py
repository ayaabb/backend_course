from MathematicalAssertion import math_operation as mp
from check_is_in_list import *
from check_is_in_dict import *


def TEST_Mathematical_Operation_assertion():
      print(f'Mathematical Operation assertion:\n'
            f'check if {3} greater than {5} : {mp(3).is_greater(5)} \n'
            f'check if {3}+{2} equal to {5} : {mp(3 + 2).is_equal(5)} \n'
            f'check if {10}-{2} smaller than {5} : {mp(10 - 2).is_smaller(5)} \n'
            f'check if {7}-{3} smaller than {5} : {mp(7 - 3).is_smaller(5)} \n'
            f'check if {7} greater than {5} : {mp(7).is_greater(5)} \n'
             f'check if {2} equal to {2} : {mp(2).is_equal(2)} \n')


def TEST_Assert_value_in_list():
      list1 =  [1, 2, 3, 4]
      list2 = [[1, 2],6, [3, [4, 5]] , []]

      print(f"Assert value in list:"
            f"check if 2 is in {list1} : {assert_list(3).in_list(list1)}\n"
            f"check if 5 is in {list1} : {assert_list(5).in_list(list1)}\n"
            f"check if 2 is in {list2} : {assert_list(2).in_list(list2)}\n"
            f"check if [4,5] is in {list2} : {assert_list([4,5]).in_list(list2)}\n"
            f"check if [] is in {list2} : {assert_list([]).in_list(list2)}\n"
            f"check if [4] is in {list2} : {assert_list([4]).in_list(list2)}\n")


def TEST_key_value_in_dictionary():
      dict1 = {'name': 'John', 'age': 25}
      dict2 = {'person': {'name': 'John', 'address': '123 Main St'}}

      print(f"Assert key or value in dictionary:\n"
            f"check if 'age' is key in {dict1} : {assert_dict('age').is_key(dict1)}\n"
            f"check if 25 is value in {dict1} : {assert_dict(25).is_value(dict1)}\n"
            f"check if 'name' is key in {dict2} : {assert_dict('name').is_key(dict2)}\n"
            f"check if 'name' is value in {dict2} : {assert_dict('name').is_value(dict2)}\n"
            f"check if 'address' is key in {dict2} : {assert_dict('address').is_key(dict2)}\n"
             f"check if '123 Main St' is value in {dict2} : {assert_dict('123 Main St').is_value(dict2)}\n")

TEST_Mathematical_Operation_assertion()
TEST_Assert_value_in_list()
TEST_key_value_in_dictionary()