## [OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)

 - Browse to a product page and click Check stock with Burp intercepting
 - Find the stock check request in Proxy > HTTP history and send it to Repeater
 - In Repeater, change the storeID parameter value to 1|whoami
 - Send the request — confirm the current username appears in the response to solve the lab


## [Blind OS command injection with time delays](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)

 - Navigate to the feedback form and submit it with Burp intercepting
 - Find the POST /feedback/submit request in Proxy > HTTP history and send it to Repeater
 - Change the email parameter value to x||ping+-c+10+127.0.0.1||
 - Send the request — confirm the response takes ~10 seconds to return, proving blind injection to solve the lab


## [Blind OS command injection with output redirection](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection)

 Navigate to the feedback form and submit it with Burp intercepting
 Find the POST /feedback/submit request in Proxy > HTTP history and send it to Repeater
 Change the email parameter value to ||whoami>/var/www/images/output.txt||
 Send the request — confirm a normal (non-delayed) response
 Intercept a product image request (or find one in history) and send it to Repeater
 Change the filename parameter value to output.txt
 Send the request — confirm the whoami output appears in the response to solve the lab


## [Blind OS command injection with out-of-band interaction](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band)


**Need burp collaborator**


## [Blind OS command injection with out-of-band data exfiltration](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band-data-exfiltration)

**Need burp collaborator**

