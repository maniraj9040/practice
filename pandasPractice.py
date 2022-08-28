import pandas as pd
import numpy as np


###################### series ################################

s = pd.Series([1, 2, 3, 4], index=("a", "b", "c", "d"))
print(s)

dic = {"a": 1, "b": 2, "c": 3, "d": 4}
s1 = pd.Series(dic, index=["b", "d", "e", "a", "c"])
print(s1)

s2 = pd.Series(5, index=["b", "d", "e", "a", "c"])
print(s2)
print(s2[:2])
print(s2[["c", "d", "a"]])

####################### end series ###########################
df = pd.DataFrame(np.random.randn(4, 3), columns=["col1", "col2", "col3"])
# print(df.to_string)

for key, value in df.iteritems():
    pass
    # print(key, value)

# print("=" * 40)

for row_index, row in df.iterrows():
    pass
    # print(row_index, row)
# print("=" * 40)

for row in df.itertuples():
    pass
    # print(row)