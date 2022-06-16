import pandas as pd

path = "./AzureDevices27522/Windows/unknown/"
all_data = pd.read_csv(path + "unknown.csv", delimiter=";")


# WindowsPhone = pd.DataFrame()
# IPhone = pd.DataFrame()
# iPhone = pd.DataFrame()
# iPad = pd.DataFrame()
# iOS = pd.DataFrame()
# AndroidEnterprise = pd.DataFrame()
# Unknown = pd.DataFrame()
# AndroidForWork = pd.DataFrame()
# Android = pd.DataFrame()
# nan = pd.DataFrame()
# windows = pd.DataFrame()

counter = 0

lst = []

# for i in all_data["operatingSystem"]:
    # i = str(i)
    # if i == "WindowsPhone":
    #   WindowsPhone = WindowsPhone.append(all_data.loc[[counter]])
    #   lst.append(lst)
    # if i.upper() == "IPAD":
    #     iPad = iPad.append(all_data.loc[[counter]])
    #     lst.append(lst)
    # if i == "iOS":
    #     iOS = iOS.append(all_data.loc[[counter]])
    #     lst.append(lst)
    # if i == "AndroidEnterprise":
    #     AndroidEnterprise = AndroidEnterprise.append(all_data.loc[[counter]])
    #     lst.append(lst)
    # if i == "Unknown":
    #     Unknown = Unknown.append(all_data.loc[[counter]])
    #     lst.append(lst)
    # if i == "AndroidForWork":
    #     AndroidForWork = AndroidForWork.append(all_data.loc[[counter]])
    #     lst.append(lst)
    # if i == "Android":
    #     Android = Android.append(all_data.loc[[counter]])
    #     lst.append(lst)
    # if i == "nan":
    #     nan = nan.append(all_data.loc[[counter]])
    #     lst.append(lst)
    # counter += 1
    # if i.upper() == "WINDOWS":
    #     print(i)
    #     windows = windows.append(all_data.loc[[counter]])
    #     lst.append(lst)
    # counter += 1

# counter = 0

# df = pd.DataFrame()

# for y in all_data["isManaged"]:
#     print(y)
#     if y == False:
#         df = df.append(all_data.loc[[counter]])
#     counter += 1

df = pd.DataFrame()

for y in all_data["approximateLastSignInDateTime"]:
    try:
        x = y[0:4]
        y = int(x)
        if y <= 2020:
            print(all_data.loc[[counter]])
            df = df.append(all_data.loc[[counter]])
    except:
        i = 0
    counter += 1

# print(oldvdi)
# WindowsPhone.to_csv(path + "WindowsPhone.csv", sep=";")
# iPhone.to_csv(path + "iPhone.csv", sep=";")
# iPad.to_csv(path + "iPad.csv", sep=";")
# iOS.to_csv(path + "iOS.csv", sep=";")
# AndroidEnterprise.to_csv(path + "AndroidEnterprise.csv", sep=";")
# Unknown.to_csv(path + "Unknown.csv", sep=";")
# AndroidForWork.to_csv(path + "AndroidForWork.csv", sep=";")
df.to_csv(path + "before2021.csv", sep=";")


# oldvdi.to_csv(path + "Android/odw10.csv", sep=";")

# print(len(lst), counter)