# API

GET - `/create_your_circle`

Link to create form with key

POST - `/api/submit_circle_post`

Creates circle

PARAMS:

uh : Found in modhash of create_your_circle
title: name of circle
votekey: key to join (can be left blank to default)
id: found in form id of create_your_circle
renderstyle: ? html

GET - `/user/<username>/circle/embed`

Field for user circles

POST - `/api/guess_voting_key.json`

id: id field, found in id of embed link
vote_key: value of key

RESPONSE

{"Guess": value}

POST - /api/circle_vote.json?dir=<>&id=<>

PARAMS:

id: id field, same as guess voting key
dir: 1 or -1 for join or betrau
vh: found in vote hash in embed
isTrusted: ? false
