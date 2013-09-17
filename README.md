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

In case of having variables for API calling. For example:

    http://api.stackexchange.com/2.1/tags/python/top-answerers/all_time?pagesize=30&site=stackoverflow

Please note the API **tags/{tag}/top-answerers** allow a tag to be a variable. In such cases. It's safe to use `__getattr__()` directly. The pystex for above example will be:

    skill = 'python'
    result = api_client.tags.__getattr__(skill).__getattr__('top-answerers').all_time.get(pagesize=30, page=1)

It's also worth to note API url with hyphen isn't allowed in Python language, thus `__getattr__()` was used.