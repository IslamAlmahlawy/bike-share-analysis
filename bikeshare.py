import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
        if city in (CITY_DATA.keys()):
            break        
        print('Invalid city name please choose value from the provided cities!')

    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        filter = input("How do you want to filter the data (by month, day, both or none)? ").lower()
        if filter in ['month', 'day', 'both', 'none']:
            break
        print("Invalid filter selected please choose a filter from the provided list")

    month_filter_message = """
    Please select a month to filter by providing just the number
    1) January
    2) February
    3) March
    4) April
    5) May
    6) June
    """
    if filter in ['month', 'both']:
        while True:
            month = input(month_filter_message)
            if month.isnumeric() and int(month) <= 6:
                month = int(month)
                break
            print(f'{month} is invalid please select a number from 1 to 6 for the month to filter with!')
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_filter_message = """
    Please select a day to filter by providing just the number
    0) Monday
    1) Tuesday
    2) Wednesday
    3) Thursday
    4) Friday
    5) Saturday
    6) Sunday
    """
    if filter in ['day', 'both']:
        while True:
            day = input(day_filter_message)
            if day.isnumeric() and int(day) <= 6 and int(day) >= 0:
                day = int(day)
                break
            print(f'{day} is invalid please select a number from 1 to 7 for the day to filter with!')
    else:
        day = 'all'


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # get city file name
    city_file = CITY_DATA[city]

    # load the data in a pandas data frame
    df = pd.read_csv(city_file)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Add month and day columns to the dataframe
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # check if we will filter with month or not
    if month != 'all':
        # filter by month 
        df = df[df['month'] == month]

    # check if we will filter with day or not
    if day != 'all':
        # filter by day 
        df = df[df['day'] == day]

    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    month = df.month.mode()[0]
    print(f'The most common month is: {months[month-1]}')

    # TO DO: display the most common day of week    
    day = df['day_of_week'].mode()[0]
    print(f'The most common day of week is: {day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {hour}')

    print(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

