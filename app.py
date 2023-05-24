import falcon
import time
import json
import secrets
import hashlib

class IOBoundWorkloadRoute():
    
    def on_get(self, request, response):
        a = (request.params['index'], request.params['index'], request.params['index'], request.params['index'])
        response.text = json.dumps({
            'result': 'ok'
        })

class ListWorkloadRoute():
    
    def on_get(self, request, response):
        a = [request.params['index'], request.params['index'], request.params['index'], request.params['index']]
        response.text = json.dumps({
            'result': 'ok'
        })

class TupleWorkloadRoute():
    
    def on_get(self, request, response):
        a = [request.params['index'], request.params['index'], request.params['index'], request.params['index']]
        response.text = json.dumps({
            'result': 'ok'
        })
        
class HeavyWorkloadRoute():
    
    def on_get(self, request, response):
        counter = 0
        val = 2
        while counter < 20:
            val = val * val
            counter+=1
            
        response.text = json.dumps({
            'result': 'ok'
        })
        

app = falcon.App()
app.add_route("/io-bound-workload", IOBoundWorkloadRoute())
app.add_route("/heavy-workload", HeavyWorkloadRoute())
app.add_route("/list-workload", ListWorkloadRoute())
app.add_route("/tuple-workload", TupleWorkloadRoute())