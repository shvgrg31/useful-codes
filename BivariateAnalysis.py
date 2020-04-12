import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns

from feature_importance import data_vars,vif_calc,random_forest_feature_imp

def bivariate_analysis_continuous(df,target_col_name,num_col_list,plot_graph_ind="Y"):
    if plot_graph_ind=="Y":
        for i,col in enumerate(num_col_list):
            plt.figure(i)
            sns.FacetGrid(df,hue=target_col_name,height=6).map(sns.distplot,col).add_legend()
    return data_vars(df[num_col_list],df[target_col_name])

def bivariate_analysis_categorical(df,target_col_name,cat_col_list,plot_graph_ind="Y"):
    if plot_graph_ind=="Y":
        for i,col in enumerate(cat_col_list):
            plt.figure(i)
        sns.boxplot(x=target_col_name,y=col,data=df)
    return data_vars(df[cat_col_list],df[target_col_name])