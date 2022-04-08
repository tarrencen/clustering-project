import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans

np.random.seed(302)



def cluster_plucker(df, scaled_df, k):
    '''
    Takes in a dataframe, a scaled version of the dataframe, and a k number of clusters;
    returns the dataframe with new column of K means model predictions.
    '''
    kmeans = KMeans(n_clusters=k).fit(scaled_df)
    df['cluster_'] = kmeans.predict(scaled_df)
    return df 



def viz_cluster(df, x, y, hue, hline=False):
    '''
    Takes in a dataframe and variables for x(categorical), y(target), and hue(cluster predictions column), 
    with the option of an horizontal axis line(calculation);
    returns a stripplot graph'''
    graph = sns.stripplot(data=df, x=x,y=y, hue=hue)

    if hline:
        graph.axhline(hline)
        return graph
    else:
        return graph


def viz_cluster_bivariates(df, x, y, hue):
    '''
    Takes in a dataframe and variables for x(continuous), y(target), and hue(cluster predictions column);
    returns a relplot graph'''
    graph = sns.relplot(data=df, x=x,y=y, hue=hue)
    return graph