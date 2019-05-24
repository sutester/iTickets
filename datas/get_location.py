#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2019-05-24 14:35:18
# @Last Modified by:   Danny
# @Last Modified time: 2019-05-24 14:35:18
import json


def get_location(index):
    if isinstance(index, int):
        with open('datas/location.json', 'r') as f:
            location_list = json.load(f).get('location')
            if index > len(location_list) - 1:
                raise IndexError('Out of index!')
            else:
                return location_list[index]
    else:
        raise TypeError('Index should be integer!')


if __name__ == '__main__':
    #test
    print(get_location(7))
    #print(get_location('a'))
    #print(get_location(8))