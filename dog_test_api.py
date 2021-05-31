from  utility.library_dog_api import DogCommandQueryHost  

if  __name__ == "__main__":
    dog =DogCommandQueryHost('staging')
    breed_list_results =dog.get_dog_breedlist()
    print('Breed List Results: ',breed_list_results,breed_list_results.json())
