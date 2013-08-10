=======
pystex
=======

Python API client for StackExchange APIv2.1

## Installation

### To Run
* pip install requests

### To Develop
Nothing specific now

## Usage

	from stackexchange import Stackexchange

	client = Stackexchange({Your API Key})
	result = client.users.get()