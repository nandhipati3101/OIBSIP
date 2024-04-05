print("Welcome to body mass index calculation:")
weight=float(input("enter your weight in kilograms:"))
height=float(input("enter your height in meters:"))
bmi=weight/height**2
print("your BMI result is:",bmi)
if bmi<18.5:
        print("you have under weight")
elif bmi>18.5 and bmi<24.9:
        print("you have a normal weight")
elif bmi>24.9 and bmi<29.9:
        print("you have a OverWeight")
else:
        print("You are suffering with Obesity")





        