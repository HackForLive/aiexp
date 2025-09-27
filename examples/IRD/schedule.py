"""
accrual / forecasting and payment dates always exactly align
the dcf is based on an actual/365 fixed day count convention
holiday calendars are completely ignored, or rather, we propose no holidays
schedules are generated from the front creating back stubs for any fractional periods.
"""

from datetime import datetime, timedelta
from math import ceil


def add_months(start: datetime, months: int) -> datetime:
    """add a given number of months to an inpute date with a modified month end rule"""
    year_roll = int((start.month + months - 1) / 12)
    month = (start.month + months) % 12
    month = 12 if month == 0 else month

    try:
        end = datetime(start.year + year_roll, month, start.day)
    except ValueError: # day is out of range of month
        return add_months(datetime(start.year, start.month, start.day -1), months)
    else:
        return end
    

class Schedule:
    def __init__(self, start: datetime, tenor: int, period: int):
        self.start = start
        self.end = add_months(start=start, months=tenor)
        self.tenor = tenor
        self.period = period
        self.dcf_conv = timedelta(days=365)
        self.n_periods = ceil(tenor/ period)

    def __repr__(self):
        output = "period start | period end | period DCF \n"
        f = "%Y-%b-%d"
        for period in self.data:
            output += f"{period[0].strftime(f)} | {period[1].strftime(f)} | " \
                        f"{period[2]:3f}\n"
            
        return output
    
    @property
    def data(self):
        schedule = []
        period_start = self.start
        for i in range(self.n_periods - 1):
            period_end = add_months(period_start, self.period)
            schedule.append(
                [period_start, period_end, (period_end-period_start)/ self.dcf_conv]
            )
            period_start = period_end
        schedule.append(
            [period_start, self.end, (self.end-period_start)/ self.dcf_conv]
        )
        return schedule