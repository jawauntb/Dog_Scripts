import requests
from bs4 import BeautifulSoup
#Jawaun Brown-2018
class Dog_breeds():
    # a class for retrieving links and names of dog breeds from the American Kennel Club
    global DOG_BREED_URL
    DOG_BREED_URL = 'https://www.akc.org/dog-breeds/'
    #use this URL as a constant

    def get_dog_soup(url):
        dogsoup = 'error'
        # Query url and return the html to a variable
        try:
            newpage = requests.get(url)
            #call the url to get a response object
            texts = newpage.text
            # Parse the page and save it in the soup
            dogsoup = BeautifulSoup(texts, 'html.parser')
        except requests.exceptions.RequestException as e:
            #let us know about failed requests
            print (e + 'invalid http request %d' %(newpage.status_code))
            #if no failures, return the soup
        return(dogsoup)


    def get_all_dogs(broth):
        #returns a list of all dog breed names
        doggies = broth.find_all('h3', {'class': 'breed-type-card__title mt0 mb0 f-25 py3 px3'})
        #find the html with these qualities because it contains our relevant info
        doglist = []
        try:
            for doge in doggies:
                newdog = doge.get_text().strip()
                #remove any text that is not the dog breed's name
                doglist.append(newdog)
                #if there is a dog add it to our list of dogs
            alphadog=sorted(doglist, key=str.lower)
            #sort our doglist in abc order
        except TypeError as e:
            #check to make sure there is a non-empty value at each 'doge'
            print(e + 'TypeError: check if breed assigned value of NONE')
            #finally, return the list of dog breed names
        return (alphadog)

    def get_all_links(soups):
        #returns a list of all dog breed links
        mylinks = soups.find_all('a',{'class':'d-block relative'})
        #find the html with these qualities because it contains our relevant info
        linksto = []
        try:
            for linksof in mylinks:
                stored = linksof['href']
                #find the value with each tag that is stored at <a href="vwx.yz" ><a/>
                linksto.append(stored)
            orderlink = sorted(linksto, key=str.lower)
            #sort the links in abc order to match up with the dog list names
        except TypeError as e:
            #check to make sure there is a non-empty value at each 'linksof'
            print(err + 'TypeError: check if link assigned value of NONE')
        #finally, return the list of links
        return (orderlink)

    def set_dog_dict(dogs, links):
        newdict={}
        #initialize a dictionary to hold our values
        d=len(dogs)
        l=len(links)
        #find the length of each, they should match up in the end
        dictlen=0
        i=0
        if (d>l):
            dictlen=d
        else:
            dictlen=l
            #the above if statement uses the longer of the two lengths as the number of times to iterate through the values
        while i < dictlen:
            try:
                #at each i-th position the dictionary will get the dog[i] added as a key and the link[i] as a value
                newdict[dogs[i]]=links[i]
                i+=1
            except IndexError as e:
                print(e + 'Index is out of bounds')
        testlen=len(newdict)
        #then we make sure that the dictionary is the correct length
        try:
            (testlen==d==l)
        except ValueError as e:
            print(e + 'lengths of arrays and dictionaries do not match')
            #finally, return the dictionary of dog breeds and their links
        return(newdict)
