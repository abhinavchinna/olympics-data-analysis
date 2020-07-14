# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data=pd.read_csv(path)
data.rename(columns={"Total":"Total_Medals"},inplace=True)
print(data.head(10))
# Summer or Winter
data["Better_Event"]=np.where(data["Total_Summer"]==data["Total_Winter"],"Both",np.where(data["Total_Summer"]>data["Total_Winter"],"Summer","Winter"))
better_event=(data["Better_Event"].value_counts()).index[0]

# Top 10
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)
def top_ten(df,col):
    countrylist=list(df.nlargest(10,col)["Country_Name"])
    return countrylist
top_10_summer=top_ten(top_countries,"Total_Summer")
top_10_winter=top_ten(top_countries,"Total_Winter")
top_10=top_ten(top_countries,"Total_Medals")
common=[]
for i in top_10_summer:
    if i in top_10_winter and i in top_10:
        common.append(i)
#Plotting Top 10
summer_df=data[data["Country_Name"].isin(top_10_summer)]
winter_df=data[data["Country_Name"].isin(top_10_winter)]
top_df=data[data["Country_Name"].isin(top_10)]
summer_df.plot.bar(x="Country_Name",y="Total_Summer")
winter_df.plot.bar(x="Country_Name",y="Total_Winter")
top_df.plot.bar(x="Country_Name",y="Total_Medals")
#Top performing country(Gold)
summer_df["Golden_Ratio"]=summer_df["Gold_Summer"]/summer_df["Total_Summer"]
winter_df["Golden_Ratio"]=winter_df["Gold_Winter"]/winter_df["Total_Winter"]
top_df["Golden_Ratio"]=top_df["Gold_Total"]/top_df["Total_Medals"]
k1=summer_df[summer_df["Golden_Ratio"]==summer_df["Golden_Ratio"].max()]
summer_country_gold=k1["Country_Name"].values[0]
summer_max_ratio=k1["Golden_Ratio"].values[0]

k2=winter_df[winter_df["Golden_Ratio"]==winter_df["Golden_Ratio"].max()]
winter_country_gold=k2["Country_Name"].values[0]
winter_max_ratio=k2["Golden_Ratio"].values[0]

k3=top_df[top_df["Golden_Ratio"]==top_df["Golden_Ratio"].max()]
top_country_gold=k3["Country_Name"].values[0]
top_max_ratio=k3["Golden_Ratio"].values[0]
#Best in the world
data_1=data.drop(data.tail(1).index,inplace=False)
data_1["Total_Points"]=data_1["Gold_Total"]*3 +data_1["Silver_Total"]*2 +data_1["Bronze_Total"]
k=data_1[data_1["Total_Points"]==data_1["Total_Points"].max()]
best_country=k["Country_Name"].values[0]
most_points=k["Total_Points"].values[0]
#plot for the best
best=data[data["Country_Name"]==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)


