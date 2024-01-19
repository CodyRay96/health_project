import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st


insurance = pd.read_csv('insurance.csv')

#print(insurance.head())

mean = insurance['bmi'].mean()
#print(mean)

smokers = insurance['smoker'].value_counts().get('yes', 0)
#print('total smokers', smokers)

insurance['charges'] = insurance['charges'].astype(int)
#print(insurance['charges'].dtype)


insurance['children'] = insurance['children'].astype(int)
#print(insurance['children'].dtype)

insurance_df = pd.DataFrame(insurance)

# southwest = []
# southeast = []
# northwest = []
# northeast = []

# for i, row in insurance.iterrows():
#     if row['region'] == 'northwest':
#         northwest.append(row)
#     elif row['region'] == 'northeast':
#         northeast.append(row)
#     elif row['region'] == 'southwest':
#         southwest.append(row)
#     else:
#         southeast.append(row)

# southwest_df = pd.DataFrame(southwest)
# southeast_df = pd.DataFrame(southeast)
# northwest_df = pd.DataFrame(northwest)
# northeast_df = pd.DataFrame(northeast)

# #mean charges for each region
# mean_charges_southwest = round(southwest_df['charges'].mean(), 2)
# mean_charges_southeast = round(southeast_df['charges'].mean(), 2)
# mean_charges_northwest = round(northwest_df['charges'].mean(), 2)
# mean_charges_northeast = round(northeast_df['charges'].mean(), 2)

# #mean children for each region
# mean_children_southwest = round(southwest_df['children'].mean(), 2)
# mean_children_southeast = round(southeast_df['children'].mean(), 2)
# mean_children_northwest = round(northwest_df['children'].mean(), 2)
# mean_children_northeast = round(northeast_df['children'].mean(), 2)

# Group by 'children' and calculate mean charges
grouped_children_charges_df = insurance_df.groupby(['children', 'region'])['charges'].mean().reset_index()


# Print mean charges for each group
for i, row in grouped_children_charges_df.iterrows():
    print(f"Mean charges for {row['children']} children in {row['region']}: {round(row['charges'], 2)}")

#Round the numbers before the dataframe
grouped_children_charges_df['charges'] = grouped_children_charges_df['charges'].round(2)

children_pivot_df = grouped_children_charges_df.pivot(index = 'region', columns = 'children', values = 'charges').reset_index()

children_pivot_df = children_pivot_df.fillna(0)

children_pivot_df.columns = ['region', '0 Kids', '1 Kids', '2 Kids', '3 Kids', '4 Kids', '5 Kids']

print(children_pivot_df)



children_pivot_df.to_csv('charges_on_children.csv', index = False)











###############################################################################################################################
# Group by 'smoker' and calculate mean charges
grouped_smoker_charges_df = insurance_df.groupby(['smoker', 'region'])['charges'].mean().reset_index()

# Print mean charges for each group
for i, row in grouped_smoker_charges_df.iterrows():
    print(f"Mean charges for {row['smoker']} smoke in {row['region']}: {round(row['charges'], 2)}")

#Round the numbers before the dataframe
grouped_smoker_charges_df['charges'] = grouped_smoker_charges_df['charges'].round(2)

# Pivot the DataFrame
smoker_pivoted_df = grouped_smoker_charges_df.pivot(index='region', columns='smoker', values='charges').reset_index()

# Fill NaN values with 0
smoker_pivoted_df = smoker_pivoted_df.fillna(0)

# Rename the columns to 'no' and 'yes'
smoker_pivoted_df.columns = ['region', 'no', 'yes']

# Print the pivoted DataFrame
print(smoker_pivoted_df)

# Export the pivoted data to a CSV file
smoker_pivoted_df.to_csv('charges_on_smoker.csv', index=False)



#FIRST ATTEMPT (long and ugly but works)
    
# sw_no_kids = []
# sw_kids1 = []
# sw_kids2 = []
# sw_kids3 = []
# sw_kids4 = []
# sw_kids5 = []

