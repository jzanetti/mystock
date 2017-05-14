import matplotlib.pyplot as plt
from data_processing import normalized_data

def plot_data(mydata,data_type,data_interval_sec):
    data_list = mydata.date
    time_list = mydata.time
    high_list = mydata.high
    low_list = mydata.low
    volume_list = mydata.volume
    open_list = mydata.open_
    close_list = mydata.close
    
    figure_size = (15, 7)

    print 'plotting high/low/open/close ... '
    plt.figure(figsize=figure_size)
    plt.plot(high_list,'r',label='High')
    plt.plot(low_list,'g',label='Low')
    plt.plot(open_list,'b',label='Open')
    plt.plot(close_list,'c',label='Close')
    title_str = mydata.symbol + '_price_' + data_type + '_' + str(data_interval_sec) + 's__from_' \
                + data_list[0].strftime('%Y-%m-%d') + ':' + time_list[0].strftime('%H:%M:%S') + '_to_' \
                + data_list[-1].strftime('%Y-%m-%d') + ':' + time_list[-1].strftime('%H:%M:%S')
    plt.title(title_str)
    plt.legend()
    plt.xlabel('time points')
    plt.ylabel('price')
    plt.grid()
    plt.savefig(title_str + '.png',bbox_inches='tight')
    plt.close()
    
    print 'plotting volume ... '
    plt.figure(figsize=figure_size)
    plt.plot(volume_list,'k',label='Volume')
    title_str = mydata.symbol + '_volume_' + data_type + '_' + str(data_interval_sec) + 's__from_' \
                + data_list[0].strftime('%Y-%m-%d') + ':' + time_list[0].strftime('%H:%M:%S') + '_to_' \
                + data_list[-1].strftime('%Y-%m-%d') + ':' + time_list[-1].strftime('%H:%M:%S')
    plt.title(title_str)
    plt.legend()
    plt.xlabel('time points')
    plt.ylabel('volume')
    plt.grid()
    plt.savefig(title_str + '.png',bbox_inches='tight')
    plt.close()
    
    print 'plotting normlized data ... '
    plt.figure(figsize=figure_size)
    plt.plot(normalized_data(high_list),'r',label='High')
    plt.plot(normalized_data(low_list),'g',label='Low')
    plt.plot(normalized_data(open_list),'b',label='Open')
    plt.plot(normalized_data(close_list),'c',label='Close')
    plt.plot(normalized_data(volume_list),'k',label='Volume')
    title_str = mydata.symbol + '_norm_' + data_type + '_' + str(data_interval_sec) + 's__from_' \
                + data_list[0].strftime('%Y-%m-%d') + ':' + time_list[0].strftime('%H:%M:%S') + '_to_' \
                + data_list[-1].strftime('%Y-%m-%d') + ':' + time_list[-1].strftime('%H:%M:%S')
    plt.title(title_str)
    plt.legend()
    plt.xlabel('time points')
    plt.ylabel('norm data')
    plt.grid(True,which='both')
    plt.minorticks_on()
    plt.savefig(title_str + '.png',bbox_inches='tight')
    plt.close()
    
def plot_google_trends(google_trends_data,mydata):
    data_list = mydata.date
    time_list = mydata.time
    plt.plot(google_trends_data,'k',label='iphone')
    
    title_str = 'google_trends_daily_from_' \
                + data_list[0].strftime('%Y-%m-%d') + ':' + time_list[0].strftime('%H:%M:%S') + '_to_' \
                + data_list[-1].strftime('%Y-%m-%d') + ':' + time_list[-1].strftime('%H:%M:%S')
        
    plt.title(title_str)
    plt.legend()
    plt.xlabel('time points')
    plt.ylabel('google trends')
    plt.grid(True,which='both')
    plt.minorticks_on()
    plt.savefig(title_str + '.png',bbox_inches='tight')
    plt.close()       
        
        