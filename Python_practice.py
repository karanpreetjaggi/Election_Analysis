counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


if "Arapahoe" in counties and "el paso" in counties:
   print("Arapahoe and el paso are in the list of counties.")
else:
    print("Arapahoe or el paso not in the list of counties.")

if "Arapahoe" in counties or "el paso" in counties:
    print("Arapahoe or el paso is in the list of counties.")
else:
    print("Arapahoe and el paso are not in the list of counties.")

if "Arapahoe" in counties and "El paso" not in counties:
   print("only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in te list of counties and El paso is not in the list of counties.")

for county in counties:
    print(county)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, voters)
voting_data = [{"county":"Arapahoe","registered voters":422829},
                {"county":"Denver","registered voters":463353},
                {"county":"Jefferson","registered voters":432438}]

for county_dic in voting_data:
     print(county_dic)
for i in range(len(voting_data)):
    print(voting_data[i])
for county_dict in voting_data:
 for values in county_dict.values():
    print(values)
for county_dict in voting_data:
    print(county_dict['registered voters'])
for county_dict in voting_data:
    print(county_dict['county'])
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county +"county has "+ str(voters) + "registered voters.")
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters.")


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
               {"county":"Denver", "registered_voters": 463353}, 
               {"county":"Jefferson", "registered_voters": 432438}]
for values, registered_voters in counties_dict.items():
    print(f"{county}) has {voters} registered voters.")