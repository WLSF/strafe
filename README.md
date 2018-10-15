# Strafe API
> A RESTFul API which connects to a twitch channel, track the messages and gives a classification of the chat mood.

This project were made using:
- Flask
- gunicorn
- pytest
- logging
- DGRAM sockets (UDP)
- STREAM sockets (TCP)

# The project:

### Structure:

```
.
├── api                     # RESTful API containing all the services
│   ├── db                  # the local sqlite db file
│   ├── resources           # the SCHEMA file
│   ├── src                 # All the source codes
│   ├── tests               # Unit and integration tests
│   ├── Dockerfile        
│   ├── requirements.txt    
│   └── settings.py
├── twitch                  # Twitch server (UDP connection with the API) 
│   ├── src                 
│   ├── tests
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Running the project:

```
# inside the strafe folder
pip install -r api/requirements.txt # Considering that you've a virtualenv with python 3
flask init-db
docker-compose up --build
```

> To run the project you must have .env files

> api/.env (example)
```
DATABASE=api/db/strafe.db
SCHEMA=../resources/schema.sql

SERVER=twitch
PORT=49152
```
> twitch/.env (example)
```
DATABASE=db/strafe.db

SERVER=irc.chat.twitch.tv
PORT=6667
PASSWORD=twitch token
NICK=twitch nick
```

The project were made using Docker, so it's set to run using the docker-compose command, since it needs to start the twitch and the API services and link them with each other.

> Listening on - localhost:8000


## Testing the project:

```
# inside the strafe folder
pytest -v
```

the coverage is not 100%, I apologize for that.
I hope you can evaluate what I've done.



# Considerations

- The project is not using ORM
- Most of the FLASK and SQLite3 integrations and code were made through studies at the very Flask documentations.
- Since I'm using SQLite, I've created a shared volume on Docker, which means that both services are accessing the same SQLite file, I didn't see any problem at all with this, the API only reads and Twitch only writes. (If I would use a different database, it should be a new service container with the MySQL or PGSQL provider and the services would connect to it remotely)
- The Twitch service creates a Thread to track the channel messages, It is a cool aproach, but to set it as a production service I need more time to implement a good service that treats the thread the way it deserves. :(
- I tried to log as much as possible inside the Twitch service, so everything could be catch on the docker terminal during the development.