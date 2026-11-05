'''Task 4 – Identify the Best and Worst Trading Days
Identify the trading days with the highest and lowest daily returns.
Use:
• np.argmax(rate) to identify the best trading day.
• np.argmin(rate) to identify the worst trading day.
For each day, display:
• Date
• Opening price
• Closing price
• Daily return rate (%)'''


from datetime import date


def Best_worst_traading_days (rate, open, close, date):
    import numpy as np
    
    best_day_index = np.argmax(rate)
    worst_day_index = np.argmin(rate)
    print("Best Trading Day:")
    print(f"Date: {date[best_day_index]}")
    print(f"Opening Price: {open[best_day_index]}")
    print(f"Closing Price: {close[best_day_index]}")
    print(f"Daily Return Rate: {rate[best_day_index]:.2f}%")
    print("\nWorst Trading Day:")
    print(f"Date: {date[worst_day_index]}")
    print(f"Opening Price: {open[worst_day_index]}")
    print(f"Closing Price: {close[worst_day_index]}")
    print(f"Daily Return Rate: {rate[worst_day_index]:.2f}%")

Best_worst_traading_days (rate, open, close, date)


'''Task 5 – Analyze Up and Down Trading Days
Determine how many trading days had positive and negative returns.
Requirements:
• Use a Boolean mask with rate > 0 to identify positive-return days.
• Use a Boolean mask with rate < 0 to identify negative-return days.
• Use np.sum() to count each category.
• Display both counts with appropriate labels.'''

def up_and_down_trading_days(rate):
    import numpy as np
    
    positive_days = np.sum(rate > 0)
    negative_days = np.sum(rate < 0)
    
    print(f"Number of Positive Trading Days: {positive_days}")
    print(f"Number of Negative Trading Days: {negative_days}")

up_and_down_trading_days(rate)

'''Task 6 – Calculate Cumulative Return
Calculate the estimated cumulative return using the daily open-to-close return rates.
Requirements:
1. Convert each daily rate into a return factor using: f = 1 + rate / 100
2. Calculate the cumulative return using: cum_return = (np.prod(f) - 1) * 100
3. Use np.prod() to calculate the product of the daily return factors.
4. Print the cumulative return as a percentage, rounded to two decimal places.'''

def cumulative_return(rate):
    import numpy as np
    f = 1 + rate / 100
    cum_return = (np.prod(f) - 1) * 100
    print(f"Cumulative Return: {cum_return:.2f}%")

cumulative_return(rate)