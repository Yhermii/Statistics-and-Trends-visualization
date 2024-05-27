# import libraries
import pandas as pd
import matplotlib.pyplot as plt


def hatecrime_plot(SPLC_report, FBI_report):
    """define a function to create a line plot of hate crime reported
    by SPLC (Southern Poverty Law Center) and FBI (Federal Bureau of Investigation)"""

    # import csv file
    hate_crime = pd.read_csv('/Users/babayhermi/Downloads/hate_crimes.csv')

    # hate crime reported by SPLC and FBI
    SPLC_report = hate_crime['hate_crimes_per_100k_splc']
    FBI_report = hate_crime['avg_hatecrimes_per_100k_fbi']

    # create line plot
    plt.figure()
    plt.plot(hate_crime['state'], SPLC_report, label='SPLC')
    plt.plot(hate_crime['state'], FBI_report, label='FBI')

    # add legend and label
    plt.legend()
    plt.xticks(rotation=90)
    plt.xlabel('State')
    plt.ylabel('Hate Crimes per 100k People')
    plt.title('Hate Crimes Reported by SPLC & FBI')

    # save and show plot
    plt.savefig('lineplot.jpg')
    plt.show()
    return(SPLC_report, FBI_report)


# line plot for hate crime reported
hatecrime_plot('SPLC_report', 'FBI_report')


def median_household_income(states, median):
    """define a function to create a bar plot of the median 
    household income of each state in USA"""

    # import csv file
    hate_crime = pd.read_csv('hate_crimes.csv')

    # create a bar plot to show highest and lowest median household income by state
    median_income = hate_crime['median_household_income']
    states = hate_crime['state']

    # create bar plot
    plt.bar(states, median_income)

    # add title and label
    plt.title("Median Household Income by State")
    plt.xlabel("State")
    plt.ylabel("Median Income ($)")
    plt.xticks(rotation=90)
    plt.tight_layout()

    # save and show plot
    plt.savefig('barplot.jpg')
    plt.show()
    return(states, median)


# bar plot for median household income
median_household_income('states', 'median')


def fbi_hatecrime_plot(fbi_data, label):
    """define a function to create a pie chart of 10 selected states in the 
    USA with hate crime as reported by FBI"""

    # import csv file
    hate_crime = pd.read_csv('hate_crimes.csv')

    # extract the hate crime data reported by FBI
    fbi_data = hate_crime['avg_hatecrimes_per_100k_fbi']
    label = hate_crime['state']

    # extract first 10 states on the list
    first10_states = fbi_data.iloc[0:10]
    labels = label.iloc[0:10]

    # create pie chart
    plt.pie(first10_states, labels=labels, autopct='%d%%')

    # add axis and title
    plt.title('First 10 States Reported by FBI')
    plt.axis('equal')
    plt.tight_layout()

    # save and show plot
    plt.savefig('piechart.jpg')
    plt.show()
    return(fbi_data, label)


# pie chart for first 10 states
fbi_hatecrime_plot('fbi_data', 'label')
