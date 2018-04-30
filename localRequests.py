#!/usr/bin/env python

import requests
import pickle
import time
import pdb

timestamp = time.time()

def get(url,params=None,timeout=0):
	dirpath = '/Volumes/Internal/Documents/localRequest/data/'
	filePath = dirpath + url.replace('/','__') + '.pkl'
	if params is not None:
		payload = makeParamPayload(params)
	else:
		payload = None
	try:
		fn = open(filePath,'r') 
		data = pickle.load(fn)
		timestamp = data['timestamp']
		fn.close()
		if payload not in data:
			data[payload] = postRequests(url,params,timeout)
			timestamp = time.time()
			data['timestamp'] = timestamp
			fn = open(filePath,'w') 
			pickle.dump(data,fn)
			fn.close()
		return data[payload]
	except IOError: 
		print 'Error: File does not appear to exist.'
		data = dict()
		data[payload] = postRequests(url,params,timeout)
		timestamp = time.time()
		data['timestamp'] = timestamp
		fn = open(filePath,'w+') 
		pickle.dump(data,fn)
		fn.close()
	return data[payload]

def postRequests(url,params,timeout):
	# print 'posting request'
	waitTime = time.time() - timestamp
	if waitTime <= timeout:
		time.sleep(timeout-waitTime)
	data = requests.get(url, params = params)
	return {'content':data.content,'url':data.url,'headers':data.headers,'status_code':data.status_code,'reason':data.reason}
	
def makeParamPayload(params):
	paramKey=[]
	for key, value in sorted(params.items()):
		paramKey.append(str(key) + '=' + str(value))
	return '&'.join(paramKey)




