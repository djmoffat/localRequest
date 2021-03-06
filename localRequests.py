#!/usr/bin/env python

import os
import requests
import pickle
import time
import pdb

timestamp = time.time()
debug = False


def get(url, params=None, timeout=0, source=None, verbose=False, path=None):
    '''
	* `url` is the classic post url
	* `params` are the standard parameters to post to a url, and used as the key in the storage dict.
	* `timeout`, in seconds, will take a timestamp record at the previous post requests, and if necessary, perform a wait function 
	to ensure the specificed time has elapsed.
	* `source` options: `None`, `local`, `remote`
	 	* `None` (default): will look up local files unless it does not exist, where a post request will be made and saved
	 	* `local`: will force only use of local files, and return None type for a parameter option not used before
	 	* `remote`: will force a pull and update of all local files, overwriting each one
	* `verbose`: print out of posting requests and waiting time, every time it is required
    * `path`: The directory path that all pickle files will be stored and read from
	'''
    if path is None:
        dirpath = os.path.realpath(__file__).replace('localRequests.py', 'data/')
    else:
        dirpath = path
        # print dirpath
    filePath = dirpath + url.replace('/', '__') + '.pkl'

    global timestamp
    global debug
    debug = verbose
    if params is not None:
        payload = makeParamPayload(params)
    else:
        payload = None
    try:
        fn = open(filePath, 'r')
        data = pickle.load(fn)
        if 'timestamp' in data.keys():
            timestamp = data['timestamp']
        else:
            data['timestamp'] = timestamp
        fn.close()
        if source == 'local':
            if payload not in data:
                return None
        else:
            if payload not in data or source == 'remote':
                data[payload] = postRequests(url, params, timeout)
                timestamp = time.time()
                data['timestamp'] = timestamp
                fn = open(filePath, 'w')
                pickle.dump(data, fn)
                fn.close()
        return data[payload]
    except IOError:
        if debug:
            print 'File does not appear to exist - Creating File'
        if source == 'local':
            print 'Cannot create new file and populate where source = local'
            return None
        else:
            data = dict()
            data[payload] = postRequests(url, params, timeout)
            timestamp = time.time()
            data['timestamp'] = timestamp
            fn = open(filePath, 'w+')
            pickle.dump(data, fn)
            fn.close()
    return data[payload]


def postRequests(url, params, timeout):
    if debug:
        print 'posting request'
    waitTime = time.time() - timestamp
    if waitTime <= timeout:
        if debug:
            print 'waiting for ' + str(timeout - waitTime) + 's'
        time.sleep(timeout - waitTime)
    data = requests.get(url, params=params)
    return {'content': data.content, 'url': data.url, 'headers': data.headers, 'status_code': data.status_code,
            'reason': data.reason}


def makeParamPayload(params):
    paramKey = []
    for key, value in sorted(params.items()):
        paramKey.append(str(key) + '=' + str(value))
    return '&'.join(paramKey)
