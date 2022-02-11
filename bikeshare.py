'''
Created on Jan 19, 2022

@author: IsmailZinhom
'''
import time
import pandas as pd
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
USER_CITY_INPIT =["chicago", "new york", "washington"]
USER_MONTH_INPUT =["january", "february", "march", "april", "may", "june"]
USER_DAY_INPUT = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday","friday"]
USER_FILTER_INPUT =["month", "day", "both", "none"]

def read_city():
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    user_choice= input("Would you like to see data for Chicago, New York, or Washington? ")
    if user_choice.lower() in USER_CITY_INPIT:
        return user_choice.lower()
    else:
        print("unrecognized choice for city please try again")
        return read_city()

def read_month():
    # TO DO: get user input for month (all, january, february, ... , june)
    user_choice= input('Which month - January, February, March, April, May, or June?')
    if user_choice.lower() in USER_MONTH_INPUT:
        return user_choice.lower()
    else:
        print("unrecognized choice for month please try again")
        return read_month()
        
def read_day():
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    user_choice= input('Which day - saturday, sunday, monday, tuesday, Wednesday, thursday or friday?')
    if user_choice.lower() in USER_DAY_INPUT:
        return user_choice.lower()
    else:
        print("unrecognized choice for day please try again")
        return read_day()
def read_filter_type():
    user_choice=input("Would you like to filter the data by month, day, both, or none(not at all)?")
    if user_choice.lower() in USER_FILTER_INPUT:
        return user_choice.lower()
    else:
        print("unrecognized choice for filter please try again")
        return read_filter_type()
def resume_exit():
    user_choice=input('\nWould you like to restart? Enter yes or no.\n')
    if user_choice.lower()=="yes":
        return "yes"
    elif user_choice.lower()=="no":
        return "no"
    else:
        print("unrecognized choice!...")
        return resume_exit()
        
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month, day ="", ""
    city= read_city() 
    user_choice = read_filter_type()
    if user_choice=="month":
        month = read_month().title()
    elif user_choice=="day":
        day = read_day().title()
    elif user_choice=="both":
        month = read_month().title()
        day = read_day().title()
    else:
        return city, month, day

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
    file_reader = pd.read_csv(CITY_DATA[city])
    if month == "" and day =="":
        return file_reader
       
    elif month !="" and day=="":
        return file_reader[pd.to_datetime(file_reader["Start Time"]).dt.month_name()==month]
        
    elif month =="" and day!="":
        return file_reader[pd.to_datetime(file_reader["Start Time"]).dt.day_name()==day]
        
    else:
        data = file_reader[pd.to_datetime(file_reader["Start Time"]).dt.month_name()==month]
        return data[pd.to_datetime(data["Start Time"]).dt.day_name()==day]
        


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
        
    # TO DO: display the most common month
    most_month=pd.to_datetime(df["Start Time"]).dt.month_name()
    print("the most common month is: {}".format(most_month.value_counts().idxmax()))

    # TO DO: display the most common day of week
    most_day = pd.to_datetime(df["Start Time"]).dt.day_name()
    print("the most common day is: {}".format(most_day.value_counts().idxmax()))

    # TO DO: display the most common start hour
    most_hour = pd.to_datetime(df["Start Time"]).dt.hour
    print("the most common hour is: {}".format(most_hour.value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
        
    # TO DO: display most commonly used start station
    print("the most start station is: {}".format(df["Start Station"].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print("the most End station is: {}".format(df["End Station"].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    print("the most trip from Start to End: {}".format(df[["Start Station","End Station"]].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
        
    # TO DO: display total travel time
    print("Total travel time: {}".format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("Average travel time: {}".format(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    print("user type count:\n{}".format(df["User Type"].value_counts()))

    # TO DO: Display counts of gender
    try:
        print("gender count:\n{}".format(df["Gender"].value_counts()))
    except:
        print("no data a for gender to show!...")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("the earliest birth year is: {}".format(int(df["Birth Year"].dropna(axis=0).min())))
        print("the recent birth year is: {}".format(int(df["Birth Year"].dropna(axis=0).max())))
        print("the most common birth year is: {}".format(int(df["Birth Year"].dropna(axis=0).value_counts().idxmax())))
    except:
        print("no data a for birth year to show!...")    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_trip_information(df):
    count = 6
    try:
        for i in range(0,5):
            print(df.iloc[i,:])
            print("-"*50)
        while True:
            user_choice = input("do you want new trip individual information? yes or no...")
            if user_choice.lower()=="yes":
                print(df.iloc[count,:])
                count+=1
                print("-"*50)
            elif user_choice.lower()=="no":
                break
            else:
                print("unrecognized answer!...")
    except :
        print("no more data to view...")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_trip_information(df)
        restart = resume_exit()
        if restart.lower() == 'no':
            break

if __name__ == "__main__":
    main()