"""
module: MeteoDateTime
"""

# CT Coordinate Time (uniform)
# TAI International Atomic Time (proper)
# TT Terrestrial Time (proper)
#    TT = TAI + offset (> 30 s)
# UTC Coordinated Universal Time
#    UTC = TAI - offset
#        + leap seconds within 0.9 s of UT1
# GMT Greenwhich Mean Sidereal Time
#    replaced by Universal Time UT1
# last leap second 2015-06-30T23:59:60Z

# MDT Mountain Daylight Saving Time UTC - 06:00
# MST Mountain Standard Time UTC - 07:00
# PDT Pacific Daylight Saving Time UTC - 07:00
# PDT Pacific Standard Time UTC - 08:00
# DST US except Hawaii and Arizona
#     2015 March 8 - 2015 November 1

import numpy
import datetime
import calendar
import unittest
from skyfield.api import utc, JulianDate

__all__ = ["IllegalMonthError", "IllegalYearRangeError",
           "strDate", "strDayNumber", "extractDate",
           "objJulianDate", "objJulianDateToEpoch2000",
           "decimalDaysToDatetimes",
           "isLeapYear", "lengthYear", "lengthMonth",
           "dateToDayNumber", "dateSequence"]

class IllegalMonthError(ValueError):
    def __init__(self, month):
        self.month = month
    def __str__(self):
        return "bad month number %r; must be 1-12" % self.month

class IllegalYearRangeError(ValueError):
    def __init__(self, yearBegin, yearEnd):
        self.yearBegin = yearBegin
        self.yearEnd = yearEnd
    def __str__(self):
        return "bad year range %r - %r" % (self.yearBegin, self.yearEnd)

def strDate(year, month, day):
    """
    year
    month
    day
    return - tuple of strings (yyyy, mm, dd)
    """

    strYear  = "%4.4i" % year
    strMonth = "%2.2i" % month
    strDay   = "%2.2i" % day

    return strYear, strMonth, strDay

def strDayNumber(year, dayNumber):
    """
    year
    dayNumber
    return - tuple of strings (yyyy, ddd)
    """

    strYear   = "%4.4i" % year
    strDayNum = "%3.3i" % dayNumber

    return strYear, strDayNum

def extractDate(date):
    """
    date
    return - tuple (year, month, day)
    """

    year = date // 10000
    month = (date - 10000 * year) // 100
    day = date - 10000 * year - 100 * month

    return year, month, day

def objJulianDate(date, fDay):
    """
    date
    return - Julian date skyfield object
    """

    # return JulianDate(datetime.datetime(
    #     *date, tzinfo = utc)
    #     + datetime.timedelta(0, 24 * 60**2 * fDay))

    return JulianDate(tt = (JulianDate(utc = date).tt + fDay))

def objJulianDateToEpoch2000(objJulianDate):
    """
    date
    return - days since 2000-01-01T00:00:00Z
    """
    return objJulianDate.tt - JulianDate(utc = (2000, 1, 1)).tt

def decimalDaysToDatetimes(dateEpoch, listDecimalDays):
    """
    dateEpoch - date tuple of epoch start
    listDecimalDays - list of decimal days since epoch start
    return - list of datetimes
    """
    return [datetime.datetime(*tuple(numpy.int32(JulianDate(
            tt = JulianDate(utc = dateEpoch).tt + fDay).utc)))
            for fDay in listDecimalDays]

def isLeapYear(year):
    """
    return - True if leap year
    """

    return (year % 4 == 0 and year % 100 != 0) \
        or (year % 400 == 0)

def lengthYear(year):
    """
    return - length of year
    """

    if (isLeapYear(year)):
        return 366
    else:
        return 365

def lengthMonth(year, month):
    """
    return - length of month
    """

    if not 1 <= month <= 12:
        raise IllegalMonthError(month)

    length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (isLeapYear(year)):
        length[1] = 29

    return length[month - 1]

