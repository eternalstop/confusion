import datetime


def days2date(nums):
	the_date = datetime.datetime(year=1900, month=1, day=1)
	result_date = the_date + datetime.timedelta(days=nums)
	return result_date.strftime('%Y/%m/%d')

