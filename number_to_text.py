#!/usr/bin/env python
# -*- coding: utf-8 -*-

from adapters.base_adapter import BaseLangAdapter
from adapters import AdapterLangTr


class NTT:
    """Convert given number to text"""

    def __init__(self,
                 adapter: object = AdapterLangTr, fraction_size: int = 2):
        self.fraction_size = fraction_size
        self.adapter = adapter

    def number_to_text(self, number_to_text: float) -> str:
        return self.adapter.number_to_text(number_to_text)

    @property
    def adapter(self):
        return self.__adapter

    @adapter.setter
    def adapter(self, value):
        assert issubclass(value, BaseLangAdapter), \
            "adapter have to be subclass of BaseLangAdapter got: {}".format(type(value))
        self.__adapter = value()
        self.adapter.fraction_size = self.fraction_size
