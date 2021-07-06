import pytest
from homework3.task3 import make_filter

sample_data  =  [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]

def test_make_filter_for_several_items_from_one_dict():
    '''The function takes two or more elements from one dict and returns a dict, uses all of them.'''
    assert make_filter(name='polly', type='bird').apply(sample_data) == [sample_data[1]]


def test_make_filter_for_items_of_different_dictionaries():
    '''Function accept two or more items of one dict and return dict use all of them'''
    assert make_filter(name='Bill', type='bird').apply(sample_data) == []


def test_make_filter_when_key_not_in_dictionary():
    '''Function takes on a key value that is not in the dictionary'''
    assert make_filter(is_alive= True).apply(sample_data) == []
