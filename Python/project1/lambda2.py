#Lambda here  is just lowering case of the names in the converted list/to a table

import pandas as pd # provides better repesentation of data
df = pd.DataFrame(
    {"name": ["IBRAHIM", "SEGUN", "YUSUF", "DARE", "BOLA", "SOKUNBI"],
     "score": [50, 32, 45 ,45, 23, 45]
     }
)
print(df) # (pandas)this converts the dictionary into a table with id to each

df["lower_name"] = df["name"].apply(lambda x: x.lower())
# this also use of lambda
print(df["score"])
