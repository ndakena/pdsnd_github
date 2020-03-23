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
    cities = ['new york city', 'chicago', 'washington']
    while True:
      city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n").lower()
      if city not in cities:
        print("_"*40)
        print("Oops, Looks like you entered a wrong city name!. Plry again.")
        print("_"*40)
        continue
      else:
        break

        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november', 'december']
    while True:
      month = (input("\nWhich month? all, january, february, march, ..., june\n ")).lower()
      if month not in months:
        print("\nOops! Seems like you entered a wrong month, please enter either 'all', or 'january',or 'february', or 'march', ..., or june ")
        continue
      else:
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days= ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday','sunday']
    while True:
      day = (input("\nWhich day? all, monday, tuesday, ... or sunday?")).lower()
      if day not in days:
        print("\nOops! Seems like you entered a wrong month, please enter either all, monday, tuesday, ... or sunday ")
        continue
      else:
        break

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
    df = pd.read_csv(CITY_DATA[city])

    # Now lets convert Start Time to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # creating a new column by extracting month and day of the week from Start Time.

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Now lets filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# Create a new dataframe with the month filter
        df = df[df['month'] == month]
       

    # Now lets filter by day of week
    if day != 'all':
        # Create a new dataframe with the day of week filter
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print('The most common Month is:              ', month)
    # TO DO: display the most common day of week
    Most_common_day = df['day_of_week'].mode()[0]
    print('Most common Week day:     ', Most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Most_common_hour = df['hour'].mode()[0]
    print('Most common Start hour is:', Most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_used_start_station = df['Start Station'].value_counts().idxmax() # get most commonly used start station
    
    print('The most commonly used start station: ', Most_used_start_station)

    # TO DO: display most commonly used end station
    ## get most commonly used start station
    Most_used_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station: ', Most_used_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    freq_combine_stations = df['Start Station'] + "*" + df['End Station']
    most_common_station = freq_combine_stations.value_counts().idxmax()
    most_common_station_0 = most_common_station.split('*')[0]
    most_common_station_1 = most_common_station.split('*')[1]
    print('Most frequent used combinations are:\n{} to\n{} '.format(most_common_station_0, most_common_station_1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_duration = sum(df['Trip Duration'])
    Total_Travel_duration = Total_Travel_duration/86400
    print('The total trip duration is {} days'.format(Total_Travel_duration))

    # TO DO: display mean travel time
    mean_travel_duration = int(df['Trip Duration'].mean())
    mean_travel_duration = mean_travel_duration/60
    print('The mean travel duration is {} Minutes:'.format(mean_travel_duration))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
          gender_count = df['Gender'].value_counts()
          print(gender_count)
    else:
          print("No gender found for the month!")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: 
        print("\nEarliest year of birth: " + str(df['Birth Year'].min()))
        print("\nMost recent year of birth: " + str(df['Birth Year'].max()))
        print("\nMost common year of birth: " + str(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    rows = 5

    start = 0
    print('\n Would you like to see some raw data?')
    end = rows - 1
    while True:
        raw_data = input('      (yes or no):  ')
        if raw_data.lower() == 'yes':
            print('\n    Displaying rows {} to {}:'.format(start + 1, end + 1))

            print('\n', df.iloc[start : end + 1])
            start += rows
            end += rows

            print('\n Would you like to see the next {} rows?'.format(rows))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
