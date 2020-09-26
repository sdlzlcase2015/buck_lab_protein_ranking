import re
import linecache
import fileinput
import pandas as pd
import csv
###################Read informatin (PDB entries) for protein species###################
start=[];end=[];point=[];seqPoint=[];PDBID=[];name=[]
fp = open ("uni_homo_PDB.xml","r")    #open file
count=-1;m=-1;n=-1;indicator=0; rep=0;q=0
for line in fp: 
   divide=line.split();   count=count+1;
   if "<entry" in line: 
       m=m+1;  start.append(count); point.append(0); PDBID.append(""); seqPoint.append(0); name.append("NA");   rep=1
   if "<recommendedName>" in line and rep==1: 
       q=1
   if "<fullName" in line and q==1 and rep==1:  
       name[m]=re.findall(r'>(.*)<', line)[0]
   if "</recommendedName>" in line:
       q=0;rep=0
   if "PDBsum" in line:
       point[m]=point[m]+1;   v = re.search('id=\"(.+?)\"/>', line)
       if v:
          PDBID[m]=PDBID[m]+v.group(1)+','
   if "</entry>" in line:
       n=n+1
       if (n==m):
         end.append(count)
       else:
         n=n-1;  indicator=indicator+1
   del line
fp.close()


########################sort and rank the protein species###############################
number_list=list(map(int, list(point)))
y=zip(number_list,name,PDBID)
y.sort(reverse=True)

with open('ProteinRank.csv', mode='w') as csv_file:
  fieldnames = ['Number_PDB_Entry', 'Name', 'PDB_ID']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  for l in range (0, len(point)):
      writer.writerow({'Number_PDB_Entry':y[l][0], 'Name': y[l][1], 'PDB_ID': y[l][2][0:(len(y[l][2])-1)]})
  


        
