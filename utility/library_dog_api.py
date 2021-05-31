
import json, ast,datetime,argparse, time
import requests,urllib3, random
from  .oauth2_test import  auth,set_env_flag,get_bearer_token
from .common_utility.py import Util
from .publish_subscribe import Api

class DogCommandQueryHost():
	''' This class publishes a json object via rest post  '''
	def __init__(self,env,config_path='../configs'):
		# self.start = datetime.datetime.now()
		init(autoreset=True)
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		self.environment =env
		self.SetUp()

	def SetUp(self):
		self.utility = Util() 
		self.send_request= Api()
		self.environment_config = self.utility.get_test_data_json(self.environment)
		self.api_client_ = self.utility.get_test_data_json(f"/config/client_account_{self.environment}")

		print('\n\n Environment: ',self.environment_config)
		self.endpoints = self.utility.get_test_data_json('endpoints')
		self.dogbreed_endpoint= self.endpoints['dog_breed']
		self.pet_urls= self.environment_config['dog_api']

	def get_backend_token(self):
		fake_auth=self.utility.get_guuid_str()
		auth =  auth(self.environment,)



	def get_headers(self, default='no-auth'):
		headers={'accept':'application/json', 'X-Correlation-ID': self.utility.get_guuid_str()  }
		if default in ('no-auth'):
			return headers
		else:
			headers.update({'Authorization':self.backend_token})
			return headers

	def get_dog_breedlist(self):
		url="{0}/{1}".format(self.pet_urls['pet_url'],self.dogbreed_endpoint['breed_list'])
		return self.send_request.query("GET",url,'', headers=self.get_headers('no-auth'))


if  __name__ == "__main__":
    DogCommandQueryHost.get_dog_breedlist()
