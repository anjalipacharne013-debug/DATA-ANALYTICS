import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.csv")

    # 1. Race count
    race_count = df['race'].value_counts().to_dict()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. % with Bachelors
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Higher education rich
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[higher_edu]['income'] == '>50K').mean() * 100, 1
    )

    # 5. Lower education rich
    lower_edu = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_rich = round(
        (df[lower_edu]['income'] == '>50K').mean() * 100, 1
    )

    # 6. Min work hours
    min_work_hours = df['hours.per.week'].min()

    # 7. % rich among min workers
    min_workers = df[df['hours.per.week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['income'] == '>50K').mean() * 100, 1
    )

    # 8. Country with highest % >50K
    country_stats = df.groupby('native.country')['income'].apply(
        lambda x: (x == '>50K').mean() * 100
    )

    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)

    # 9. Top occupation in India
    top_IN_occupation = (
        df[(df['native.country'] == 'India') & (df['income'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    return {
    'race_count': race_count,
    'average_age_men': float(average_age_men),
    'percentage_bachelors': float(percentage_bachelors),
    'higher_education_rich': float(higher_education_rich),
    'lower_education_rich': float(lower_education_rich),
    'min_work_hours': int(min_work_hours),
    'rich_percentage': float(rich_percentage),
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': float(highest_earning_country_percentage),
    'top_IN_occupation': top_IN_occupation
}
print(calculate_demographic_data())

'''Output 
{'race_count': {'White': 27816, 'Black': 3124, 'Asian-Pac-Islander': 1039, 'Amer-Indian-Eskimo': 311, 'Other': 271},
'average_age_men': 39.4,
'percentage_bachelors': 16.4, 
'higher_education_rich': 46.5,
'lower_education_rich': 17.4,
'min_work_hours': 1,
'rich_percentage': 10.0,
'highest_earning_country': 'Iran',
'highest_earning_country_percentage': 41.9,
'top_IN_occupation': 'Prof-specialty'}
'''