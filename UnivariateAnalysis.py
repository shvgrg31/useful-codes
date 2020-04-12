import pandas as pd

def univariate_analysis_for_char(df,cat_col_list,to_display_counter=7):
    df_sum = pd.merge(df[cat_col_list].describe().T.reset_index().rename(columns={'index':'cols'})[['cols','unique']],df[cat_col_list].isnull().sum().reset_index().rename(columns={'index':'cols',0:'#Miss'}),on='cols',how='left')
    df_sum['count'] = df.shape[0]
    df_sum['miss%'] = df_sum['#Miss']/df_sum['count']
    for col in cat_col_list:
        for i in range(to_display_counter):
            try:
                df_sum.loc[df_sum[df_sum['cols']==col].index,'top_'+str(i+1)] = [str(key)+" : "+str(value) for key,value in dict(df[col].value_counts()[:to_display_counter]).items()][i]
            except:
                df_sum.loc[df_sum[df_sum['cols']==col].index,'top_'+str(i+1)] = "-"
    return df_sum[['cols','count','#Miss','miss%','unique']+["top_"+str(i+1) for i in range(to_display_counter)]]

def univariate_analysis_for_ind(df,ind_col_list,top_display=5):
    df_sum = pd.merge(df[ind_col_list].describe().T.reset_index().rename(columns={'index':'cols'})[['cols','mean','std']],df[ind_col_list].isnull().sum().reset_index().rename(columns={'index':'cols',0:'#Miss'}),on='cols',how='left')
    df_sum['count'] = df.shape[0]
    df_sum['miss%'] = df_sum["#Miss"]/df_sum['count']
    for col in ind_col_list:
        df_sum.loc[df_sum[df_sum['cols']==col].index,'unique'] = len(list(df[col].value_counts().index))
        for i in range(top_display):
            try:
                df_sum.loc[df_sum[df_sum['cols']==col].index,'top_'+str(i+1)] = [str(key)+" : "+str(value) for key,value in dict(df[col].value_counts()[:top_display]).items()][i]
            except:
                df_sum.loc[df_sum[df_sum['cols']==col].index,'top_'+str(i+1)] = "-"
    return df_sum[['cols','count','#Miss','miss%','unique']+["top_"+str(i+1) for i in range(top_display)]]
    return df_sum

def univariate_analysis_for_cont(df,num_col_list,percentiles_list=[.01,.25, .5, .75,.99]):
    df_sum = pd.DataFrame(df[num_col_list].isnull().sum(),columns=["#Miss"])
    df_sum['miss%'] = df_sum["#Miss"]/df.shape[0]
    df_sum2 = df[num_col_list].describe(percentiles=percentiles_list).T
    df_fin = pd.merge(df_sum,df_sum2,how = 'left',left_index=True,right_index=True)
    df_fin['count'] = df.shape[0]
    df_fin = df_fin.reset_index().rename(columns={'index':'cols'})
    return df_fin[['cols','count','#Miss', 'miss%', 'mean', 'std', 'min','max', '1%', '25%', '50%','75%', '99%' ]]