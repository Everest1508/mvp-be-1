# API Reference
## API Endpoints
#### Signup
```Endpoint: POST /signup/```

Parameters:
```
name (string, required): User's name
email (string, required): User's email
phone (string, required): User's phone
age (integer, required): User's age
college (string, required): User's college
password (string, required): User's password
```
***

#### Login

```Endpoint: POST /login/```

Parameters:
```
email (string, required): User's email
password (string, required): User's password
```
***
#### List Users

```Endpoint: GET /users/```
***

#### List/Create Colleges

```Endpoint: GET/POST /colleges/```

Parameters (POST):

```
title (string, required): Title of the college
image (file): Image of the college
```
***
#### List/Create Games


```Endpoint: GET/POST /games/```


Parameters (POST):
```
title (string, required): Title of the game
image (file): Image of the game
```
***

#### Verify OTP

```Endpoint: POST /verify/```


Parameters:
```
email (string, required): User's email
otp (string, required): OTP (One-Time Password)
```
***

#### Create SubEvent

```Endpoint: POST /subevent/```

Request Body:
```
{
title: sub event title
game: Kho-Kho # game title not id
description: description
rules: rules
main_event_id: 3
}
```
***


#### Add User to SubEvent

```Endpoint: POST /subevent/<int:id>/```

Parameters:
```
id (integer, path, required): Event ID
```
Request Body:
```
{
id: 2 # Assuming the User ID is 2
}
```
***

#### User Event
```Endpoint: GET /myevent/```
***

#### Add SubEvent to MainEvent

```Endpoint: PUT /mainevent/<int:id>/```

Parameters:
```
id (integer, path, required): MainEvent ID
```
Request Body:

```
{
  id: 1 # Assuming the SubEvent ID is 1
}
```