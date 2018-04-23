# localRequest
Python requests module modification that allows for storing and pulling data from local store, rather than posting requests to servers every time - primarily for testing/bandwidth management


Module is a work in progress, current usage demo:

```python
import localRequests as lr

lr.get(url,params=paramsAsDict)
```

Please get in touch for any questions