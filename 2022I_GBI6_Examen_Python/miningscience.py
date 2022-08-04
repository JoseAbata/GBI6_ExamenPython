from Bio import Entrez 
import re
import csv

def download_pubmed(keyword): 
    """Funcion para descargar la información de los articulos de interes, extraidos de Pubmed
    """
   # Always tell NCBI who you are (edit the e-mail below!)
    Entrez.email = "gualapuro.moises@gmail.com"
    handle = Entrez.esearch(db="pubmed", 
                            term=keyword,
                            usehistory="y")
    record = Entrez.read(handle)
    # generate a Python list with all Pubmed IDs of articles about keyword Network
    id_list = record["IdList"]
    record["Count"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                            rettype="medline", 
                            retmode="text", 
                            retstart=0,
    retmax=543, webenv=webenv, query_key=query_key)
    filename = keyword+".txt"
    out_handle = open(filename, "w")
    data = handle.read()
    handle.close()
    out_handle.write(data)
    out_handle.close()
    return

def map_science(tipo):
    """Funcion para mapear la cantidad de articulos escritos en un determinado lugar, sobre los datos obtenidos en la funcion download_pubmed"""
    #if tipo == "AD":
    with open(tipo) as f:
        my_text = f.read()
    my_text = re.sub(r'\n\s{6}', ' ', my_text)  
    zipcodes = re.findall(r'[A-Z]{2}\s(\d{5}), USA', my_text)
    unique_zipcodes = list(set(zipcodes))
    zip_coordinates = {}
    with open('zip_coordinates.txt') as f:
        csvr = csv.DictReader(f)
        for row in csvr:
         zip_coordinates[row['ZIP']] = [float(row['LAT']), float(row['LNG'])]
    zip_code = []
    zip_long = []
    zip_lat = []
    zip_count = []
    for z in unique_zipcodes:
    # if we can find the coordinates
        if z in zip_coordinates.keys():
            zip_code.append(z)
            zip_lat.append(zip_coordinates[z][0])
            zip_long.append(zip_coordinates[z][1])
            zip_count.append(zipcodes.count(z))
    import matplotlib.pyplot as plt
    #%matplotlib inline
    plt.scatter(zip_long, zip_lat, s = zip_count, c= zip_count)
    plt.colorbar()
# only continental us without Alaska
    plt.xlim(-125,-65)
    plt.ylim(23, 50)
# add a few cities for reference (optional)
    ard = dict(arrowstyle="->")
    plt.annotate('Columbus', xy = (-82.98, 39.98), 
                   xytext = (-72.98, 39.98), arrowprops = ard)
    plt.annotate('Houston', xy = (-95.3698, 29.7604), 
                   xytext = (-85.3698, 24.7604), arrowprops= ard)
    plt.annotate('Washington D. C.', xy = (-77.0368, 38.9071), 
                   xytext = (-70.0368, 35.9071), arrowprops= ard)
    plt.annotate('New York', xy = (-74.0059, 40.7127), 
                   xytext = (-70.0059, 45.7127), arrowprops= ard)
    plt.annotate('San Francisco', xy = (-122.4194, 37.7749), 
                   xytext = (-112.4194, 37.7749), arrowprops= ard)
    plt.annotate('New Orleans', xy = (-90.0715, 29.9510), 
                   xytext = (-80.0715, 29.9510), arrowprops= ard)
    params = plt.gcf()
    plSize = params.get_size_inches()
    params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
    return plt.show()

