# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 17:09:47 2022

@author: lovaa
"""


## lets try and create this function as an itterable (as in it uses yield)
## then have it return,  

def annuity(n,i,P,immediate = True,PV = True):
    '''

    Parameters
    ----------
    n : compounding periods 
    i : Interest in decimal form
    P : Payment
        
    immediate : True calculates annuity immediate 
        DESCRIPTION. The default is True.
    PV : TYPE, True calculates present value of an annuity. 
        DESCRIPTION. The default is True.
    ------
    obviously it you could calculate pv without needing generating function
    nevertheless it's good practice learning how to use them. 
    '''
    def yieldflow(n,i):
        for k in range(1,n+1):
            yield (1+i)**(-k)
    cashflow_iterable = yieldflow(n,i)
    pres_val = 0 
    while True:
        try:
            pres_val += cashflow_iterable.__next__()
        except StopIteration:
            break
    if immediate == True:
        if PV == True: 
            return P*pres_val 
        else:
            return P*pres_val*(1+i)**n
    else:
        if PV == True: 
            return P*pres_val*(1+i) 
        else:
            return P*pres_val*(1+i)**(n+1)
        
''' would be cool to do a two dimensional plot with variables, n,i changing and then
future value as the z axis ''' 

import numpy
import matplotlib.pyplot as plt
import seq 
import pandas


for interest in [interest*.01 for interest in range(1,10)]:
    years_input = seq.seq(0,20,1)
    annuity_sums = [annuity(int(year),interest,1,True,False) for year in years_input]
    plt.plot(years_input,annuity_sums)

                
years_input = seq.seq(0,20,1)
annuity_sums = [annuity(int(year),.05,1,True,False) for year in years_input]



def yieldflow(n,i):
    for k in range(1,n+1):
        yield (1+i)**(-k)
        
        
        
        
T = yieldflow(10,.10)

PV = 0
while True:
    try:
        PV += T.__next__()
    except StopIteration:
        break
print(PV)
    



''' create a function that produces the amortization schedule of a bond ''' 



def amortize_bond(F,r,j,n):
    ''' F = face_value 
        c = coupon rate 
        j = effective yield rate for coupon period 
        n = bond term '''
    def yield_PR(n):
        for k in range(1,n+1):
            if k < n:
                yield F*(r-j)*(1+j)**(-(n-k+1))
            else:
                yield F*(r-j)*(1+j)**(-(n-k+1)) + F 
    principle_generator = yield_PR(n)
    OB = F*(1+j)**(-n) + F*r * sum([(1+j)**(-k) for k in range(1,n+1)])
    print(f"{0:^4}|{OB:^10,.2f}|{'-':^8}|{'-':^8}|{'-':^8}")
    iter_count = 1 
    while True:
        try:
            PR = principle_generator.__next__()
            I = F*r - PR
            if iter_count == n:
                I = F*r - PR + F 
            OB = OB - PR
            print(f"{iter_count:^4}|{OB:^10,.2f}|{round(F*r,3):^8}|{I:^8,.2f}|{PR:^8,.2f}")
            iter_count += 1 
        except:
            break 

                          

def amortize_bond(F,r,j,n,C = 'par'):
    ''' F = face_value 
        c = coupon rate 
        j = effective yield rate for coupon period 
        n = bond term '''
    if C == 'par':
        C = F  
    def yield_PR(n):
        for k in range(1,n+1):
            if k < n:
                yield (F*r-C*j)*(1+j)**(-(n-k+1))
            else:
                yield (F*r-C*j)*(1+j)**(-(n-k+1)) + C 
    principle_generator = yield_PR(n)
    OB = C*(1+j)**(-n) + F*r * sum([(1+j)**(-k) for k in range(1,n+1)])
    print(f"{0:^4}|{OB:^10,.2f}|{'-':^8}|{'-':^8}|{'-':^8}")
    iter_count = 1 
    while True:
        try:
            PR = principle_generator.__next__()
            I = F*r - PR
            if iter_count == n:
                I = F*r - PR + C 
            OB = OB - PR
            print(f"{iter_count:^4}|{OB:^10,.2f}|{round(F*r,3):^8}|{I:^8,.2f}|{PR:^8,.2f}")
            iter_count += 1 
        except:
            break 
        
        
                                                                 


def yield_market_value(F,r,j,n,C = 'par'):
    if C == 'par':
        C = F
    print(C)
    days = n * 180
    for k in range(1,days+1):
        k2 = k % 180
        k1 = k // 180
        yield ( (C*(1+j)**(-k1) + F*r * sum([(1+j)**(-t) for t in range(1,k1+1)]))*(1+j)**(k2/180))
        

def yield_market_value2(F,r,j,n,C = 'par'):
    if C == 'par':
        C = F
    print(C)
    days = n * 180
    for k in range(0,days+1):
        k2 = k % 180
        k1 = k // 180
        if k< 10:
            print(n - k1)
        yield ( (C*(1+j)**(-(n-k1)) + F*r * sum([(1+j)**(-t) for t in range(1,n-k1+1)]))*(1+j)**(k2/180))


a_n = lambda n: sum([(1.10)**(-t) for t in range(1,n+1)])

         
mark_val = yield_market_value2(10000, .05, .07 , 2)

# while True:
#     try:
#         print( mark_val.__next__())
#     except StopIteration:
#         break

mark_val = yield_market_value2(10000, .05, .17 , 8)
mark_vals = [i for i in mark_val]

days_input = seq.seq(0,8*180,1)
plt.plot(days_input,mark_vals)

'''
for interest in [.02*k for k in range(1,10)]:
    mark_val = yield_market_value2(10000, .05, interest , 8)
    mark_vals = [i for i in mark_val]
    days_input = seq.seq(0,8*180,1)
    plt.plot(days_input,mark_vals)
'''
    
for coupon in [.02*k for k in range(1,5)]:
    mark_val = yield_market_value2(10000, coupon, .08 , 8)
    mark_vals = [i for i in mark_val]
    days_input = seq.seq(0,8*180,1)
    plt.plot(days_input,mark_vals)
    
def amortize_loanz(loan_amount, period_rate, num_payments):
    L = loan_amount 
    i = period_rate
    n = num_payments 
    a_n = lambda n: sum([(1+i)**(-t) for t in range(1,n+1)])
    K = L / a_n(n)
    K_t = lambda t: K if t != n else 0
    OB_t = lambda t: K*a_n(n-t) #if n != t else 0
    PR_t = lambda t: K*(1+i)**(-(n-t+1)) #if n != t else 0
    I_t = lambda t: K - PR_t(t) #if n != t else 0
    print(f"\n\n{'Payment':^10}|{'Outstanding Bal':^20}|{'Interest':^10}|{'Principle':^12}")
    print("="*55)
    iter_count = 0
    while True:
        print(f"{K_t(iter_count):^10,.2f}|{OB_t(iter_count):^20,.2f}|{I_t(iter_count):^10,.2f}|{PR_t(iter_count):^12,.2f}")
        iter_count += 1
        if iter_count == n+1:
            break 
    
        
    
    
        