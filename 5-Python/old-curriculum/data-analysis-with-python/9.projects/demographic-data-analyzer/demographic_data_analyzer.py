import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    is_man = df['sex'] == 'Male'    # check if Male
    men = df.loc[is_man]            # select lines where 'sex' == 'Male'
    average_age_men = round(men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_levels = ['Bachelors', 'Masters', 'Doctorate'] 
    has_higher_education = df['education'].isin(higher_education_levels)
    higher_education = df[has_higher_education]
    lower_education = df[~has_higher_education]

    # percentage with salary >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    is_rich = df['salary'] == '>50K'
    
    people_by_country = df.groupby('native-country').size()
    high_income_by_country = df[is_rich].groupby('native-country').size()
    high_income_by_country = high_income_by_country.reindex(people_by_country.index, fill_value=0)
    high_income_percentage = round(high_income_by_country / people_by_country * 100, 1)
    
    highest_earning_country = high_income_percentage.idxmax()
    highest_earning_country_percentage = high_income_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.
    is_from_india = df['native-country'] == 'India'
    india_high_earners = df[is_rich & is_from_india]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
