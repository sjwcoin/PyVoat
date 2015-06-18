import requests
import json
import objects
frontpoint = "https://fakevout.azurewebsites.net/api/"
class PyVoat:
    def __init__(self):
        f=open("config.txt")
        lines=f.readlines()
        trash, token = lines[0].split(":")
        trash, pubkey = lines[1].split(":")
        self.headers = {'content-type': 'application/json', 'Authorization': "Bearer " + token.rstrip(),'Voat-ApiKey': pubkey.rstrip()}
    def getUser(self,username):
        user = objects.user(username)
        return user
    def getSubverse(self, subverse):
        subverse = objects.subverse(subverse)
        return subverse
    def getSubmissionById(self,submis):
        response = requests.get(frontpoint + "v1/submissions/"+submis, headers=self.headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        submission = objects.submission(data['subverse'],data['title'],data['userName'],data['url'],data['content'],submis)
        return submission
    def getCommentById(self,comid):
        response = requests.get(frontpoint + "v1/comments/"+comid, headers=self.headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        comment = objects.comment(comid, data['subverse'], data['userName'], data['content'], data['parentID'])
        return comment
    def getUsernameMentions(self):
        response = requests.get(frontpoint + "v1/u/messages/Mention/unread", headers=self.headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        messages=[]
        for x in data:
            message = objects.message(x["id"],x["sender"],x["content"])
            messages.append(message)
        return messages
    def getPrivateMessages(self):
        response = requests.get(frontpoint + "v1/u/messages/Inbox/unread", headers=self.headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        messages=[]
        for x in data:
            message = objects.message(x["id"],x["sender"],x["content"])
            messages.append(message)
        return messages
    def getAllMessages(self):
        response = requests.get(frontpoint + "v1/u/messages/All/unread", headers=self.headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        messages=[]
        for x in data:
            message = objects.message(x["id"],x["sender"],x["content"])
            messages.append(message)
        return messages
    def sendMessage(self,user,subject,body):
        post_data = json.dumps({'recipient': user, 'subject': subject, 'message': body})
        response = requests.post(frontpoint + "v1/u/messages", data=post_data, headers=self.headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded
        return data
