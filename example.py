import json
import PyVoat

v = PyVoat.PyVoat("token","pubkey")

messages = v.getAllMessages()
user = v.getUser("healdb")
subverse = v.getSubverse("api")

#Loop through all unread messages
for message in messages:
  print(message.author)
  print(message.body)

print(user.getInfo())

#Loops through each post in the subverse
submissions = subverse.getSubmissions()
for post in submissions:
  print(post.author)
  comments= post.getComments()
  for comment in comments:
    print(comment.body)
