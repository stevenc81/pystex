=======
pystex
=======

Python API client for StackExchange APIv2.1

## Installation

### To Run
	pip install pystex

### To Develop
Nothing specific now

## Usage

	from pystex import Stackexchange
    from pystex import APIError

	client = Stackexchange({Your API Key})

    try:
	   result = client.users.get()
    except APIError as e:
        print e