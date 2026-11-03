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

Best_worst_traading_days (rate, open, close, date):