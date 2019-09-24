import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('quandlapikey.txt','r').read()

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/w/index.php?title=List_of_U.S._states&oldid=5253027')
    return fiddy_states[0][0][1:]
    
def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df = pd.DataFrame(df['NSA Value'])
        df.columns=[str(abbv)]

        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    pickle_out = open('fiddy_states_3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()        

def HPI_Benchmark():
	abbv = 'USA'
	query = "FMAC/HPI_"+str(abbv)
	df = quandl.get(query, authtoken=api_key)
	df = pd.DataFrame(df['NSA Value'])
	df.columns=[str(abbv)]
	df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
	return df


#grab_initial_state_data()



'''
pickle_in = open('fiddy_states.pickle','rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data.head())

HPI_data2 = pd.read_pickle('fiddy_states.pickle')
#print(HPI_data2.head())
'''



'''
HPI_data = pd.read_pickle('fiddy_states.pickle')

HPI_data2 = HPI_data.pct_change()

pickle_out = open('fiddy_states_pct.pickle','wb')
pickle.dump(HPI_data2, pickle_out)
pickle_out.close()

HPI_data2.plot()
plt.legend().remove()
plt.show()
'''



'''
HPI_data3 = pd.read_pickle('fiddy_states_3.pickle')
print(HPI_data3)

HPI_data2 = pd.read_pickle('fiddy_states.pickle')
print(HPI_data2)

HPI_data3.plot()
#plt.legend().remove()
plt.show()
'''


'''
fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data3 = pd.read_pickle('fiddy_states_3.pickle')
benchmark = HPI_Benchmark()

benchmark.plot(ax=ax1,color = 'k')
HPI_data3.plot(ax=ax1,linewidth = 1)

plt.legend().remove()
plt.show()
'''

HPI_data3 = pd.read_pickle('fiddy_states_3.pickle')
HPI_Correlation_table = HPI_data3.corr()
print(HPI_Correlation_table)

print(HPI_Correlation_table.describe())