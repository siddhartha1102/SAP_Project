

try:
    import pandas as pd
    import os
    #from date_utils import datetime
    def date_conversion(input_filename,output_filename):

        #input_filename="Process_chain_23_june_2025_final.xlsx"
        #compete_filename=os.path.join(input_directory,input_filename)
        #print(compete_filename)
        df=pd.read_excel(input_filename)

        df['Start'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))
        df['End'] = pd.to_datetime(df['End Date'].astype(str) + ' ' + df['End Time'].astype(str))
        df = df.drop(['Date', 'Time','End Date','End Time','Runtime [sec]','Main','Log-Id','SubChains',], axis=1)
        df = df[['Chain', 'Start', 'End','Runtime',"Status"]]
        print(df)
        #df = df.drop(['Col1', 'Col2'], axis=1)
        #output_filename="Process_chain_23_june_2025_final1.xlsx"
        df.to_excel(output_filename,index=False)
except Exception as e:
    print(e)