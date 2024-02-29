# create a function by "def <name of function>(<argument if needed) : "
def _helloworld():
    print("hello, World!")
#to call the function
_helloworld()

# function that accepts parameter which is name
def print_name(name):
    print(f"Name is {name}")

print_name("Ariel")

output = print_name("Mushy Brain")

def add_two(num):
    return num+2

result = add_two(3)
print(result)

#BMI function weight vs height

def gather_info():
    height = float(input("what is your height? (inches or meters): "))
    weight = float(input("what is your weight? (kg or pound): "))
    system = input ("are your measurements in meteric(kg/meter) or imperial(pound/inch)? ").lower().strip()
    #.lower() = lowercase, strip()= removes spaces
    return (height, weight, system)

# this ^^ function only gathers info. 


def calculate_bmi(weight, height, system = 'metric'):
    """
    Return the Body Mass Index (BMI) for the
    given weight, height, and measurement system
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = (weight / (height ** 2)) * 703
    return bmi
while True: # in case i didn't put values
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, height=height, system='imperial')
        print(f"your BMI is:{bmi}")
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(f"your BMI is:{bmi}")
        break
    else:
        print("ERROR : Unknown measurement system, please use imperial or metric")
#print(f"Your BMI is:{calculate_bmi(weight, height, system)}")
