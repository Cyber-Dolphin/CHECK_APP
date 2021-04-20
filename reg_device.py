from gpapi.googleplay import GooglePlayAPI

server = GooglePlayAPI("it_IT", "Europe/Rome")

mail = "myemail@gmail.com"
passwd = "mypasswd"

server.login(mail, passwd, None, None)

gsfId = server.gsfId
authSubToken = server.authSubToken

print(gsfId)
print(authSubToken)