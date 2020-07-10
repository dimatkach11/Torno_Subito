#
# ! URL : Uniform Resourse Locator
# * Is a set of characters that unequely identifies the address of a resource on a computer network, such as a document, an image, a video, tipically present on a host server and made accessible to a client. It is mostly used to indicate web resources (http), resources recoverable through file transfer protocols (ftp), remote shares(smb) or acces to external system (ssh). The resolution of the URL in IP address, necessary for routing whith the IP protocol, is done via DNS. The structure of a URL normally consists of six parts, some of which are optional:

# * protocol://[username[:password]@]host[:port]</path>[?querystring][#fragment]

# * HOST: Identifies the server where the resources resides. It can be directly rapresented by an IP address or more commonly a domain name that the software converts into an ip address using the DNS service. 
# * PORT(optional): Identifies the network service port to wich the request should be sent. The port number can be omitted when it correspondes to the standard port associated with the protocol indicated by the URL (e.g. 80 fo HTTP or 443 for HTTPS).
# * PATH(optional): in the file system of the server that identifies the resource (usually a web page, an image or a multimedia file). If the file name is not specified. the server can be configured to return a defoult file.
# * QUERYSTRING(optional): if required, you can add a string query at the end of the url by separating it using the "?" symbol. The query string is a character string that allows you to pass one or more parameters to the server. Normallly, the querystring has this format: [...]?parameter1=value1&parameter2=value2.
# * FRAGMENT(optional): if present, indicates a part or position within the resource.

# ! urllib.request
# * Is a Python module for fetching URLs(Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cockies, proxies and so on. These are provided by objects called handlers and openers. 

import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
    #print(html)

# HTTP is based on requests and responses - the client makes requests and servers send responses. urllib.request mirrors this with a Request object which represents the HTTP request you are making. In its simplest form you create a Request object that specifies the URL you want to fetch. Calling urlopen with this Request object returns a response object for the URL requested. This response is a file-like object, which means you can for example call .read() on the response:
req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    #print(the_page)

# For parsing we only need urllib and re i.e regular expression. By using both of these libraries we can fetch the data on web pages. Note that parsing of websites means that fetch the whole source code and that we want to search using a given url link, it will give you the output as the bulk of HTML content that you can’t understand. 
import urllib.parse
import re

url = 'http://www.pythonprogramming.net'
values = {
    's': 'basics',
    'submit': 'search'
}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

#for eachP in paragraphs:
    #print(eachP)

# *________________________________________________________________________________

response = urllib.request.urlretrieve('https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png', 'the_url/downloaded_files/tux.png')
#print(response)
#urllib.request.urlcleanup() # clean cache
