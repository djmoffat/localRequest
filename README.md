# localRequest
Python requests module modification that allows for storing and pulling data from local store, rather than posting requests to servers every time - primarily for testing/bandwidth management


Module is a work in progress, current usage demo:

```python
import localRequests as lr

lr.get(url,params=paramsAsDict, timeout=5)
```

## Parameters
* `url` is the classic post url
* `params` are the standard parameters to post to a url, and used as the key in the storage dict.
* timeout, in seconds, will take a timestamp record at the previous post requests, and if necessary, perform a wait function 
to ensure the specificed time has elapsed.
* `source` options: `None`, `local`, `remote`
    * `None` (default): will look up local files unless it does not exist, where a post request will be made and saved
    * `local`: will force only use of local files, and return None type for a parameter option not used before
    * `remote`: will force a pull and update of all local files, overwriting each one
* `verbose` print out of posting requests and waiting time, every time it is required


Please get in touch for any questions