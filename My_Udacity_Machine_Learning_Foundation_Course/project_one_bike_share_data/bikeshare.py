import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTH_NAMES = ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']

WEEK_NAMES = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Global data
city_data_loaded = False
month_data_loaded = False
week_data_loaded = False
data_frame = None
local_data_frame = None
city = "chicago"
week_day = "All"
month = "All"


def get_selection(text_for, selection_list):
    """

    :param text_for: The name of the category to be selected (city, month, week day)
    :param selection_list: A list containing valid values for the selection.
    :return: returns the selected value from the selection_list
    """

    selection = None
    while not selection:
        try:
            selection = input("\nPlease input the {} for which data is required.\n [{}]: "
                              .format(text_for, ", ".join(selection_list)))

            if text_for.lower() == "city":
                selection = selection.lower()
            else:
                selection = selection.title()

            if selection not in selection_list:
                selection = None
                raise ValueError()

        except (ValueError, KeyError):
            print("\nUnfortunately, we do not know or have the data for the provided input. ")
            pass
    return selection


def load_week_day():
    global local_data_frame, week_data_loaded

    if not week_data_loaded:
        week_data_loaded = True
        if week_day.lower() != "all":
            if local_data_frame is None:
                local_data_frame = data_frame
            local_data_frame = local_data_frame[local_data_frame.day_of_week == week_day.title()]


def change_week_day():
    global week_day, week_data_loaded

    week_data_loaded = False
    week_day = get_selection("Week day", WEEK_NAMES)
    load_week_day()

    return week_day


def load_month():
    global local_data_frame, month_data_loaded

    if not month_data_loaded:
        month_data_loaded = True
        if month.lower() != "all":
            # print(data_frame['month'])
            # print('+'*60)
            # if local_data_frame:
            #    print(local_data_frame['month'])
            # print('-'*60)
            local_data_frame = data_frame[data_frame.month == MONTH_NAMES.index(month.title())]
            # print(local_data_frame.describe())
            # print(local_data_frame['month'])
            # print('+' * 60)
            # print(data_frame['month'])
            # print('+'*60)

        else:
            local_data_frame = data_frame


def change_month():
    global month, month_data_loaded

    month_data_loaded = False
    min_month = data_frame.month.min()
    max_month = data_frame.month.max()
    available_months = MONTH_NAMES[min_month:max_month + 1]
    available_months.insert(0, "All")
    month = get_selection("Month", available_months)

    load_month()
    return month


def load_city_data():
    """
    Loads data for the specified city and filters by month and day (if applicable) into global variable data_frame.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        None
    """

    global data_frame

    data_frame = pd.read_csv("resources/bikeshare-2/" + CITY_DATA[city.lower()])

    # Drop all rows whose 'Start Time' or "End Time' or 'Start Station' or 'End Station' have no values
    data_frame.dropna(subset=['Start Time', 'End Time', 'Start Station', 'End Station'], inplace=True)

    # print(data_frame.columns)

    data_frame['Start Time'] = pd.to_datetime(data_frame['Start Time'])
    # data_frame['End Time'] = pd.to_datetime(data_frame['End Time'])
    data_frame['month'] = data_frame['Start Time'].dt.month
    data_frame['day_of_week'] = data_frame['Start Time'].dt.weekday_name
    data_frame['hour'] = data_frame['Start Time'].dt.hour


def load_default_city_data():
    global city_data_loaded

    if not city_data_loaded:
        city_data_loaded = True
        print("\nSelected city: {}.\nLoading data for city: {}...".format(city, city))
        load_city_data()


def change_city():
    global city, city_data_loaded
    city_data_loaded = False
    city = get_selection("City", list(CITY_DATA.keys()))
    load_default_city_data()


def prompt_user():
    """
    Common function to take user choice for city, month and day including error checking

    :return: the final user selection of city, month and day
    """
    global city, month, week_day, city_data_loaded, month_data_loaded, week_data_loaded

    while True:
        print("\n")
        print('-' * 40)
        print("1. City: {}".format(city))
        print("2. Month: {}".format(month))
        print("3. Week day: {}".format(week_day))

        selection = input("\nTo change any of the values above, please input their corresponding number followed by "
                          "<enter> key or any other key to continue with the above selections: ")

        # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        if selection == "1":
            change_city()
            # If month is not set to "all" force the user to change the selection based on the available months' data
            # for the selected city.
            if month.lower() != "all":
                month = None

        # Get user input for month (all, january, february, ... , june)
        elif selection == "2" or not month:
            month_data_loaded = False
            load_default_city_data()

            if not month:
                print("\nSince the city selection is changed after month selection, month needs to be re-selected "
                      "based on the available list of months' data under the selected city.")
            # display month
            month = change_month()

        # Get user input for day of week (all, monday, tuesday, ... sunday)
        elif selection == "3":
            week_data_loaded = False
            load_default_city_data()
            week_day = change_week_day()

        else:
            # load csv file if not already loaded
            load_default_city_data()
            load_month()
            load_week_day()

            break


