1. Download database from https://www.uniprot.org/downloads#uniprotkblink.
File name uniprot_sprot.xml.gz.
2. unzip the file. Get uniprot_sprot.xml.
3. Extract protein species for human; select proteins with at least 1 PDB. (python uni_homo_PDB.py)
4. Sort and rank the protein by the number of available pdb entries (python PDBrank.py)
