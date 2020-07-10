# 
# ! Cookies
# * Sice the 1980s and tipically used to identifying a client at a server, such as authentication of the X Window System server.
# * Servers send cookies in the HTTP response to the client and web browsers are ecpected to save and send cookies to the server whenever additional requests are made to the web server.
# * This recognition makes it possible to create authentication mechanisms used, for example, for logins; to store data useful for the browsing session, such as preferences on the graphic or linguistic aspect of the site; to track the user's navigation, for example for statistical or advertising purposes; to associate data stored by the server, for example the contents of the shopping cart of an electronic store.
# * Given the implications for the privacy of web surfers, the use of cookies is categorized and regulated in the legal systems of many countries, including Europe, including Italy. 
# * The security of an authentication cookie generally depends on the security of the site that issues it, the user's web browser, and whether the cookie is encrypted or not. Security vulnerabilities may allow hackers to read the cookie's data, which could be used to gain access to user data, or to gain access (with user credentials) to the website to which the cookie belongs.
# * Cookies, and in particular third party cookies, are commonly used to store users' browsing searches; this sensitive data can be a potential threat to users' privacy; this is what led European and US authorities to regulate their use through a law in 2011.  Indeed, European legislation requires all Member State sites to inform users that the site uses certain types of cookies.
# * A cookie is similar to a small file, stored on your computer by websites while you are browsing, useful to save your preferences and improve website performance. This optimizes the user's browsing experience.
# * In detail, a cookie is a small text string sent from a web server to a web client (usually a browser) and then sent back from the client to the server (without modification) each time the client accesses the same portion of the same web domain. Cookies were originally introduced to provide a way for users to store the items they wanted to purchase while browsing the website (the so-called "shopping cart").
# * Oggi, tuttavia, i contenuti del carrello di un utente vengono archiviati in un database sul server, anziché in un cookie sul client. Per tenere traccia dell'utente a cui è assegnato il carrello, il server Web invia un cookie al client che contiene un identificatore di sessione univoco (in genere una lunga serie di lettere e numeri). Poiché i cookie vengono inviati al server ad ogni richiesta del client, l'identificatore di sessione verrà inviato al server ogni volta che l'utente visita una pagina sul sito Web, ciò consente al server di sapere quale carrello della spesa fornire all'utente.
# * Because session cookies only contain a unique session identifier, this makes the amount of personal information that a website can store virtually unlimited. The site is not limited to restrictions on how long the text string that makes up a cookie can be. Session cookies can also help improve page loading times, as the amount of information in a session cookie is small and requires little bandwidth.
# * The main cookie, the one used to store the options for all other cookies, is called a technical (consent) cookie, which is the one that presides over the sending and receiving of the information package (markers). Each domain or part of it that is visited with the browser can set cookies. Since a typical Internet page, for example a newspaper on the net, contains objects from many different domains and each of them can set cookies, it is normal to have many hundreds of cookies in your browser.
# * Cookies are often mistakenly believed to be real programs and this leads to misconceptions. In reality they are simple blocks of data, unable to perform any action on your computer by themselves. 
# * A cookie is an additional header in a request (Cookie:) or response (Set-cookie:) HTTP: in case the server wants to assign a cookie to the user, it will add it among the response headers. The client must note the presence of the cookie and store it in a special area (usually a directory is used where each cookie is stored in a file). The cookie consists of an arbitrary text string, an expiration date (beyond which it should not be considered valid) and a pattern to recognize the domains to which it should be sent. You can set multiple cookies in a single HTTP response.
# * The client web browser will send the cookie back, without any modification, to all HTTP requests that meet the pattern, by the expiration date. The server can then choose to assign the cookie again, overwriting the old one. Resending via pattern allows all subdomains of a given domain to receive the cookie, if desired.
# * Cookies are used to add a status to a stateless protocol. Without cookies there would be no difference on a page loaded before logging in, from the same page loaded afterwards. Since cookies remain in the system for long periods of time, sites can assign an index to the user and keep track of their navigation within the site, usually for the purpose of creating statistics. They can also be used to track navigation on third party sites if these third party sites use content from the site that set the cookie. Usually the advertising on the sites is managed by companies that have advertisements on various websites.
# * The content of the advertisement itself is uploaded directly from their server (via an HTTP request) and displayed in an integrated way on the site that the user wishes to visit. In this way the server of the advertising company will receive from the user's browser the address of the page that is being displayed, and it will be able to send a cookie to the client. Through this mechanism advertising companies can aggregate information about users and build profiles and show them targeted advertisements.
# * The world's most popular search engine, Google, also sends a cookie that stores data about searches, search keywords and user habits.

# * More in detail the different uses of cookies are therefore:

# * To fill the virtual shopping cart in commercial sites (cookies allow us to put or remove items from the shopping cart at any time).

# * To allow a user to login to a website.

# * To customize the web page according to the user's preferences (for example, the Google search engine allows the user to decide how many search results he wants to display per page).

# * To track the user's path (typically used by advertising companies to obtain information about the navigator, his tastes and preferences.)

# * For the management of a site: cookies are used by those who update a site to understand how users visit the site, what path they take within the site. If the path leads to dead ends, the operator can see this and can improve the navigation of the site.
# * To share social network information with other users. Many modern browsers allow you to decide when to accept cookies, but rejecting certain cookies does not allow you to use certain sites (take a website such as Wikipedia as an example).

# * Contrary to popular belief, a cookie is not a small text file: it can be stored in a text file, but not necessarily. In the cookie we can usually find four attributes:

# * Name/value is a variable and a mandatory field.

# * Expiration date is an optional attribute that allows you to set the expiration date of the cookie. It can be expressed as a date, as a maximum number of days or as Now (implies that the cookie is deleted immediately from the user's computer as it expires when it is created) or Never (implies that the cookie is not subject to expiration and these are called persistent).

# * Access Mode (HttpOnly) makes the cookie invisible to JavaScript and other client-side languages on the page.

# * Secure indicates whether the cookie should be transmitted encrypted with HTTPS.

# * The main attribute through which we can divide cookies is their life cycle, which allows us to distinguish them into: 

# * Session cookies: these cookies are not permanently stored on your device and are deleted when you close your browser. Unlike other cookies, session cookies do not have an expiration date, which allows the browser to identify them as such. 

# * Persistent cookies: Instead of disappearing when you close your browser, as with session cookies, persistent cookies expire on a specific date or after a certain period of time. This means that, for the entire lifetime of the cookie (which may be long or short depending on the expiry date decided by its creators), its information will be transmitted to the server each time the user visits the website, or each time the user views a resource belonging to that site from another site (e.g. an advertisement). For this reason, persistent cookies may be used by advertisers to record information about a user's web browsing habits for an extended period of time.

# * With the requests module we can request the value of a cookies, the value will be assigned to a dict type, let’s look an simple cookies request querying the google homepage, for see what cookies they use:

import requests

session = requests.Session()
print(session.cookies.get_dict())
response = session.get('http://google.com')
print(session.cookies.get_dict())

# * In the first snippet we can see the object session instanced in a variable and the print method give to us an empty dict. Using the method get with an url , the result changes giving to us the value of the cookie instaced in the website searched.

import requests

response = requests.get('https://www.20tab.com/')
print(response.cookies)
for cookie in response.cookies:
    print(f'cookie domain = {cookie.domain}')
    print(f'cookie name = {cookie.name}')
    print(f'cookie value = {cookie.value}')
    print('\n') 

# * With the previous code we seeing how to retrieve information from the site we asking the cookie.
