
from Bio import Entrez
from Bio import SeqIO


def download_pubmed(x): 
    """Docstring download_pubmed"""
    Entrez.email = "jose.abata@est.ikiam.edu.ec"
    handle=Entrez.efetch (db="pubmed", rettype="medline", retmode="text", id=x)
    record = SeqIO.read(handle, "fasta")
    handle.close()
    
    return (record.seq, description) 

def mining_pubs(tipo):
    """Docstring mining_pubs"""
    if tipo == "AD":
        
    
    return 

    