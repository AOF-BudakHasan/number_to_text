#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Helps you convert to numbers to text
    ===
    Example usage with adapter (default: AdapterLangTr) and fraction_size (default: 2)
    >>> from number_to_text import AdapterLangTr, NTT
    >>> new_ntt = NTT(adapter=AdapterLangTr, fraction_size=2)
    >>> new_ntt.number_to_text(2134.5362) -> "İKİBİNYÜZOTUZDÖRTLİRAELLİDÖRTKURUŞ"
"""
from .number_to_text import NTT
from .adapters import AdapterLangTr

__all__ = ['NTT', 'AdapterLangTr']

