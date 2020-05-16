from twilio.rest import Client

account_sid = 'AC700dbafe6b0596be8b2534f0199737b7'
auth_token = '0471140af15f2efa8932966c5279a8e1'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12073863543',
    body='Hi, Arfiz',
    to='+8801764144774'
)

print(message.sid)
