import pandas as pd
import timeit

df = pd.read_csv("resources/bikeshare-2/chicago.csv")
#print(df.head())  # start by viewing the first few rows of the dataset!
#print(df.columns)
#print(df.describe())
#print(df.info())
#print(df['End Station'].value_counts())
#print(df['End Station'].unique())
#print(len(df['End Station'].unique()))
# print(df.isnull())
#print(df.isnull().sum())
#%timeit
#print(df.isnull().any())
#print(df.isnull().any().any())
#print(df.isnull().values.sum())
#print(df.isnull().sum().sum())
#print(df.isnull().values.any())
#print(df.info())

#print(df['Start Time'])
#df['Start Time'] = pd.to_datetime(df['Start Time'])
#df['hour'] = df['Start Time'].dt.hour
# print(df['Start Time'].dt.hour)
# print(df['hour'])
#p = df['hour'].value_counts()
#print(p)
#print(p.index[0])

#p = df['hour'].mode()
#print(p)
#print(p[0])

#user_types = df['User Type'].value_counts()
#print(user_types)

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv("resources/bikeshare-2/" + CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #print(df['month'])
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['day_of_week_name'] = df['Start Time'].dt.weekday_name
    print(df['day_of_week_name'])
    #print(df['day_of_week'])
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df.month == month]

    print(df)
        # filter by day of week if applicable
    if day != 'all':
        weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week == weeks.index(day)]
        df = df[df.day_of_week_name == day.title()]

    return df


df = load_data('chicago', 'march', 'friday')
print(df)
