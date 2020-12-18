import re
import cmath
def get_complex_part(string):
    string = string.replace('+',' +').replace('-',' -')
    return list(map(int,re.sub("[^-\d+]",' ',string).split()  ))
_complex = input()
[real,imaginary] = get_complex_part(_complex)
print(pow( pow(real,2)+pow(imaginary,2), 0.5 ))
print(cmath.phase( complex(real,imaginary) ))