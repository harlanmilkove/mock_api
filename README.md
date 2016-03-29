Mock API
===

This is a simple RESTFul API help for debugging integrations that require a service.


### Starting the test server.

0. ``` pip install -r requirements.txt ```
0. ``` python start_server.py ```

### Example

```
curl \
  -XPOST \
  -d '{"type": "purchase", "id": "buyer@example.com", "amount": 13.37}' \
  http://localhost:5000/webhook-debugger
```

```json
{
  "event": {
    "amount": 13.37,
    "id": "buyer@example.com",
    "type": "purchase"
  }
}
```
