data_in_colume = ''' ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 
'new_deaths', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 
'new_deaths_per_million', 'new_tests', 'total_tests', 'total_tests_per_thousand', 'new_tests_per_thousand',
 'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_per_case', 'positive_rate', 'tests_units', 
 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 
 'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 
 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy']'''

import csv
import collections as e
with open('D:/csv_file/covid_dat2.csv') as file_object:
    data = csv.reader(file_object)
    next(data)
    all_data = []
    for each in data:
        all_data.append({"country":each[2], "total_case":each[4], "date":each[3], "total_death":each[6]})
print(len(all_data))
# print(all_data[12999])
#
#
# dict_india = e.defaultdict(list)
# for i in all_data:
#     dict_india[i['country']].append(i["total_case"])
# dict_india['India'].append('123')
# print(len(dict_india['India']))