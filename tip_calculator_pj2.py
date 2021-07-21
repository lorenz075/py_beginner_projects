def calculate_tip(total_bill, percentage, number_of_people):
    each_payment = (total_bill * ((percentage/100)+1)) / number_of_people
    return each_payment


if __name__ == "__main__":
   print("Welcome to the tip calculator")
   print("------------------------------")
   total_bill = float(input("What was the total bill?"))
   percentage = float(input("What percentage would like to give?")) 
   number_of_people = float(input("How many people to split the bill?"))
   
   result = calculate_tip(total_bill, percentage, number_of_people)
   
   print("Each person should pay: {}".format(round(result, 2)))
    