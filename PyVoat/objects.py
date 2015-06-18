import requests
import json
import time
import PyVoat

f=open("config.txt")
lines=f.readlines()
trash, token = lines[0].split(":")
trash, pubkey = lines[1].split(":")
headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' +token.rstrip(),'Voat-ApiKey': pubkey.rstrip()}
frontpoint = "https://fakevout.azurewebsites.net/api/v1/"

class submission:
    def __init__(self,sub,title,username,url,body,subid):
        self.subverse = sub
        self.title = title
        self.id = subid
        self.author =username
        self.url=url
        self.body=body
    def postSubmissionReply(self,value):
        post_data = json.dumps({'value': value})
        response = requests.post(frontpoint + "v/"+self.subverse+"/"+self.id+"/comment", data=post_data, headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        return data
    def getComments(self):
        v = PyVoat.PyVoat()
        response = requests.get(frontpoint + "v/"+self.subverse+"/"+self.id+"/comments", headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        comments=[]
        for x in data:
            comid = str(x['id'])
            comment = v.getCommentById(comid)
            comments.append(comment)
            time.sleep(2)
        return comments
    def delete(self):
        response = requests.delete(frontpoint + "v/"+self.subverse+"/"+self.id,headers=headers)
        return response
class user:
    def __init__(self,user):
        self.user = user
    def getInfo(self):
        response = requests.get(frontpoint + "u/"+self.user+"/info", headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        print(decoded)
        data = decoded['data']
        return data
    def getPrefs(self):
        response = requests.get(frontpoint + "u/preferences", headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        print(decoded)
        data = decoded['data']
        return data
    def getComments(self):
        v = PyVoat.PyVoat()
        response = requests.get(frontpoint + "u/"+self.user+"/comments", headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        comments=[]
        for x in data:
            comid = str(x['id'])
            comment = v.getCommentById(comid)
            comments.append(comment)
            time.sleep(2)
        return comments
    def getSubmissions(self):
        v = PyVoat.PyVoat()
        response = requests.get(frontpoint + "u/"+self.user+"/submissions", headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        posts=[]
        for x in data:
            subid = str(x['id'])
            post = v.getSubmissionById(subid)
            posts.append(post)
            time.sleep(2)
        return posts
class comment:
    def __init__(self,comid,subverse,author,body,parent):
        self.id =comid
        self.subverse=subverse
        self.author=author
        self.body=body
        self.parent = parent
    def postCommentReply(self,value):
        post_data = json.dumps({'value': value})
        response = requests.post(frontpoint + "comments/"+self.id, data=post_data, headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        return data
    def delete(self):
        response = requests.delete(frontpoint + "comments/"+self.id,headers=headers)
        return response
class subverse:
    def __init__(self,subverse):
        self.subverse = subverse
    def info(self):
        response = requests.get(frontpoint + "v/"+self.subverse+"/info", headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        return data
    def getSubmissions(self):
        v = PyVoat.PyVoat()
        response = requests.get(frontpoint + "v/"+self.subverse, headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        posts=[]
        for x in data:
            subid = str(x['id'])
            post = v.getSubmissionById(subid)
            posts.append(post)
            time.sleep(2)
        return posts
    def getComments(self):
        v = PyVoat.PyVoat()
        response = requests.get(frontpoint + "v/"+self.subverse, headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        allData =[]
        for x in data:
            subid= x['id']
            response = requests.get(frontpoint + "v/"+self.subverse+"/"+str(subid)+"/comments", headers=headers)
            json_input = response.json()
            decoded = json.dumps(json_input)
            decoded = json.loads(decoded)
            data = decoded['data']
            allData+=data
            time.sleep(2)
        comments=[]
        for p in allData:
            comid = str(p['id'])
            comment = v.getCommentById(comid)
            comments.append(comment)
            time.sleep(2)
        return comments
    def postSelfSubmission(self,title,content):
        post_data = json.dumps({'title': title, 'content': content})
        print(post_data)
        response = requests.post(frontpoint + "v/"+self.subverse, data=post_data, headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        return data
    def postLinkSubmission(self,title,url):
        post_data = json.dumps({'title': title, 'url': url})
        response = requests.post(frontpoint + "v/"+self.subverse, data=post_data, headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        data = decoded['data']
        return data
class message:
    def __init__(self,mesID, username, content):
        self.id = mesID
        self.author = username
        self.body = content
    def reply(self,text):
        post_data = json.dumps({'value': text})
        response = requests.post(frontpoint + "u/messages/reply/"+str(self.id), data=post_data, headers=headers)
        json_input = response.json()
        decoded = json.dumps(json_input)
        decoded = json.loads(decoded)
        print(decoded)
        data = decoded['data']
        return data
        
    
