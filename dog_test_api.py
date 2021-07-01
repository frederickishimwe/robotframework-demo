from  utility.library_dog_api import DogCommandQueryHost  
from  utility.oauth2_test import get_basic_auth_credentials  
import keyboard



def basic_auth( environment="staging"):
    credentials = get_basic_auth_credentials(environment)
    keyboard.write(credentials['username'])
    keyboard.send("tab")
    keyboard.write(credentials['password'])
    keyboard.send("enter")
    # print('Authenticated')


if  __name__ == "__main__":
    dog =DogCommandQueryHost('staging')
    breed_list_results =dog.get_dog_breedlist()
    print('Breed List Results: ',breed_list_results,breed_list_results.json())
