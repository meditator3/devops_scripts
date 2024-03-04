"""
 in windows we can access env. variables via:
 system proporties > advanced > environment variables
 under - system variables.
 and we can add a variable for ourselves to be used

 how is this done in python?
"""
import os # installing an operating system library(which is already in python)




"""
also we can do something similar with getenv()
but if we delete the env.variable
it won't import it from the registery, but will
also CREATE it.
"""
stage2 = os.getenv("STAGE", "dev").upper() # this removes errors using getenv
# by adding actual env. variable with the value dev

output2 = f"We're running in {stage2}"
if stage2.startswith("PROD"):
    output2 = "DANGER !!! - " + output2

print(output2)

# in current env. var i changed stage to PRODUCTION.
# can change value to dev, to see no warning