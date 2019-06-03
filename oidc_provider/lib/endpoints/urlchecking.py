import urllib.parse

def canonicalise_url(url):
    """
    If the URI has no path component (i.e. it's just hxxp://host), add a trailing slash.
    """
    split_url = urllib.parse.urlparse(url)

    if split_url.path == '':
        url = urllib.parse.urlunparse(urllib.parse.ParseResult(
            scheme=split_url.scheme,
            netloc=split_url.netloc,
            path='/',
            params=split_url.params,
            query=split_url.query,
            fragment=split_url.fragment))

    return url

def redirect_uri_valid(requested_redirect_uri, redirect_uris):
    return requested_redirect_uri in redirect_uris
    redirect_uris = {canonicalise_url(uri) for uri in redirect_uris}
    return canonicalise_url(requested_redirect_uri) in redirect_uris
