#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from json import loads
from abc import ABCMeta, abstractmethod


__all__ = ['BaseLangAdapter']


class BaseLangAdapter(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__fraction_size = 2
        self.decimal_delimater = '.'
        self.lang_file_name = None
        self.lang_file = None

    @abstractmethod
    def number_to_text(self, number_to_text: float) -> str:
        pass

    @property
    def fraction_size(self) -> int:
        return self.__fraction_size

    @fraction_size.setter
    def fraction_size(self, value):
        if value:
            assert isinstance(value, int), "fraction_size have to be an int got: {}".format(type(value))
            self.__fraction_size = value

    def set_lang_json(self):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.lang_file_name)
        with open(file_path, 'r', encoding="utf-8") as f:
            self.lang_file = loads(f.read())

    def round_and_split(self, number: float) -> tuple:
        nmb, dcm = str(round(float(number), 2)).split(self.decimal_delimater)
        return nmb, dcm