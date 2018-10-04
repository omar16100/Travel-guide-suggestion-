import random
import time
from typing import Dict


def displayIntro():
    print('You want to travel in your midbreak but you are confused which country to go.')
    print('So, each of the friends gives a suggestion,')
    print('along with a pro and a con.')
    print('The countries are Russia, Palestine, Indonesia, Syria, Canada, Egypt, Ghana, Bangladesh, New Zealand and '
          'India.')
    print('Final decision will be based upon the number of votes.')
    print()

def chooseCountry():
    country = ''
    while country != '1' and country != '2' and country != '3' and country != '4' and country != '5' and country != '6' \
            and country != '7' and country != '8' and country != '9' and country != '10':
        print('Choose a number between 1 and 10: ')
        country = input()

    return country

def switch_demo(argument):
    switcher: Dict[int, str] = {
        1: "Bangladesh, beautiful but not tourist friendly.",
        2: "India, beautiful, but not tourist friendly.",
        3: "New Zealand, great weather, but lots of mosquitos and sandflies.",
        4: "Russia, amazing architecture, but expensive.",
        5: "Ghana, rich and diverse culture but climate is humid.",
        6: "Canada, great outdoors but expensive.",
        7: "Palestine, amazing cuisine but transportation is complicated.",
        8: "Indonesia, beautiful country but bad traffic.",
        9: "Syria, naturally beautiful but lack of safety.",
        10: "Egypt, epitome of ancient history but bad traffic."
    }
    print(switcher.get(argument, "Invalid."))

    

def checkCountry(chosenCountry):

    time.sleep(2)
    print('Upon considerations, the place has to be cheap and beautiful but may not fulfill both..')
    time.sleep(2)
    print()


    country = random.randrange(1, 10, 1)

    return switch_demo(country)


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    countryNumber = chooseCountry()

    checkCountry(countryNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
