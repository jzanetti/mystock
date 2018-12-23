from pytrends.request import TrendReq
import datetime
import numpy

def google_trends(start_datetime_str, end_datetime_str, kw_list_in, ref_datetime_list):
    timeframe_in = (datetime.datetime.strptime(start_datetime_str, '%Y%m%dT%H%M%S')).strftime('%Y-%m-%d') + ' ' + (datetime.datetime.strptime(end_datetime_str, '%Y%m%dT%H%M%S')).strftime('%Y-%m-%d')
    google_username = "zsjzyhzp@gmail.com"
    google_password = "zsjzyhzp1985"
    pytrend = TrendReq(google_username, google_password, hl='en-US', tz=360, custom_useragent=None)
    pytrend.build_payload(kw_list=kw_list_in,timeframe=timeframe_in)
    return mask_missing_data(ref_datetime_list, pytrend)

def mask_missing_data(ref_datetime_list, pytrend):
    pytrend_data = []
    a = pytrend.interest_over_time()
    google_trend_date = [x.strftime('%Y-%m-%d') for x in (a[a.keys()[0]]).keys()]
    for refd in ref_datetime_list:
        refd_str = refd.strftime('%Y-%m-%d')
        if refd_str in google_trend_date:
            pytrend_data.append(a[a.keys()[0]][refd])
        else:
            pytrend_data.append(numpy.NaN)
    
    return pytrend_data
            