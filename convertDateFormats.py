##using regex

import re


def transform_date_format(date):
    return re.sub(r"(\d{4})-(\d{1,2})-(\d{1,2})", "\\3-\\2-\\1", date)


date_input = "2021-12-21"
print(transform_date_format(date_input))


### using datetime module

from datetime import datetime

new_date = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d:%Y:%m")
print(new_date)
