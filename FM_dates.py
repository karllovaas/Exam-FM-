# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:41:22 2022

@author: lovaa
"""
import random
import time

months = ['January','February','march','april','may','june','july','august','september','october','november','december']
months_dict = {i:months[i] for i in range(len(months))}
months_dictr = {months[i]:i for i in range(len(months))}

def select_two_months():
    month1 = random.randint(1, 12)-1
    month2 = random.randint(1,12)-1
    while month1 == month2:
        month2 = random.randint(1, 12)
    selection = [months_dict[month1],months_dict[month2]]
    if month1 > month2:
        interval_between = 12 + (month2-month1)
    else: 
        interval_between = month2 - month1
    selection.append(interval_between)
    return selection

print(select_two_months())


def compouding_periods_game():
    while True:
        question = select_two_months()
        start = time.time()
        guess = int(input(f"How many compouding periods are there between \n7{question[0]} and {question[1]}?: "))
        stop = time.time()
        total_time = round(stop - start,2)
        if guess == question[2]:
            print(f"Correct: n = {question[2]}, Time:{total_time}")
        else: 
            print(f"Incorrect: n = {question[2]} not: {guess} ,Time: {total_time}")
        onward = input("press q to quit:")
        if onward == 'q':
            break 
        
## i need a program that picks years near 
## it would be nice to have program that ask for number of months between different date 
## forms. 
## the second essential part of the program is diserning the number of months between these dates.
## consider for example the two dates 02/2020 and 04/2020 (Feb. 2020 and April. 2022). 
## notice april comes after februrary that is 04 > 02 and. obviously we need an algorithm that 
## comes up with the answer 26. notice 2022-2020*12 =  24. 12 - month(feb) = 10 so always start are calculation 
## at the beggining of the first year go forward.... (year2 - year1 ) + (month(year2) - month(year1)
## see if this algorithm works for dates where month year(1) > month year(2). consider the reverse 
## by comparing the dates 04/2020 and 02/2020 algorithm would be (2022-2020)*12 + (2 - 4) = 22 .which to me makes sense. 
## this 



def select_two_years():
    ''' this game is similar to the other game except that '''
    years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997,
             1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
             2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
             2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,
             2022, 2023, 2024, 2025]
    year1 = random.randint(1990, 2025)
    year2 = random.randint(year1, 2025)
    months_between = (year2 - year1)*12
    selection = [year1, year2, months_between]
    return selection

def select_two_years_close():
    ''' this game is similar to the other game except that '''
    years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997,
             1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
             2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
             2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,
             2022, 2023, 2024, 2025]
    year1 = random.randint(1990, 2025)
    year2 = random.randint(year1, 2025)
    while year2 - year1 >= 6:
        year1 = random.randint(1990, 2025)
        year2 = random.randint(year1, 2025)
    months_between = (year2 - year1)*12
    selection = [year1, year2, months_between]
    return selection

def select_two_years_close2():
    ''' this game is similar to the other game except that '''
    years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997,
             1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
             2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
             2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,
             2022, 2023, 2024, 2025]
    year1 = random.randint(2016, 2025)
    year2 = random.randint(year1, 2025)
    while year2 - year1 >= 6:
        year1 = random.randint(1990, 2025)
        year2 = random.randint(year1, 2025)
    months_between = (year2 - year1)*12
    selection = [year1, year2, months_between]
    return selection


## i think this probably a good example a possition where i need to use  classes anything else is 
## just so tediious 

def game2():
    Input = 'a'
    print("Press q at an moment to quit the game:")
    while Input != 'q':
        correct_n = -1
        while correct_n < 0:
            a = random.choice([0,1,2])
            ''' would be cool assign based on a discrete or multinomial distribution '''
            if a == 0:
                years_choice = select_two_years()
            elif a == 1:
                years_choice = select_two_years_close()
            else:
                years_choice = select_two_years_close2()
            print(years_choice)
            months_choice = select_two_months()
            correct_n = years_choice[2] + (months_dictr[months_choice[1]] - months_dictr[months_choice[0]])    
            print(correct_n)
        a = random.choice([0,1])
        start = time.time()
        if a == 0 :
            Input = input(f"How many months between {months_choice[0]}, {years_choice[0]} and {months_choice[1]}, {years_choice[1]}")
        else:
            Input = input(f"How many months between {months_dictr[months_choice[0]]}/{years_choice[0]} and {months_dictr[months_choice[1]]}/{years_choice[1]}")
        if Input == 'q':
            break
        else:
            guess = int(Input)
        stop = time.time()
        timer = round(stop - start,2)
        if guess == correct_n:
            print(f"Correct n = {correct_n} , Time:{timer} ")
        else:
            print(f'Incorrect n = {correct_n} not {guess} , Time:{timer}')
        
## the biggest mistake that i made with this program is didn't write the program first to produce the correct
## values, the inputs and the assessment of the input are easy and periferal, including them too early 
## obscures the 