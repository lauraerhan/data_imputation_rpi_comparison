

import numpy as np
import pandas as pd
from impyute.imputation.cs import mice
from missingpy import MissForest
from sklearn.impute import KNNImputer
import sys
import random

def mean_imputation(df_orig):
    df_mean_imputation = df_orig.copy()
    df_mean_imputation['ozone_Mean_Filled'] = df_mean_imputation['ozone'].fillna(df_orig['ozone'].mean())
    return df_mean_imputation

def mice_imputation(df_orig):
    imputed = mice(df_orig.values)
    df_imputed = pd.DataFrame(imputed, columns=df_orig.columns)
    #print(df_imputed.isnull().sum())
    return df_imputed

def missforest_imputation(df_orig):
    #print(df_orig.isnull().sum())
    imputer = MissForest()
    imputed = imputer.fit_transform(df_orig)
    df_imputed = pd.DataFrame(imputed, columns=df_orig.columns)
    #print(df_imputed.isnull().sum())
    return df_imputed

def knn_imputation(df_orig):
    #print(df_orig.isnull().sum())
    imputer = KNNImputer(n_neighbors=3)
    imputed = imputer.fit_transform(df_orig)
    df_imputed = pd.DataFrame(imputed, columns=df_orig.columns)
    #print(df_imputed.isnull().sum())
    return df_imputed

if __name__ == "__main__":
    #main()
    #run the code as code burst_size cont_rate alg
    #burst_size 0: random case, otherwise burstsize
    #cont_rate 1 ,10, etc
    #alg full, knn, mean, mice, mf
    burst_size = int(sys.argv[1])
    cont_rate = int(sys.argv[2])
    alg = sys.argv[3]

    df_original = pd.read_csv("original.csv")
    if burst_size == 1:
        dataset_name = "dataset_contamination_level_random_err_contamination_rate_" +str(cont_rate) +".csv"
    else:
        dataset_name = "dataset_contamination_level_whole_bursty_err_size" + str(burst_size) +"_contamination_rate_" +str(cont_rate) +"%.csv"
       
    
    file = "results"  
    if alg == "full":
        file_to_analyse = pd.read_csv(dataset_name)
        #mean imputation on contaminated dataset
        df_mean_imputation = mean_imputation(file_to_analyse)
        #print(df_mean_imputation['ozone_Mean_Filled'].describe())
        df_mean_imputation.to_csv(file+'_mean_imputated.csv')
            
        #mice imputation on contaminated dataset
        file_to_analyse = pd.read_csv(dataset_name)
        df_mice_imputation = mice_imputation(file_to_analyse)
        #print(df_mice_imputation['ozone'].describe())
        df_mice_imputation.to_csv(file+'_mice_imputated.csv')
            
            #miss forest imputation on contaminated dataset
        file_to_analyse = pd.read_csv(dataset_name)
        df_missforest_imputation = missforest_imputation(file_to_analyse)
            #print(df_missforest_imputation['ozone'].describe())
        df_missforest_imputation.to_csv(file+'_missforest_imputated.csv')
            
            #knn imputation on contaminated dataset
        file_to_analyse = pd.read_csv(dataset_name)
        df_knn_imputation = knn_imputation(file_to_analyse)
            #print(df_knn_imputation['ozone'].describe())
        df_knn_imputation.to_csv(file+'_knn_imputated.csv')
       
    elif alg == "knn":
            #knn imputation on contaminated dataset
        file_to_analyse = pd.read_csv(dataset_name)
        df_knn_imputation = knn_imputation(file_to_analyse)
        print(df_knn_imputation['ozone'].describe())
        df_knn_imputation.to_csv(file+'_knn_imputated.csv')
            
    elif alg == "mean":
            #mean imputation on contaminated dataset
        file_to_analyse = pd.read_csv(dataset_name)
        df_mean_imputation = mean_imputation(file_to_analyse)
        print(df_mean_imputation['ozone_Mean_Filled'].describe())
        df_mean_imputation.to_csv(file+'_mean_imputated.csv')
    elif alg == "mice":
            #mice imputation on contaminated dataset
        file_to_analyse = pd.read_csv(dataset_name)
        df_mice_imputation = mice_imputation(file_to_analyse)
        print(df_mice_imputation['ozone'].describe())
        df_mice_imputation.to_csv(file+'_mice_imputated.csv')
    else: # alg == "mf"
        #miss forest imputation on contaminated dataset
        file_to_analyse = pd.read_csv(dataset_name)
        df_missforest_imputation = missforest_imputation(file_to_analyse)
        print(df_missforest_imputation['ozone'].describe())
        df_missforest_imputation.to_csv(file+'_missforest_imputated.csv')        