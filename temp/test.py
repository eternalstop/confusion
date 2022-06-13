import pandas as pd


result_list = []
file_name = "result.txt"
with open(file_name, "r") as f:
    lists = f.readlines()

for i in range(0, len(lists)):
    tmp_list = [j.strip() for j in lists[i].strip().split("|")][1:5]
    result_list.append(tmp_list)

columns = ["objectIndex", "max_jf", "can_rwIds", "ed_rwIds"]
dt = pd.DataFrame(result_list, columns=columns)
dt.to_excel("result_xlsx.xlsx", index=0)
dt.to_csv("result_csv.csv", index=0)
