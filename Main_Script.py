import hist_analysis
import data_vis
import news_search
data_config = {
    'data_type': 'daily',
    
    'daily_data_config': {
        'start_datetime_str': '20120101T010000',
        'end_datetime_str': '20170501T010000',
        'stock_symbol': 'AAPL',
        'data_source': 'google',
        'data_res': 'daily',
        'google_trends': {
            'run_google_trends': False,
            'google_trends_keywords': ['iphone']
            }
        },
    
    'intraday_data_config':{
        'stock_symbol': 'AAPL',
        'goback_days': 1,
        'data_interval_sec': 300
        }
    }

if data_config['data_type'] == 'daily':
    my_data = hist_analysis.extract_daily_data(data_config['daily_data_config']['stock_symbol'], 
                                   data_config['daily_data_config']['data_source'],
                                   data_config['daily_data_config']['data_res'],
                                   data_config['daily_data_config']['start_datetime_str'],
                                   data_config['daily_data_config']['end_datetime_str'])
    data_vis.plot_data(my_data,'daily','NULL')
    
    if data_config['daily_data_config']['google_trends']['run_google_trends']:
        google_trends_data = news_search.google_trends(data_config['daily_data_config']['start_datetime_str'], 
                                  data_config['daily_data_config']['end_datetime_str'], 
                                  data_config['daily_data_config']['google_trends']['google_trends_keywords'],
                                  my_data.date)
        data_vis.plot_google_trends(google_trends_data,my_data)

if data_config['data_type'] == 'intraday':
    my_data = hist_analysis.extract_intraday_data(data_config['intraday_data_config']['stock_symbol'],
                                                  data_config['intraday_data_config']['goback_days'],
                                                  data_config['intraday_data_config']['data_interval_sec'])
    

    print 'visualization ...'
    data_vis.plot_data(my_data,'intraday',data_config['intraday_data_config']['data_interval_sec']) 


