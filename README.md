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

	from pystex.stackexchange import Stackexchange

	client = Stackexchange({Your API Key})
	result = client.users.get()