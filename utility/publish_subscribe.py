import json, ast
import argparse
import requests
# import aiohttp

class Api():
	''' This class publishes a json object via rest post request  and also makes rest get query request'''

	def publish(self, url, payload={}, headers = {'content-type': 'application/json'}, proxy={},params={}, verify_=False,timeout=35):
		''' Post data payloads to a rest api and return the result '''
		session = requests.Session()
		session.trust_env = False
		res = None
		if (proxy == {}):
			if(params == {}):	
				try:
					res = session.post(url,headers=headers, data=payload, verify=verify_, timeout=timeout )
				except Exception as e:
					print (e)
			else:    				    				
					try:
						res = session.post(url,headers=headers, data=payload, verify=verify_, timeout=timeout, params=params )
					except Exception as e:
						print (e)
			
		else:
			if(params == {}):	
				try:
					res = session.post(url,headers=headers, data=payload, verify=verify_, timeout=timeout, proxies=proxy )
				except Exception as e:
					print (e)
			else:
					try:
						res = session.post(url,headers=headers, data=payload, verify=verify_, timeout=timeout, proxies=proxy, params=params)
					except Exception as e:
						print (e)
 
		return res	

	def n_publish(self, url, payload, number):
		result = []
		for i in xrange(0,number):
			res = self.publish(url,payload)
			result.append(res)
		return result
	
	def query(self, url, query_data,headers, proxy={}, verify = False,timeout=35):
		''' Post data payloads to a rest api and return the result '''
		session = requests.Session()
		session.trust_env = False
		res = None
		if (proxy == {}):
			try:
				print ('GET :',url+query_data,'  Headers :',headers)
				res = session.get(url+query_data, headers= headers, verify=verify, timeout=timeout)
			except Exception as e:
				raise (e)
		else:
			try:
				print (url+query_data)
				res = session.get(url+query_data, headers= headers, verify=verify, timeout=timeout,  proxies=proxy)

			except Exception as e:
				raise (e)

		return res
