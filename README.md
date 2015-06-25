<h1>PyVoat</h1>
A simple python3 Wrapper for Voat.co's API 


<h2>Getting Started</h2>
1. Install PyVoat by entering "pip install PyVoat"
2. Register an api key and obtain an access token from Voat.co
3. Enjoy PyVoat!

<h2>Example</h2>
<h3>This is an example of how to use PyVoat from example.py</h3>
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
