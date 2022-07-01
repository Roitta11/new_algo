import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

'''
Plan for the project:-
1) Get the base url
2) Parse through the url to get the name of the subjects
3) Parse through the subjects' url to get the years 
4) Parse through the years' url to get the pdfs
5) Divide the pdfs between Summer and Winter according to their 
   corresponding year
6) Download the files

'''



# The link from where the files are to be downloaded
base_url = "https://papers.gceguide.com/A%20Levels/"

# Get the current folder location for downloading the files.
folder_location = os.getcwd()

# Get the response and create a Beautiful soup object
response = requests.get(base_url)
soup = BeautifulSoup(response.text,'lxml')
for subject in soup.find_all('li', class_='dir'):
    # Get the subject name from the base_url link
    links = subject.a.text
    # print(links)

    # Form the link for the particular subjects
    links_text = links.split()
    link_head = links_text[0]
    link_tail = links_text[-1]
    link_form = link_head + "%20" + link_tail
    final_link = base_url + link_form + "/"
    link_list = final_link.split(' ')
    # print(final_link)
    # print(link_list)




    # Create the subject directories
    # for i in range(1,int(links)):
    #     os.makedirs(folder_location + f"/{i}")







    # Parse the 'final_link' to find the years for each subject
    for i in link_list:
        response2 = requests.get(i)
        soup2 = BeautifulSoup(response2.text,'lxml')
       

    for year in soup2.find_all('li', class_='dir'):
        # Grab the years for each subject
        year_link = year.a.text
        # print(year_link)
        year_link_text = year_link.split()
        year_head = year_link_text[0]
        # print(year_head)
        # Form the url for each year with the base url
        final_year = final_link + year_head + "/"
        # print(final_year)
        year_list = final_year.split(' ')
        # print(year_list)

        # Create summer and winter directories





    # Parse each year's link to find the pdf for each subject
        for i in year_list:
            response3 = requests.get(i)
            soup3 = BeautifulSoup(response3.text,'lxml')
      
    # Find the pdf now
        for pdf in soup3.find_all('li', class_='file'):
            pdf_link = pdf.a.text
            # print(pdf_link)
    
    '''
    We have to divide the pdfs in to june and november 
    according to their corresponding year

    '''


 



