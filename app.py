import requests
import json
from secret_keys import *
import csv



class Back4App():
    def get_sentance(self):
        
        with open('leaders_name.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} {row[1]} {row[2]}.')
                    line_count += 1
            

        #for i in results['meaning']:
            #print(i)
        birth_date=row[1]
        #birth_date=date time.strptime(row[1],%y-%m-%d)
        today=date.today

int(date)
        birthdate_list=birth_date.split("-")
        deathdate_list=death_date.split("-")
            for in birthdate_list:
                if today_date==birthdate_list[2]
            for in deathdate_list:
                if today_date==birthdate_list[2]
        death_date=row[2]
        deathdate_list=death_date.split("-")
                if today_date==deathdate_list[2]

if __name__ == "__main__":
    print("Try running daily_one_word.py first")
