from pyfaidx import Fasta, os
project_root = os.path.dirname(os.path.dirname(__file__)) #Gets the folder containing the script
fasta_path = os.path.join(project_root, "data", "sequence.fasta") #Creates a path to the fasta file
genes = Fasta(fasta_path)
print(genes.keys())
