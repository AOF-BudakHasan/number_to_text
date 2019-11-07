# Number To Text 
Helps you convert numbers to text by selected langauge

```bash
pip install number-to-text
```

## Supported Languages
tr_TR 
## Usage

```python
# Example usage with adapter (default: AdapterLangTr) and fraction_size (default: 2)
from number_to_text import AdapterLangTr, NTT

new_ntt = NTT(adapter=AdapterLangTr, fraction_size=2)
new_ntt.number_to_text(2134.5362)  # returns 'İKİBİNYÜZOTUZDÖRTLİRAELLİDÖRTKURUŞ'
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
