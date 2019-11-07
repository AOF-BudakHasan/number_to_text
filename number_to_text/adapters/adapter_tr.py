#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base_adapter import BaseLangAdapter

__all__ = ['AdapterLangTr']


class AdapterLangTr(BaseLangAdapter):
    """Convert given number to text"""

    def __init__(self):
        super(AdapterLangTr, self).__init__()
        self.lang_file_name = 'lang_tr.json'
        self.converted_text = ''

    def __del__(self):
        del self.lang_file

    def number_to_text(self, number_to_text: float) -> str:
        self.set_lang_json()
        nmb, dcm = self.round_and_split(number=number_to_text)
        decimal_value = ''
        if dcm != '0':
            res = self.convert_to_text(dcm)
            decimal_value = '{}{}'.format(res, self.lang_file['currency_decimal_title'])
        res = self.convert_to_text(nmb)
        self.converted_text = '{}{}{}'.format(res, self.lang_file['currency_title'], decimal_value)
        return self.converted_text

    def convert_to_text(self, number_str: str) -> str:
        self.converted_text = ''
        if number_str == '0':
            self.concat_text(self.lang_file.get('zero', 'zero'))
            return self.converted_text
        name_index = 0
        for index, val in enumerate(number_str[::-1]):
            if val == '0':
                text = ''
            elif index <= 1:
                text = self.lang_file.get(val, '**')[index]
            else:
                res = (index + 1) % 3
                temp_val = self.lang_file.get(val, '**')[1 if res == 2 else 0]
                endfix = ''
                if res == 0:  # yüzlük ise 6 yüz veya 6 yüz milyon
                    endfix = self.lang_file['names'][0]
                    name_index += 1
                elif res == 1:
                    if len(number_str) == index + 1 and val == '1' and name_index == 1:
                        temp_val = ''
                    endfix = self.lang_file['names'][name_index]
                text = '{}{}'.format(temp_val, endfix)
            self.concat_text(text)
        return self.converted_text

    def concat_text(self, new_text: str):
        self.converted_text = new_text.upper() + self.converted_text
