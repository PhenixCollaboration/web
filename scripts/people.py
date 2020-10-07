#!/usr/bin/env python3

import argparse
import csv

Usage		= '''Usage:
Files with "people", "affiliation" and "msg" data exported from the PHENIX DB must be specified as inputs.
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-U", "--usage",	action='store_true',	help="print usage notes and exit")
    parser.add_argument("-p", "--people",	required=True, type=str,help="the 'people' file exported from the PHENIX DB (csv)")
    parser.add_argument("-a", "--affiliation",	required=True, type=str,help="the 'institutional affiliation' file exported from the PHENIX DB (csv)")
    parser.add_argument("-i", "--institutions",	required=True, type=str,help="the 'institutions' file exported from the PHENIX DB (csv)")
    parser.add_argument("-m", "--mgs",		required=True, type=str,help="the 'members in good standing (mgs)' file exported from the PHENIX DB (csv)")
    parser.add_argument("-e", "--email",	required=True, type=str,help="the 'e-mail addresses' file exported from the PHENIX DB (csv)")

    args = parser.parse_args()

    if(args.usage):
        print(Usage)
        exit(0)

    mgs=[]
    people=[]

    email={}
    affiliation={}
    institutions={}
    
    with open(args.affiliation, newline='') as affiliation_file:
        reader = csv.DictReader(affiliation_file)
        for row in reader:
            if(row['status']!='prim'): continue
            try:
                if(affiliation[row['person']]['run']!=''):
                    if(int(row['run'])>int(affiliation[row['person']]['run'])): affiliation[row['person']]={'institute':row['institute'], 'run':row['run']}
                else:
                    affiliation[row['person']]={'institute':row['institute'], 'run':row['run']}
            except:
                affiliation[row['person']]={'institute':row['institute'], 'run':row['run']}

    with open(args.email, newline='') as email_file:
        reader = csv.DictReader(email_file)
        for row in reader: email[row['person_id']]=row['email']
    
    with open(args.institutions, newline='') as institutions_file:
        reader = csv.DictReader(institutions_file)
        for row in reader: institutions[row['id']]=row['name']
        
    ###
    
    with open(args.mgs, newline='') as mgs_file:
        reader = csv.DictReader(mgs_file)
        for row in reader:
            mgs.append(row['id'])

    with open(args.people, newline='') as people_file:
        reader = csv.DictReader(people_file)
        for row in reader:
            if(row['id'] in mgs):
                person=row['id']
                aff=affiliation[person]['institute']
                institution=institutions[aff]
                people.append(
                    {
                        'id':row['id'],
                        'family_name':row['family_name'],
                        'first_name':row['first_name'],
                        'email':email[row['id']],
                        'inst_name':institution
                    }
                )
            
    fieldnames=['family_name', 'first_name', 'email', 'inst_name']
    
    # At this point, we have a list of dictionaries like this one:
    # {'email': 'potekhin@bnl.gov', 'first_name': 'Maxim', 'family_name': 'Potekhin', 'id': '1723', 'inst_name': 'Physics Department, Brookhaven National Laboratory (BNL), Upton, New York 11973-5000, USA'}
    with open('collaboration.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in people:
            del p['id']
            writer.writerow(p)
        
    csvfile.close()
   
    