def time_stats():
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # print(data_frame.month.value_counts())
    pd.options.display.max_columns = data_frame.shape[1]
    # print(data_frame.describe(include='all'))
    # print(local_data_frame.describe(include='all'))
    # print(data_frame.describe(include=['day_of_week', 'month', 'hour']))
    # print(local_data_frame.describe(include=['day_of_week', 'month', 'hour']))

    print("Most common month of bike usage: " + MONTH_NAMES[data_frame.month.mode()[0]])

    # TO DO: display the most common day of week
    # print(data_frame.day_of_week.value_counts())
    print("Most common day of week of bike usage: " + str(data_frame.day_of_week.mode()[0]))

    # TO DO: display the most common start hour
    # print(data_frame.hour.value_counts())
    print("Most common hour of day of bike usage: " + str(data_frame.hour.mode()[0]))

    if week_day.lower() != "all" or month.lower() != "all":
        text = ""
        if month.lower() != "all":
            text = "month [{}] ".format(month)
        if week_day.lower() != "all":
            text = text + "week [{}] ".format(week_day)

        print("Most common hour of day of bike usage for selected {}: {}".format(
            text,
            str(local_data_frame.hour.mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats():
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station: " + local_data_frame['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("Most commonly used end station: " + local_data_frame['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent combination of start station and end station trip: " +
          str(local_data_frame.groupby(['Start Station', 'End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def assign_default_string(text, value):
    if value == 0 or value == " ":
        return ""
    else:
        return str(int(value)) + " " + text + ","


def format_travel_time(text, seconds):
    """
    Converts seconds into days, hours, minutes and seconds and returns a formatted string

    :param text: A default string that can be prepended to the formatted date
    :param seconds: integer, number of seconds
    :return: returns a formatted string
    """

    days = divmod(seconds, 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)

    days = assign_default_string("days", days[0])
    hours = assign_default_string("hours", hours[0])
    minutes = assign_default_string("minutes", minutes[0])
    seconds = assign_default_string("seconds", minutes[1])

    return "{} travel time across all rides for given input: {} {} {} {}"\
        .format(text.title(), days, hours, minutes, seconds.rstrip(","))


def trip_duration_stats():
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(format_travel_time("Total", local_data_frame['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print(format_travel_time("Mean", local_data_frame['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats():
    """Displays statistics on bikeshare users."""
    global local_data_frame

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # local_data_frame.dropna(subset=['User Type'], inplace=True)
    local_data_frame = local_data_frame.dropna(subset=['User Type'])
    # print(data_frame.count())

    # TO DO: Display counts of user types
    print("Counts for each user type: \n{}".format(local_data_frame['User Type'].value_counts().to_string()))

    if 'Gender' in local_data_frame and 'Birth Year' in local_data_frame:
        # local_data_frame.dropna(subset=['Gender', 'Birth Year'], inplace=True)
        local_data_frame = local_data_frame.dropna(subset=['Gender', 'Birth Year'])

        # TO DO: Display counts of gender
        print("\nCounts for each Gender: \n{}".format(local_data_frame['Gender'].value_counts().to_string()))

        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nEarliest year of birth: {}".format(int(local_data_frame['Birth Year'].min())))
        print("Most recent year of birth: {}".format(int(local_data_frame['Birth Year'].max())))
        print("Most common year of birth: {}".format(int(local_data_frame['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    global month_data_loaded, week_data_loaded, local_data_frame

    while True:
        print("\n\n")
        print('Hello! Let\'s explore some US bikeshare data!')

        prompt_user()

        print('-' * 40)

        time_stats()
        station_stats()
        trip_duration_stats()
        user_stats()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        else:
            local_data_frame = None
            month_data_loaded = False
            week_data_loaded = False


if __name__ == "__main__":
    main()
