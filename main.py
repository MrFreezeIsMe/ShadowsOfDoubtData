import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('PLACE YOUR FILEPATH HERE')

allValues = df[(df.Disk>=0)]
#print(a)

disksAppear = df[(df.Disk>0)]
#print(b)

averageFee = allValues["Fee"].mean()
averageFee = averageFee-(averageFee%50)
print(averageFee)


d = allValues.sort_values("Fee")
#print(d)

e = d.groupby("Fee").count()
#print(e)

f = disksAppear.sort_values("Disk")
#print(f)

g = f.groupby("Disk").count()
print(g)

averageOccurance = e["Disk"].mean()
print(averageOccurance)

averageOccuranceDisk = g["Contract"].mean()


c = allValues.sort_values("Contract")
contracts = c.groupby("Contract").count()

averageOccuranceContract = contracts["Fee"].mean()

x1 = allValues[(allValues.Contract=="Arrest")]
Arrest = x1["Fee"].mean()
x2 = allValues[(allValues.Contract=="Humiliate")]
Humiliate = x2["Fee"].mean()
x3 = allValues[(allValues.Contract=="Investigate Infidelity")]
InvestigateInfidelity = x3["Fee"].mean()
x4 = allValues[(allValues.Contract=="Photograph")]
Photograph = x4["Fee"].mean()
x5 = allValues[(allValues.Contract=="Stolen Item")]
StolenItem = x5["Fee"].mean()
x6 = allValues[(allValues.Contract=="Theft")]
Theft = x6["Fee"].mean()
x7 = allValues[(allValues.Contract=="Vandalism")]
Vandalism = x7["Fee"].mean()

ArrestMn = x1["Fee"].min()
HumiliateMn = x2["Fee"].min()
InvestigateInfidelityMn = x3["Fee"].min()
PhotographMn = x4["Fee"].min()
StolenItemMn = x5["Fee"].min()
TheftMn = x6["Fee"].min()
VandalismMn = x7["Fee"].min()

ArrestMx = x1["Fee"].max()
HumiliateMx = x2["Fee"].max()
InvestigateInfidelityMx = x3["Fee"].max()
PhotographMx = x4["Fee"].max()
StolenItemMx = x5["Fee"].max()
TheftMx = x6["Fee"].max()
VandalismMx = x7["Fee"].max()



contractsPayout = {
    'Contract':["Arrest","Humiliate","Investigate","Photograph","Stolen Item","Theft","Vandalism"],
    'Average Fee':[Arrest,Humiliate,InvestigateInfidelity,Photograph,StolenItem,Theft,Vandalism]
}

contractsPayoutMn = {
    'Contract':["Arrest","Humiliate","Investigate","Photograph","Stolen Item","Theft","Vandalism"],
    'Average Fee':[ArrestMn,HumiliateMn,InvestigateInfidelityMn,PhotographMn,StolenItemMn,TheftMn,VandalismMn]
}

contractsPayoutMx = {
    'Contract':["Arrest","Humiliate","Investigate","Photograph","Stolen Item","Theft","Vandalism"],
    'Average Fee':[ArrestMx,HumiliateMx,InvestigateInfidelityMx,PhotographMx,StolenItemMx,TheftMx,VandalismMx]
}

contractPayout = pd.DataFrame(contractsPayout)
contractPayoutMn = pd.DataFrame(contractsPayoutMn)
contractPayoutMx = pd.DataFrame(contractsPayoutMx)

#print(contractPayout,contractPayoutMn,contractPayoutMx)


sns.set_style("darkgrid")


Fees = sns.catplot(x="Fee", y="Disk", data=e, kind="bar", hue="Disk", palette="viridis")
Fees.set_axis_labels("Fee", "How often")
plt.axhline(averageOccurance, color="red", linestyle="--")
plt.axvline((averageFee-300)/50, color="green", linestyle="--")
plt.xticks(rotation=45)


Disks = sns.catplot(x="Disk", y="Contract", data=g, kind="bar", hue="Contract", palette="viridis")
Disks.set_axis_labels("Disk", "How often")
plt.axhline(averageOccuranceDisk, color="red", linestyle="--")
plt.xticks(rotation=45)


Contracts = sns.catplot(x="Contract", y="Fee", data=contracts, kind="bar", hue="Fee", palette="viridis")
Contracts.set_axis_labels("Contract", "How often")
plt.axhline(averageOccuranceContract, color="red", linestyle="--")
plt.xticks(rotation=45)


ax = plt.subplots()
ax = sns.barplot(x=contractPayout["Contract"], y=contractPayout["Average Fee"], hue=contractPayout["Average Fee"], palette="viridis")
ax = sns.boxplot(x=contractPayoutMn["Contract"], y=contractPayoutMn["Average Fee"])
ax = sns.boxplot(x=contractPayoutMx["Contract"], y=contractPayoutMx["Average Fee"])
plt.axhline(averageFee, color="red", linestyle="--")
plt.xticks(rotation=45)

plt.show()


#avgFee = len(a)
rowsTotal = len(allValues)
rowsWith = len(disksAppear)
rowsWithout = len(disksAppear) - len(allValues)
chanceDisk = rowsWith/rowsTotal

print("A disk is rewarded around", chanceDisk, "% of the time")
