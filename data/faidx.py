from pyfaidx import Fasta, os
project_root = os.path.dirname(os.path.dirname(__file__)) #Gets the folder containing the script
fasta_path = os.path.join(project_root, "data", "sequence.fasta") #Creates a path to the fasta file
genes = Fasta(fasta_path)

mitochondria = list(genes.keys())[0] #Fasta object is dictionary-like, so we can create the first key to access
print(genes[mitochondria][100:150:1]) #First goes to mitochondria, then slices sequence from 100 to 150 with a step of 50
     