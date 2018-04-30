#!/usr/bin/env python

import requests
import pickle


def get(url,params=None):
	dirpath = '/Volumes/Internal/Documents/localRequest/data/'
	filePath = dirpath + url.replace('/','__') + '.pkl'
	if params is not None:
		payload = makeParamPayload(params)
	try:
		fn = open(filePath,'r') 
		data = pickle.load(fn)
		fn.close()
		if payload not in data:
			data[payload] = postRequests(url,params)
			fn = open(filePath,'a') 
			pickle.dump(data,fn)
			fn.close()
		return data[payload]
	except IOError: 
		print 'Error: File does not appear to exist.'
		data = dict()
		data[payload] = postRequests(url,params)
		fn = open(filePath,'w+') 
		pickle.dump(data,fn)
		fn.close()
	return data[payload]

def postRequests(url,params):
	print 'posting request'
	data = requests.get(url, params = params)
	return {'content':data.content,'url':data.url,'headers':data.headers,'status_code':data.status_code,'reason':data.reason}
	
def makeParamPayload(params):
	paramKey=[]
	for key, value in sorted(params.items()):
		paramKey.append(str(key) + '=' + str(value))
	return '&'.join(paramKey)




