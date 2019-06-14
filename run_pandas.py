import os
import csv
import sys
import pandas
from util import ValidateVIN

# python ml.py training/vin_master_origin

def footer():
     print("")

def pandas_serialzing(file1, file2):
    # load csv file1
    frame_one = pandas.read_csv(file1, sep='\t', names=['vin', 'make'])
    print("csv file1 head: ", file1)
    print(frame_one.head())

    # serialize the repeated categorical data field make
    # this allows us to serialize and re-hydrate the field faster
    frame_one['make'] = frame_one['make'].astype('category')
    frame_one.vin
    footer()

def pandas_sorting(file1, file2):

    # load csv file1
    frame_one = pandas.read_csv(file1, sep='\t', names=['vin', 'make'])
    print("csv file1 head: ", file1)
    print(frame_one.head())
    footer()
    
    # sort ascending first by make then by vin
    frame_one.sort_values(by=['make', 'vin'], ascending=True)

def pandas_examples(file1, file2):

    # load csv file1
    frame_one = pandas.read_csv(file1, sep='\t', names=['vin', 'make'])
    print("csv file1 head: ", file1)
    print(frame_one.head())
    footer()

    # load csv file2
    frame_two = pandas.read_csv(file2, sep='\t', names=['vin', 'make'])
    print("csv file2 head: ", file2)
    print(frame_two.head())
    footer()

    # are there vins in frame one that are in frame two
    df = frame_one['vin'].isin(frame_two['vin'])
    print("frame_one is in frame_two")
    print(df.describe())
    footer()

    # are there vins in frame two that are in frame one
    print("frame_two is in frame_one")
    df = frame_two['vin'].isin(frame_one['vin'])
    print(df.describe())
    footer()

    # are there last 8 of vin from frame one in last 8 of vin in frame two
    print("last 8: frame_one is in frame_two")
    df = frame_one['vin'].str[8:].isin(frame_two['vin'].str[8:])
    print(df.describe())
    footer()

    # are there last 8 of vin from frame two in last 8 of vin in frame one
    print("last 8: frame_two is in frame_one")
    df = frame_two['vin'].str[8:].isin(frame_one['vin'].str[8:])
    print(df.describe())
    footer()
    
    # is frame one equal to frame two
    print("frame_one equals frame_two?")
    df = frame_one.equals(frame_two)
    print(df)
    footer()

    # list last 8 of vin in frame one
    #print(frame_one.vin.str[8:])

    # list last 8 of vin in frame two
    #print(frame_two.vin.str[8:])

def validate_vin(file_path):

    data_origin = pandas.read_csv(file_path, sep='\t', names=['vin', 'make'])

    # data_clean = open("out/data_clean", "w")
    # data_encoded = open("out/data_encoded", "w")
    # data_exception = open("out/data_exception", "w")

    for row in data_origin:
        
        try:

            # record_data = "{0}\t{1}".format(row[0], row[4])
            # record_encoded_data = "{0}\t{1}\t{2}\t{3}".format(row[0], row[4], sum(row[0][:8].encode('utf-8')), 1)

            vin_result = ValidateVIN(row[0].upper())
            print(row)
            if vin_result[0]:
                print(row[0], row[4], sum(row[0][:8].encode('utf-8')), 1)
                # data_clean.write(record_data + "\n")
                # data_encoded.write(record_encoded_data + "\n")
            else:
                print("oops")
                # data_exception.write(record_encoded_data + "\t" + vin_result[2] + "\n")
        except csv.Error as e:
            print(e)
            #pass



    # data_clean.flush()
    # data_clean.close()
    # data_encoded.flush()
    # data_encoded.close()
    # data_exception.flush()
    # data_exception.close()


# cat vinValidation.txt | grep False > invalidVins.txt
# cat vinValidation.txt | grep True > validVins.txt
# python ml.py > vinValidation.txt


if __name__ == "__main__":

    print("Welcome to the pandas exception file example")

    pandas_examples(sys.argv[1], sys.argv[2])

    pandas_sorting(sys.argv[1], sys.argv[2])


    
 