# for i, row in southwest_df.iterrows():
#     if row['children'] == 1:
#         sw_kids1.append(row)
#     elif row['children'] == 2:
#         sw_kids2.append(row)
#     elif row['children'] == 3:
#         sw_kids3.append(row)
#     elif row['children'] == 4:
#         sw_kids4.append(row)
#     elif row['children'] == 5:
#         sw_kids5.append(row)
# else:
#         sw_no_kids.append(row)
        


# sw_no_kids_df = pd.DataFrame(sw_no_kids)
# sw_kids1_df = pd.DataFrame(sw_kids1)
# sw_kids2_df = pd.DataFrame(sw_kids2)
# sw_kids3_df = pd.DataFrame(sw_kids3)
# sw_kids4_df = pd.DataFrame(sw_kids4)
# sw_kids5_df = pd.DataFrame(sw_kids5)
# print(sw_kids5)
# print(round(sw_kids1_df['charges'].mean(), 2))
# print(round(sw_kids2_df['charges'].mean(), 2))
# print(round(sw_kids3_df['charges'].mean(), 2))
# print(round(sw_kids4_df['charges'].mean(), 2))
# print(round(sw_kids5_df['charges'].mean(), 2))



#mean age for each region
# mean_age_southwest = round(southwest_df['age'].mean(), 2)
# mean_age_southeast = round(southeast_df['age'].mean(), 2)
# mean_age_northwest = round(northwest_df['age'].mean(), 2)
# mean_age_northeast = round(northeast_df['age'].mean(), 2)

# #mean BMI for each region
# mean_bmi_southwest = round(southwest_df['bmi'].mean(), 2)
# mean_bmi_southeast = round(southeast_df['bmi'].mean(), 2)
# mean_bmi_northwest = round(northwest_df['bmi'].mean(), 2)
# mean_bmi_northeast = round(northeast_df['bmi'].mean(), 2)


# #mean smokers for each region
# southwest_smokers = southwest_df['smoker'].value_counts().get('yes', 0)
# southeast_smokers = southeast_df['smoker'].value_counts().get('yes', 0)
# northeast_smokers = northeast_df['smoker'].value_counts().get('yes', 0)
# northwest_smokers = northwest_df['smoker'].value_counts().get('yes', 0)

# mean_smoker_southwest = round((southwest_smokers/len(southwest_df)*100), 2)
# mean_smoker_southeast = round((southeast_smokers/len(southeast_df)*100), 2)
# mean_smoker_northwest = round((northwest_smokers/len(northwest_df)*100), 2)
# mean_smoker_northeast = round((northeast_smokers/len(northeast_df)*100), 2)



# #mean charges for male and female in each region
# southwest_male = southwest_df['sex'].value_counts().get('male', 0)
# southeast_male = southeast_df['sex'].value_counts().get('male', 0)
# northeast_male = northeast_df['sex'].value_counts().get('male', 0)
# northwest_male = northwest_df['sex'].value_counts().get('male', 0)

# mean_male_southwest = round((southwest_male/len(southwest_df)*100), 2)
# mean_male_southeast = round((southeast_male/len(southeast_df)*100), 2)
# mean_male_northwest = round((northwest_male/len(northwest_df)*100), 2)
# mean_male_northeast = round((northeast_male/len(northeast_df)*100), 2)

# southwest_male_charges = southwest_df.loc[southwest_df['sex'] == 'male', 'charges'].mean()
# southwest_female_charges = southwest_df.loc[southwest_df['sex'] == 'female', 'charges'].mean()

# print('male charges', southwest_male_charges)
# print('female charges', southwest_female_charges)

# print('mean charges northeast', mean_charges_northeast)
# print('mean children northeast', mean_children_northeast)

#print(f'northeast mean smokers {mean_smoker_northeast}%')
# print('northeast male population', mean_male_northeast)



#print(insurance['children'].max())
