# Design a chat service like messenger or whatsapp

## Features

- One to one chatting
- Online, Sent/ Read
- Send picture or any documents
- Database
- Security

### We cannot use HTTP here.
- HTTP cannot initilize the request. It can only send responses. So when a user wants to send messages to other user, user a will sent the request but http won't be able to sent it back to other user.
- Alternatives are
    - Websocket (Bidirectioanl): Works best for chat service
    - BOSH(Bidirectional Stream Over Synchronized HTTP)
    - Long Pool HTTP