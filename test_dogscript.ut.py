from dogscript import Dog_breeds
import unittest
#Jawaun Brown-2018

class TestDogScript(unittest.TestCase):
    #unit testing the crucial methods to ensure that my program would work in a prod. environment
    #unit test also allows me to ensure functionality each time even a tiny part of my program is edited
    def setUp(self):
        self.dbu = 'https://www.akc.org/dog-breeds/'
        self.dogsoup = Dog_breeds.get_dog_soup(self.dbu)
        self.links = Dog_breeds.get_all_links(Dog_breeds.get_dog_soup(self.dbu))
        #for each test case we want to have the right soup object to work with
        #as well as the links to test our final method

    def test_get_all_dogs(self):
        first_dog ='affenpinscher'
        soup = self.dogsoup
        r = Dog_breeds.get_all_dogs(soup)
        thrown = r[0]
        self.assertEqual(thrown.lower(), first_dog)
        #ensures that the right links are checked and the right value is returned from the site we query

    def test_set_dog_dict(self):
        doggyies = Dog_breeds.get_all_dogs(self.dogsoup)
        dl = self.links
        k9map = Dog_breeds.set_dog_dict(doggyies, dl)
        first= k9map['Affenpinscher']
        testy = 'https://www.akc.org/dog-breeds/affenpinscher/'
        self.assertEqual(first, testy)
        #ensures that the correct ordering as well as correct values are present
        #when we create a dict of dog names and links

    def tearDown(self):
        gc.collect()
        #clears the heap of the variables we are no longer using

if __name__ == '__main__':
    unittest.main()
