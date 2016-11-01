########################################################################################################
# redisHelathCheck.py
# Hans Kristian Moen
# ©Copyright IBM Corporation 2016.
#
# Uses the healthcheck python package to query and report status: https://github.com/Runscope/healthcheck
#
# LICENSE: MIT (http://opensource.org/licenses/MIT)
########################################################################################################
########################################################################################################
import os, json
from flask import Flask
from healthcheck import HealthCheck
import redis

# When deploying to Bluemix Watson Service Credentials of bound services are available in VCAP_SERVICES
if os.environ.get('VCAP_SERVICES'):
  services = json.loads(os.environ.get('VCAP_SERVICES'))
  redisuri = str(services['compose_for_redis'][0]['credentials']['uri'])

# Connect to Redis Server
client=redis.from_url(redisuri)

# Setup Flask
port = int(os.getenv('VCAP_APP_PORT', 8080))
app = Flask(__name__, static_url_path='')

# Define a test to verify Redis availability
def redis_available():
  try:
    info = client.info()
    return True, {'status':'UP'}
    
  except Exception as e:
    return False, {'status':'DOWN', 'message': e.message}

def someother_test():
  # If there are other relevant dependencies test for these can be added here
  return True, {'status':'UP'}
    
# Setup healthcheck
###########################################################################
## Overall healthcheck will succeed if all specified healthcheck succeeds
## HTTP Return code 200 on success and 500 on failure
##
health = HealthCheck(app, "/healthcheck")
health.add_check(redis_available)
health.add_check(someother_test)


@app.route("/")
def root():
  return '<html><body><a href="/healthcheck">RedisHealthCheck</a></body></html>'
  
app.run(host='0.0.0.0', port=port)
