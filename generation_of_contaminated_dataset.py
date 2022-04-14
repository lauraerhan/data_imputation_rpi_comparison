

import pandas as pd
import sys
import random

def create_contaminated_dataset(df_orig, err_rate, burst_size):
    #creating copy to contaminate
    df_orig.drop(['timestamp'], axis = 1, inplace = True)
    df_copy = df_orig

    samp = round((err_rate*len(df_copy.index))/(100*burst_size))
    print(samp)
    #dataset generation with desired contamination level - err_rate
    #https://stackoverflow.com/questions/51918580/python-random-list-of-numbers-in-a-range-keeping-with-a-minimum-distance
    
    index_to_nan = [burst_size*i + x for i, x in enumerate(sorted(random.sample(range(len(df_copy.index) - burst_size - (samp - 1)*(burst_size -1)), samp)))]
    for j in index_to_nan:
        for b in range(burst_size):
            df_copy.loc[b+j,'ozone'] = pd.NA    
            
    print(df_copy['ozone'].isnull().sum()/len(df_copy.index))
    #export to csv the dataset
    #file_location = r"C:\path\to\file"
    if burst_size == 1:
        dataset_name = "dataset_contamination_level_random_err_contamination_rate_" +str(cont_rate) +".csv"
    else:
        dataset_name = "dataset_contamination_level_whole_bursty_err_size" + str(burst_size) +"_contamination_rate_" +str(err_rate) +"%.csv"

    df_copy.to_csv(dataset_name, index = False, header=True)
    return dataset_name

if __name__ == "__main__":
    #main()
    #run the code as code burst_size cont_rate 
    #burst_size 1: random case, otherwise burstsize
    #cont_rate 1 ,10, etc
    burst_size = int(sys.argv[1])
    cont_rate = int(sys.argv[2])

    if burst_size == 1:
        #random case scenario
        file = "dataset_contamination_level_random_err_contamination_rate_" +str(cont_rate)
        dataset_name = "dataset_contamination_level_random_err_contamination_rate_" +str(cont_rate) +".csv"
    else:
        #bursty case scenario
        file = "dataset_contamination_level_whole_bursty_err_size" + str(burst_size) +"_contamination_rate_" +str(cont_rate) +"%"
        dataset_name = "dataset_contamination_level_whole_bursty_err_size" + str(burst_size) +"_contamination_rate_" +str(cont_rate) +"%.csv"
   
    df_original = pd.read_csv("original.csv")
    #print(df_original['ozone'].describe())
    #contaminated dataset
    create_contaminated_dataset(df_original, cont_rate, burst_size)