# Python Client for StackExchange API

## Install

### To Run
* pip install requests

### To Develop
Nothing specific now

## Usage

	from stackexchange import Stackexchange

	client = Stackexchange({Your API Key})
	result = client.users.get()