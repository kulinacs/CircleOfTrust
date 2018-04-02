Circle of Trust API
===================

Create Circle
-------------

### User Form

GET - `/create_your_circle`

Form to the create a cirle

### API

POST - `/api/submit_circle_post`

Creates the circle

#### Parameters

`uh`: modhash (can be found in `/create_your_circle`)

`title`: name of the circle to create

`votekey`: password for the circle (can be left blank to autogenerate)

`id`: form id (can be found in `/create_your_circle`)

`renderstyle`: defaults to html, not sure what it does.

Get User Circle
---------------

GET - `/user/<username>/circle/embed`

Link to a user's circle

Circle Operations
-----------------

### Unlock Circle

Unlocks the Circle for the logged in user

POST - `/api/guess_voting_key.json`

#### Parameters

`id`: form id, (can be found in `/user/<username>/circle/embed`)

`vote_key`: password for the circle

#### Response

{"Guess": (true or false)}

### Vote on Circle

Join or Betray a Circle

POST - `/api/circle_vote.json?dir=<>&id=<>`

#### Parameters

`id`: form id, (can be found in `/user/<username>/circle/embed`)

`dir`: operation, 1 or -1 for join or betray

`vh`: vote hash, (can be found as vote_hash in `/user/<username>/circle/embed`)

`isTrusted`: defaults to false, not sure what it does.
