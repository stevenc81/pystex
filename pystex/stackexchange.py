import requests, urllib
import collections
import json

_HTTP_GET = 0
_HTTP_POST = 1

class APIError(StandardError):
    """
    APIError contains json message indicating failure
    """
    def __init__(self, error_id, error_message, error_name, request,  *args, **kwargs):
        self.error_id = error_id
        self.error_message = error_message
        self.error_name = error_name
        self.request = request
        super(StandardError, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(StandardError, self).__str__() + '\n' \
        'APIError: %s: %s\n%s\nURL: %s' % \
        (self.error_id, self.error_name, self.error_message, self.request)

def _encode_params(**kwargs):
    """
    Do url-encode parameters

    >>> _encode_params(a=1, b='R&D')
    'a=1&b=R%26D'
    >>> _encode_params(a=u'\u4e2d\u6587', b=['A', 'B', 123])
    'a=%E4%B8%AD%E6%96%87&b=A&b=B&b=123'
    """

    args = []
    for k, v in kwargs.iteritems():
        if isinstance(v, basestring):
            qv = v.encode('utf-8') if isinstance(v, unicode) else v
            args.append('%s=%s' % (k, urllib.quote(qv)))
        elif isinstance(v, collections.Iterable):
            for i in v:
                qv = i.encode('utf-8') if isinstance(i, unicode) else str(i)
                args.append('%s=%s' % (k, urllib.quote(qv)))
        else:
            qv = str(v)
            args.append('%s=%s' % (k, urllib.quote(qv)))
    return '&'.join(args)

def _encode_ids(*args):
    """
    Do url-encode resource ids
    """

    ids = []
    for v in args:
        if isinstance(v, basestring):
            qv = v.encode('utf-8') if isinstance(v, unicode) else v
            ids.append(urllib.quote(qv))
        else:
            qv = str(v)
            ids.append(urllib.quote(qv))

    return ';'.join(ids)


def _http_call(url, method, auth, *args, **kwargs):
    params = _encode_params(**kwargs)
    ids = ''
    credentials =''
    url_format_str = '%s%s?%s'

    if args:
        ids = _encode_ids(*args)
        url_format_str = '%s/%s?%s'
    if auth:
        credentials = _encode_params(**auth)
        url_format_str += '&%s'

    http_url = url_format_str % (url, ids, params, credentials) \
               if method == _HTTP_GET else url

    try:
        result = requests.get(http_url)
    except requests.exceptions.ConnectionError as e:
        raise APIError('ConnectionError', 'ConnectionError', 'ConnectionError',
                       http_url, e)

    try:
        result = json.loads(result.text)
    except ValueError as e:
        raise APIError('ValueError', result.text, 'ValueError', http_url, e)

    if 'error_id' in result:
        raise APIError(result['error_id'], result['error_message'],
            result['error_name'], http_url)

    return result


class Stackexchange(object):
    """
    Stackexchange uses dot notation when accessing Stackexchange API
    """

    def __init__(self, app_key=None, domain='api.stackexchange.com', \
        site='stackoverflow', version='2.1'):

        self.app_key = str(app_key)
        self.api_url = 'http://%s/%s/' % (domain, version)
        self.site = site

    def __getattr__(self, attr):
        if '__' in attr:
            return getattr(self.get, attr)
        return _Callable(self, attr)


class _Executable(object):

    def __init__(self, client, method, path):
        self._client = client
        self._method = method
        self._auth = None if client.app_key is None else {'key': client.app_key}
        self._path = path

    def __call__(self, *args, **kwargs):
        return _http_call('%s%s' % (self._client.api_url, self._path), \
            self._method, self._auth, *args, site=self._client.site, **kwargs)

    def __str__(self):
        return "_Executable (%s %s)" % (self._method, self._path)

    __repr__ = __str__

class _Callable(object):

    def __init__(self, client, name):
        self._client = client
        self._name = name

    def __getattr__(self, attr):
        if attr == 'get':
            return _Executable(self._client, _HTTP_GET, self._name)
        if attr == 'post':
            return _Executable(self._client, _HTTP_POST, self._name)
        name = '%s/%s' % (self._name, attr)
        return _Callable(self._client, name)

    def __str__(self):
        return "_Callable (%s)" % self._name

    __repr__ = __str__