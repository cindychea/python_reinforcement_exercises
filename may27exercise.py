digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
es = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'neuve']
la = ['usus', 'duo', 'tres', 'quattuor', 'quinque', 'sex', 'septem', 'octo', 'novem']
ch = ['yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']

# { 
#   '1': {'french': 'un', 'english': 'one'},
#   '2': {'french': 'deux', 'english': 'two'},
#   '3': {'french': 'trois', 'english': 'three'},
#   ...
#   '9': {'french': 'neuf', 'english': 'nine'} 
# }

numbers = {}
for i in range(0,len(digits)):
    numbers[digits[i]] = {
        'french': fr[i],
        'english': en[i],
        'spanish': es[i],
        'latin': la[i],
        'chinese': ch[i],
    }
        
print(numbers)

# {
#     '1': {'french': 'un', 'english': 'one', 'spanish': 'uno', 'latin': 'usus', 'chinese': 'yi'}, 
#     '2': {'french': 'deux', 'english': 'two', 'spanish': 'dos', 'latin': 'duo', 'chinese': 'er'}, 
#     '3': {'french': 'trois', 'english': 'three', 'spanish': 'tres', 'latin': 'tres', 'chinese': 'san'}, 
#     '4': {'french': 'quatre', 'english': 'four', 'spanish': 'cuatro', 'latin': 'quattuor', 'chinese': 'si'}, 
#     '5': {'french': 'cinq', 'english': 'five', 'spanish': 'cinco', 'latin': 'quinque', 'chinese': 'wu'}, 
#     '6': {'french': 'six', 'english': 'six', 'spanish': 'seis', 'latin': 'sex', 'chinese': 'liu'}, 
#     '7': {'french': 'sept', 'english': 'seven', 'spanish': 'siete', 'latin': 'septem', 'chinese': 'qi'}, 
#     '8': {'french': 'huit', 'english': 'eight', 'spanish': 'ocho', 'latin': 'octo', 'chinese': 'ba'}, 
#     '9': {'french': 'neuf', 'english': 'nine', 'spanish': 'neuve', 'latin': 'novem', 'chinese': 'jiu'}
# }
