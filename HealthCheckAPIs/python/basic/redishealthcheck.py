########################################################################################################
# redisHelathCheck.py
# Hans Kristian Moen
# Copyright IBM Corporation 2016.
#
# Implements a basic healthcheck API
#
# LICENSE: MIT (http://opensource.org/licenses/MIT)
########################################################################################################
########################################################################################################
import os, json
from flask import Flask, jsonify
import redis

# When deploying to Bluemix Watson Service Credentials of bound services are available in VCAP_SERVICES
if os.environ.get('VCAP_SERVICES'):
  services = json.loads(os.environ.get('VCAP_SERVICES'))
  redisuri = str(services['compose-for-redis'][0]['credentials']['uri'])

# Connect to Redis Server
client=redis.from_url(redisuri)

# Setup Flask
port = int(os.getenv('VCAP_APP_PORT', 8080))
app = Flask(__name__)
 
# Setup healthcheck
###########################################################################
## Overall healthcheck will succeed if all specified healthcheck succeeds
## HTTP Return code 200 on success and 500 on failure
##
@app.route("/healthcheck")
def healthcheck():
  # Attempt to connect to get get server information from Redis server to verify successful connectivity and access
  try:
    info = client.info()
    # If connectivity is successful return http 200 with a json object
    resp = jsonify(status='UP')
    resp.status_code = 200
    
  except Exception as e:
    # If connectivity is unsuccessful return http 500 with a json object
    resp = jsonify(status='DOWN')
    resp.status_code = 500
  
  return resp
  


@app.route("/")
def root():
  return '<html><body><a href="/healthcheck">RedisHealthCheck</a></body></html>'
  
app.run(host='0.0.0.0', port=port)
