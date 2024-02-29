"""
 in windows we can access env. variables via:
 system proporties > advanced > environment variables
 under - system variables.
 and we can add a variable for ourselves to be used

 how is this done in python?
"""
import os # installing an operating system library(which is already in python)
stage = os.environ["STAGE"].upper() # this extracts the env. variable "stage"
# and converts it to uppercase

output = f"We're running in {stage}"
if stage.startswith("PROD"):
    output = "DANGER !!! - " + output

print(output)

# this will print an error, because there is no env. var. named "STAGE"!!
# so we need to create it via windows, like explained above
# and also because even if we did place stage in env. var. in windows
# it won't register in pycharm, so we have to reboot the editor.
# same with git bash

"""
also we can do something similar with getenv()
but if we delete the env.variable
it won't import it from the registery, but will
also CREATE it.
"""
stage2 = os.getenv("STAGE").upper()

output2 = f"We're running in {stage2}"
if stage2.startswith("PROD"):
    output2 = "DANGER !!! - " + output2

print(output2)