import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
import os.path
savefolder = '/home/kamgo/Schreibtisch/PacmanDQNPER/figure/'
#/home/kamgo/Schreibtisch/PacmanDQNPER/logs/Mon_25_Feb_2019_08_24_12-l-7-m-7-x-5000.log

def readlog(title,filepath):
    dfLog = pd.DataFrame( columns=[ 'Times' , 'reward' , 'Q_values' , 'won' ] )
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
    log = readlog('/home/kamgo/Schreibtisch/projekt2/PacmanDQN/logs/Mon_25_Feb_2019_08_17_07-l-7-m-7-x-5000.log')
    title='unifor_prioritized'
    plotlog(title,log)
if __name__ == "__main__":
    main()      