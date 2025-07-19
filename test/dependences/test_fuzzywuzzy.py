# test_fuzzywuzzy.py
from fuzzywuzzy import fuzz
print(fuzz.ratio("hola", "hola mundo"))  # Debería imprimir un número entre 0 y 100