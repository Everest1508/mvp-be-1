
## API Reference

#### Get all items


## API Reference

#### Get all Data
API Endpoints


```http
Signup: POST /signup/
```

| Parameter |	Type	| Description |
| :-------- | :--------- | :---------- |
| name |	string |	Required. User's name |
| email	| string	| Required. User's email |
| phone	| string	| Required. User's phone | 
| age	 | integer	| Required. User's age |
| college |	string	 | Required. User's college |
| password | 	string | 	Required. User's password |

```http
Login: POST /login/
```
| Parameter |	Type	| Description |
| :-------- | :--------- | :---------- |
| email	| string	| Required. User's email |
| password | 	string | 	Required. User's password |


```http
List Users: GET /users/
```

```http
List/Create Colleges: GET/POST /colleges/
```

| Parameter |	Type	| Description |
| :-------- | :--------- | :---------- |
| title	| string	| Required. Title |


```http
List/Create Games: GET/POST /games/
```

| Parameter |	Type	| Description |
| :-------- | :--------- | :---------- |
| title	| string	| Required. Title |



```http
Verify OTP: POST /verify/
```
| Parameter |	Type	| Description |
| :-------- | :--------- | :---------- |
| email	| string	| Required. User's email |
| otp | 	string | 	Required. otp |

```http
Create SubEvent: POST /subevent/
```

**Request:**
```json
{
  "title": "Event 1",
  "game": 1, 
  "description": "Description of Event 1",
  "rules": "Rules of Event 1",
  "participants": [1, 2, 3]
}
```


```http
Add User to SubEvent: POST /subevent/<int:id>/
```

```<int:id> id is event id```

```json
{
  "id": 2  # Assuming the User ID is 2
}

```


```http
User Event: POST /myevent/<int:id>/
```

```<int:id> id is user id```

