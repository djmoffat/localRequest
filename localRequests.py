#!/usr/bin/env python

import requests
import json
from collections import OrderedDict

class getRequest():
	dirPath = None


	def __init__(self,dirPath='data/',forceUpdate=False,forceLocal=False,timeout=0,url=None):
		self.dirPath = dirPath
		self.forceUpdate = forceUpdate
		self.forceLocal = forceLocal
		self.timeout = timeout
		self.url = url
		self.f = None

		if url is not None:
			self.filePath = '/'.join(arg.strip('/') for arg in [dirpath,url]) + '.json'
			try:
				self.f = open(filePath,'r') 
				self.data = json.load(self.f)
			except IOError: 
				print 'Error: File does not appear to exist.'

	def get(self,url=None,params=[]):
		if self.url is not None:
			if url is not None and url != self.url:
				print 'Error - URL already defined'
			return readData(params)
		else #self.url is None

			print 'Not implemented yet'

	def readData(params):
		if params is None:
				return self.data
			else:
				return self.data[makeParamPayload(params)]

	def makeParamPayload(params):
		paramKey=[]
		for key, value in sorted(params.items()):
			paramKey.append(str(key) + '=' + str(value))
		return '&'.join(paramKey)