def dateToDayNumber(year, month, day):
    """
    year
    month
    day
    return - Julian day number
    """

    if not 1 <= month <= 12:
        raise IllegalMonthError(month)

    dayNumber = 0

    for iMonth in range(1, month):
        dayNumber += lengthMonth(year, iMonth)

    dayNumber += day

    return dayNumber

def dateSequence(dateBegin, dateEnd):

    yearBegin, monthBegin, dayBegin = dateBegin
    yearEnd, monthEnd, dayEnd = dateEnd

    listDates = []

    for year in range(yearBegin, yearEnd + 1):

        monthLoopBegin, monthLoopEnd = 1, 12
        if (year == yearBegin):
            monthLoopBegin = monthBegin
        if (year == yearEnd):
            monthLoopEnd = monthEnd

        for month in range(monthLoopBegin, monthLoopEnd + 1):

            dayLoopBegin, dayLoopEnd = 1, lengthMonth(year, month)
            if (year == yearBegin and month == monthBegin):
                dayLoopBegin = dayBegin
            if (year == yearEnd and month == monthEnd):
                dayLoopEnd = dayEnd

            for day in range(dayLoopBegin, dayLoopEnd + 1):
                listDates.append((year, month, day))

    return listDates

# test classes
class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.objDateToday = datetime.date.today()

    def testExtractDate(self):
        date = 10000 * self.objDateToday.year \
             + 100 * self.objDateToday.month \
             + self.objDateToday.day
        year, month, day = extractDate(date)
        self.assertEqual(year, self.objDateToday.year)
        self.assertEqual(month, self.objDateToday.month)
        self.assertEqual(day, self.objDateToday.day)

    def testObjJulianDate(self):
        # 2000-01-01T12:00:00Z = JD2451545.0
        date = 2000, 1, 1
        jd = objJulianDate(date, 0.5)
        self.assertAlmostEqual(jd.tt, 2451545.0, places = 2)

    def testObjJulianDateToEpoch2000(self):
        pass

    def testDecimalDaysToDatetimes(self):
        dateEpoch = 2000, 1, 1
        listDatetimes = decimalDaysToDatetimes(dateEpoch, [0.5, 1.0, 1.5])
        print(listDatetimes)

    def testIsLeapYear(self):
        for year in range(1900, 2101):
            self.assertEqual(isLeapYear(year), calendar.isleap(year))

    def testLengthYear(self):
        for year in range(1900, 2101):
            if (calendar.isleap(year)):
                length = 366
            else:
                length = 365
            self.assertEqual(lengthYear(year), length)

    def testLengthMonth(self):
        # print("\n")
        for year in range(2000, self.objDateToday.year + 1):
            #  print("testLengthMonth: %4.4i" % year)
            for month in range(1, 13):
                self.assertEqual(lengthMonth(year, month), \
                    calendar.monthrange(year, month)[1])

    def testDateToDayNumber(self):
        # print("\n")
        for year in range(2000, self.objDateToday.year + 1):
            # print("testDateToDayNumber: %4.4i" % year)
            for month in range(1, 13):
                for day in range(1, lengthMonth(year, month) + 1):
                    dayNumber = dateToDayNumber(year, month, day)

    def tearDown(self):
        del self.objDateToday

class TestBuiltInDateTime(unittest.TestCase):

    def setUp(self):
        self.year = datetime.date.today().year
        self.calendar = calendar.Calendar()

    def testYearDatesDateTime(self):
        yearDateTime = self.calendar.yeardatescalendar(self.year)

    def tearDown(self):
        del self.year
        del self.calendar

if __name__ == "__main__":
    suiteDateTime \
        = unittest.TestLoader().loadTestsFromTestCase(TestDateTime)
    suiteBuiltInDateTime \
        = unittest.TestLoader().loadTestsFromTestCase(TestBuiltInDateTime)
    tests = unittest.TestSuite([suiteDateTime, suiteBuiltInDateTime])
    unittest.TextTestRunner(verbosity=2).run(tests)

