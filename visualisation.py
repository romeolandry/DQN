import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
import os.path
savefolder = '/home/kamgo/Schreibtisch/PacmanDQNPER/figure/'
#/home/kamgo/Schreibtisch/PacmanDQNPER/logs/Mon_25_Feb_2019_08_24_12-l-7-m-7-x-5000.log

def readlog(title,filepath):
    dfLog = pd.DataFrame( columns=[ 'Times' , 'reward' , 'Q_values' , 'won' ] )
    #df = pd.read_table('logs/Mon_25_Feb_2019_08_24_12-l-7-m-7-x-5000.log',sep=':',header=None,comment='#')
    with open(filepath,'r') as logFile:
        numRows = -1
        for line in logFile:
            tokens = line.split("|")
            col = tokens[3].split(":")
            time = col[1]
            col = tokens[4].split(":")
            reward =col[1]
            col = tokens[6].split(":")
            Q_values=col[1]
            col = tokens[7].split(":")
            won = col[1]
            numRows+=1
            dfLog.loc[numRows] =[time,reward,Q_values,won]

    plotlog(title,dfLog)

def plotlog(title,dataframe):
    df = dataframe.drop(labels='won',axis=1)
    df = df.astype(float)
    ax =plt.gca()
    df.plot(kind='line',x='Times',y='Q_values',ax=ax)

    #df.plot(kind='line',x='Times',y='reward',ax=ax)
    plt.title(title)
    plt.savefig(os.path.join(savefolder,title +'.png'))
    plt.show()



def main():
    title='prop_prioritized_without_epsilon-greedy'  
    log = readlog(title,'logs/Tue_26_Feb_2019_02_54_19-l-7-m-7-x-5000.log')
    plotlog(title,log)
if __name__ == "__main__":
    main()      