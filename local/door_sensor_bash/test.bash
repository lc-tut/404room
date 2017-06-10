#!/bin/bash

TOKEN='YourTOKEN'

curl -XPOST -d "token=$TOKEN" -d "pretty=1" "https://slack.com/api/auth.test"

echo
