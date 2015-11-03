"""
Created on Tue Nov 03 17:11:26 2015

@author: Bilal El Banna
"""
################################IMPORTS########################################
import urllib

################################FUNCTIONS DEFs#################################


def scraper (txt_file):
    """ Function to save images locally which are retrieved from certain weblocations, 
    given a plaintext file containing one url per line.

    txt_file: path of the plaintext file
    """
    # Open plaintext file, load each line into an iterable list, 
    #close plaintext file
    links = open(txt_file, "r")
    line= links.read().splitlines()
    links.close()   
    
    #iterate over all lines/links
    for download_link in line:
        try:
            #split the url at each slash
            pic_name = download_link.split("/")
            #open link and save the Image into the python script's root folder
            urllib.urlretrieve(download_link,pic_name[-1])
        except:
            next
    return

################################MAIN###########################################

def main():
    
    
    txt_file = "jpg-links_plaintext.txt"
    scraper(txt_file)
 

if __name__ == "__main__":
    main()
    
################################END########################################