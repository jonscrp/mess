# Channels Concepts

Traditonal Cycle:
Client
Request ->
<- Response 
Server

Modern web
WebSockets and Http2


## What is a channel

An extension to Django's event driven programming

Incoming connections contain a scope. This scope contains information about the incoming message. The scope persists throuhgout the  sockets connections life time(for an http connection this scope lasts a single request) .

## What is a consumer?

An object that handles events(Web Socket connection) and lives for the duration of scope

Each object has its unique channel name and can join groups, allowing both point to point and broadcast.


## Channel Layer

Simmilar to shared memory

A channel is a mailbox where messages can be sent to. Each channel has a name. Anyone who has the name of a channel can send a message to the channel.

A group is a group of related channels. A group has a name. Anyone who has the same name of a group can add/remove a channel to the group by name and send a message to all channels in the group. It is not possible to enumera what channels are in a particular group.

Every consumer instance has an automatically generated unique channel name.