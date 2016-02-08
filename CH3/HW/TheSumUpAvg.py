# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:32:00 2016

@author: kiaph

This program will be used to calculate the average of a seriers of numbers.
"""

def main():
    print("Welcome to SeqCarlulator, the sequenced numbers average calculator!")
    print("thank you for choosing SeqCarlulator")
    x = (input("Are your numbers of consecutive sequence? " )).lower()
    total_value = 0
    
    if x in('yes','y', 'yeah', 'yep', 'yer', 'yee', 'yap', 'si', 'ja'):
    
        
        starting_number = eval(input("what is the value of the lowest number? "))
        ending_number = eval(input("What is the value of the greatest number? "))
        number_range = ((ending_number - starting_number) + 1)
        number_rangex = (number_range)
        new_number = (starting_number)
        total_value = 0
        #starting_numberx = starting_number
        while number_rangex != 0:
            #starting_numberx = starting_number
            #print("Starting number : ", starting_numberx)
            
            total_value = total_value + new_number
            new_number = new_number + 1
            
            number_rangex = number_rangex - 1
        else:
            total_value = total_value #+ ending_number 
            number_avg = total_value/(number_range)
            print("The sum of your numers is: ", total_value)
            print("The average of your sequence is: ", number_avg )
            

        
    elif x in("nah", "no", "nope", "nu-uh", "not", "na", "nop", "noo", "neigh", "nae"):
         
        number_total = eval(input("How many numbers are in your sequence? "))
        number_totalx = number_total        
        print("Please enter your numbers one at a time. ")
        while number_totalx != 0 :
            next_number = eval(input("Enter your number: "))
            total_value = next_number + total_value
            number_totalx = number_totalx - 1
        else:
            number_mean = total_value/number_total
            print("The total sum is: ", total_value )
            print("The average of the sequence is: ", number_mean)
            
            
    else:
        print("I cannot understand you, please try again using yes or no. ")
        
main()
  
        
            
            
            
        
        
    
    