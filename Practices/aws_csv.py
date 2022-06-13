import pandas as pd

csv_files = "D:\\Python\\confusion\Practices\\files\\aws-tags.csv"
csv_data = pd.read_csv(csv_files, engine="python", usecols=["UnBlendedCost", "ResourceId", "user_Project"])
for i in range(0, len(csv_data)):
    UnBlendedCost_data = csv_data["UnBlendedCost"][i]
    ResourceId_data = csv_data["ResourceId"][i]
    Project_data = csv_data["user_Project"][i]
    if "figure" in str(Project_data):
        print(UnBlendedCost_data)
        print(ResourceId_data)
        print(Project_data)