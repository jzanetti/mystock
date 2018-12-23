import datetime
import data_processing

def extract_daily_data(stock_symbol,
                  data_source,
                  data_resolution,
                  start_datetime_str, end_datetime_str):
    start_datetime = datetime.datetime.strptime(start_datetime_str,'%Y%m%dT%H%M%S')
    end_datetime = datetime.datetime.strptime(end_datetime_str,'%Y%m%dT%H%M%S')

    return data_processing.daily_data_reformat().return_hist_daily_stats(start_datetime, end_datetime, stock_symbol, data_source)
    

def extract_intraday_data(stock_symbol,
                  goback_days, data_interval_sec):
    
    return data_processing.GoogleIntradayQuote(stock_symbol,data_interval_sec,goback_days)