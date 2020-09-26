import linecache
import fileinput

##########################Find information for protein of Homo Sapine################################
start=[]; end=[]; point=[]; virus=[]; pdb=[]
fp = open ("uniprot_sprot.xml","r")   
count=-1; m=-1; n=-1; indicator=0
for line in fp:   
    count=count+1
    if "<entry" in line: 
       m=m+1; start.append(count); point.append(0); virus.append(0); pdb.append(0)
    if ">Homo sapiens</name>" in line:
       point[m]=1
    if "PDBsum" in line:
       pdb[m]=1
    if "<organismHost>" in line:
       virus[m]=1
    if "</entry>" in line:
       n=n+1
       if (n==m):
         end.append(count)
       else:
         n=n-1; indicator=indicator+1
    del line
fp.close()


#########################write the information of protein to a separate file#########################
fd = open ("uni_homo_PDB.xml","w")
with open ('uniprot_sprot.xml', 'r') as f:    
   dyns=0; dyne=1  
   for i, line in enumerate(f):  
       add=0;
       for j in  range (dyns,dyne):
          if (dyne<len(start)):
             if i>=start[j] and i<=(end[j]):
                if i==end[j]:
                   add=1
                if (point[j]==1 and virus[j]!=1 and pdb[j]==1):        
                   fd.write(line)
       dyns=dyns+add
       dyne=dyne+add
   del f
fd.close()
