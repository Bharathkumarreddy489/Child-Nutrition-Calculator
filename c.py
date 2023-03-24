#to know bmi category based on bmi
def bmiCategory(Name,bmi):
    if bmi<16:
        print("BMI OF ",Name,"is",bmi,"he or she is severly underweight.")
    elif bmi>=16 and bmi<18.5:
        print("BMI OF ",Name,"is",bmi,"he or she is underweight.")
    elif bmi>=18.5 and bmi<25:
        print("BMI OF ",Name,"is",bmi,"he or she is Healthy.")
    elif bmi>=25 and bmi<30:
        print("BMI OF ",Name,"is",bmi,"he or she is Overweight.")
    elif bmi<=30:
        print("BMI OF ",Name,"is",bmi,"he or she is obese.")

#to calculate total intake calories of the child by comparing the calories for 100gm
def caloriesCalcutor(calories):
    caloriesperHundredgrams={"Milk":100,"Vegetables":85,"Meat":143,"Lentils":113,"Egg":155,"Rice":130}
    
    #for key , value in calories.items():
       # calorie=value
    milk_cal=calories['Milk']*100/100
    veg_cal=calories['Vegetables']*85/100
    meat_cal=calories['Meat']*143/100
    lentils_cal=calories['Lentils']*113/100
    egg_cal=calories['Egg']*155/100
    rice_cal=calories['Rice']*130/100
    totalCalories=milk_cal+veg_cal+meat_cal+lentils_cal+egg_cal+rice_cal
    return totalCalories
# nourishmentResult function to print the nourished status of child
def Result(Name,Age,totalCalorie):
    
    if Age>=0 and Age<2:      #if Age>=0 and Age<2 and totalCalories<800- under-nourished else nourished
        if totalCalories<800:
            print("The daily calorie consumption of ",Name," has to be 800 and he (she) is taking ",totalCalorie,"he or she required more calories  and he or she is  under-nourished.")
        else:
            print("The daily calorie consumption of ",Name, "has to be 800 and he (she) is taking ",totalCalorie," he or she is nourished.")
    elif Age>=2 and Age<4:       ##if Age>=2 and Age<4 and totalCalories<1400- under-nourished else nourished
        if totalCalories<1400:
            print("The daily calorie consumption of ",Name," has to be 1400 and he (she) is taking ",totalCalorie,"he or she required more calories  and he or she is  under-nourished.")
        else:
            print("The daily calorie consumption of ",Name," has to be 1400 and he (she) is taking ",totalCalorie," he or she is nourished.")
    elif Age>=4 and Age<8:      ##if Age>=4 and Age<8 and totalCalories<1800- under-nourished else nourished
        if totalCalories<1800:
            print("The daily calorie consumption of ",Name," has to be 1800 and he (she) is taking ",totalCalorie,"he or she required more calories  and he or she is  under-nourished.")
        else:
            print("The daily calorie consumption of ",Name," has to be 1800 and he (she) is taking ",totalCalorie," he or she is nourished.")
    else:
        print("He(or She) is not Child!")
        


        
print("WELCOME TO CHILD NUTRTION CALCULATOR")
print("Enter the following details of child:")
Name=input("Name:")
Age=int(input("Age:"))
Height=float(input("Height(inches):"))
Weight=float(input("Weight(lb):"))
             
print("")

#details of food consumption of a child in grams
print("Food consumption of a child in a day in grams")
calories={}
calories["Milk"]=int(input("Milk:"))
calories["Vegetables"]=int(input("Vegetables:"))
calories["Meat"]=int(input("Meat:"))
calories["Lentils"]=int(input("Lentils:"))
calories["Egg"]=int(input("Egg:"))
calories["Rice"]=int(input("Rice:"))

print("")

#calculation of body mass index using formula
bmi=(Weight/(Height**2))*703
#rounding of the decimal number to two decimal places
bmiDecimal=round(bmi,2)
#calling the bmiCategory function 
bmiCategory(Name,bmiDecimal)

print("")

totalCalories=caloriesCalcutor(calories)
totalCaloriesRoundOff=round(totalCalories,2)

Result(Name,Age,totalCaloriesRoundOff)


