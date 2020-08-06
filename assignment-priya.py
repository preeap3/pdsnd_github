import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    cities =('chicago','new york city','washington')
    while True:
        input_city = input('Please enter city name : chicago, new york city or washington? ').lower()
        if input_city in cities:
           break



    # TO DO: get user input for month (all, january, february, ... , june)
    months = {'January','February', 'March', 'April','May','June','July','August','September','October','November','December'}
    while True:
         input_month = input('Please enter month:').capitalize()
         if input_month in months:
            break
   
         

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days= {'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
    while True:
         input_day= input('Please enter the day you want information from:').lower()
         if input_day in days:
            break


    #print('-'*40)
    print("City is",input_city)
    print("Month of", input_month)
    print("Day:", input_day)

    return input_city, input_month, input_day


def load_data(input_city,input_month,input_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = input_city + ".csv"
    df = pd.read_csv(filename)
    #df = df.loc[df['Start Time'].dt.month == input_month]
    #df = df.loc[df['Start Time'].dt.day == input_day]
    #This code is to allow for filtering of user input for day and month

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("\nPopular month is %s" % popular_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startstation = df['Start Station'].mode()[0]
    print("The most commonly used start station: %s" % most_common_startstation)

    # TO DO: display most commonly used end station
    most_common_endstation = df['End Station'].mode()[0]
    print("The most commonly used end station: %s"% most_common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'] + df['End Station']
    most_frequent_combo = df['Start_End'].mode()[0]
    print("The most frequently used combination of start- and end-station:%s "% most_frequent_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total time of travel: ", total_travel_time)

    # TO DO: display mean travel time
    mean_traveltime = df["Trip Duration"].mean()
    print("The average travel-time: ", mean_traveltime)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count of user types: ",df["User Type"].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df:
        print("\nCounts of person's gender")
        print("Male: ", df.query("Gender == 'Male'").Gender.count())
        print("Female: ", df.query("Gender == 'Female'").Gender.count())


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Year of Birth" in df:
        print("\nEarliest year of birth: ", df["Year of Birth"].min())
        print("Most recent year of birth: ", df["Year of Birth"].max())
        print("Most common year of birth: ", df["Year of Birth"].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        input_city, input_month, input_day = get_filters()
        df = load_data(input_city, input_month, input_day)
      i = 0
      raw = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
      pd.set_option('display.max_columns',200)
     
       while True:            
        if raw == 'no':
          break
        print(df[i:i+5])
        raw = input('\nWould you like to see next rows of raw data?\n').lower()
        i += 5

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
