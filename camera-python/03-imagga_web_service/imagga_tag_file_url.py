
import ConfigParser
import requests
import json

#
# replace "authorization: "Basic ..." with your Authorization in web_service.conf
#
config = ConfigParser.ConfigParser()
config.read('web_service.conf')
authorization = config.get('imagga', 'authorization')

url = "http://api.imagga.com/v1/tagging"
querystring = {"url":"http://playground.imagga.com/static/img/example_photo.jpg"}
headers = {
    "accept": "application/json",
    "authorization": authorization
    }
response = requests.request("GET", url, headers=headers, params=querystring)

# un-comment to see all tags
#print response.text

data = json.loads(response.text.encode("ascii"))
tag = data["results"][0]["tags"][0]["tag"].encode("ascii")
print "Get tag... "
print "<< " + tag + " >>"
