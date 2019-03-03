from pprint import pprint

dict_cinema = {
    'Пятница':
        {'day':{'today':{'number of people':{'<20':{'time_price': {12: 250, 16: 350, 20: 450}},'>20':{'time_price': {12: 250*0.8, 16: 350*0.8, 20: 450*0.8}}}},
                'tomorrow':{'number of people':{'<20':{'time_price': {12: 250*0.95, 16: 350*0.95, 20: 450*0.95}},'>20':{'time_price': {12: 250*0.75, 16: 350*0.75, 20: 450*0.75}}}},
                'genre': 'комедия', 'limit': 16}},
    'Чемпионы':
         {'day':{'today':{'number of people':{'<20':{'time_price': {10: 250, 13: 350, 16: 350}},'>20':{'time_price': {10: 250*0.8, 13: 350*0.8, 16: 350*0.8}}}},
                'tomorrow':{'number of people':{'<20':{'time_price': {10: 250*0.95, 13: 350*0.95, 16: 350*0.95}},'>20':{'time_price': {10: 250*0.75, 13: 350*0.75, 16: 350*0.75}}}},
                'genre': 'спорт', 'limit': 16}},

    'Пернатая банда':
          {'day':{'today':{'number of people':{'<20':{'time_price': {10: 350, 14: 450, 18: 450}},'>20':{'time_price': {10: 350*0.8, 14: 450*0.8, 18: 450*0.8}}}},
                'tomorrow':{'number of people':{'<20':{'time_price': {10: 350*0.95, 14: 450*0.95, 18: 450*0.95}},'>20':{'time_price': {10: 350*0.75, 14: 450*0.75, 18: 450*0.75}}}},
                'genre': 'мультфильм', 'limit': 6}},
    }


print(dict_cinema['Пятница']['day']['tomorrow']['number of people']['>20']['time_price'][12])
