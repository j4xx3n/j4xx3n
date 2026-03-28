## [Reflects XSS](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)

- Test if search value is reflected in the html.
  - Inject the following payload:
    ```html
    '<script>alert(1)</script>
    ```

## [Stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)

- Test if comment values are reflected in the HTML
  - Inject the following payload:
    ```html
    '<script>alert(1)</script>
    ```

## [DOM XSS in `document.write` sink using source `location.search`](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)

- Check if search value is reflected in the DOM.
- Check if the value is being written by the document.write function.
  - Break out of the tag with '> by injecting the following payload:
    ```html
    '><script>alert(1)</script>
    ```

## [DOM XSS in `innerHTML` sink using source `location.search`](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)

- Check if search value is reflected in the DOM.
- Check if the value is being written by the location.search function.
- Note: `<script>` tags are filtered out by browsers when injected by the location.search function.
  - Use the following payload to perform xss on the location.search function.
    ```html
    <img src='0' onerror='alert(1)'>
    ```

## [DOM XSS in jQuery anchor `href` attribute sink using `location.search` source](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink)

- Check if there is a parameter for the home page button in the url
- Replace the value with a random string and check if it is reflected in the DOM.

  - Note: This can also lead to an open redirect vulnerability.
  - Inject the following payload:

  ```java
  javascript:alert(1)
  ```

## [DOM XSS in jQuery selector sink using a hashchange event](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event)

- Read the source code for a hashchange function.
- Try to use the hashchange function to autoscroll to a h2 tag.
- Add this line to the expoit server and deliver the payload to the victom:
  ```html
  `<iframe src="https://vulnerable-website.com#" onload="this.src+='<img src=1 onerror=print(1)>'">`
  ```

## [Reflected XSS into attribute with angle brackets HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded)

- Try to inject a random string into the search value.
- Check if you can break out of quotes.
- If angle brackets are encoded inject an event handler.
  - Inject the following payload:
    ```java
    "onmouseover="alert(2)
    ```

## [Stored XSS into anchor `href` attribute with double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded)

- Try to inject a random string into the url feild for a comment.
- If it allows a string without http:// or https:// you should be able to inject a javascript protocal injection.
- Inject this payload:
  ```java
  javascript:alert(1)
  ```

## [Reflected XSS into a JavaScript string with angle brackets HTML encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)

- Inspect if the search term is reflecting inside javascript.
- Break out of the javascript quote and inject the alert() function with the following payload:
  ```java
  j4xx3n'; onload=alert(); var myVar='test
  ```

## [DOM XSS in `document.write` sink using source `location.search` inside a select element](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)

- Look for check stock functionality.
- Read the source code and look for javascript code that uses the `storeId` parameter as a source and the `document.write` function as the sink.
- Add storeId as a parameter in the URL and check if the value is added as a new store.
- If you suceffuly injected a new store value inject the following payload in to the storeId value:
  ```html
  </select><script>alert()</script>
  ```
- Note: The payload needs to break out of the select tag to execute arbitrary javascript.

## [DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-angularjs-expression)

- Inject the following payload into the search feild:
  ```java
  {{ 1 + 1 }}
  ```
- If 2 is printed to the screen inject the following payload:

```java
{{$on.constructor('alert()')()}}
```

## [Reflected DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected)

- Search for a random string.
- Look for other requests useing the same string in the parameter value.
- Check if the second request is returning JSON.
- Break out of the JSON object and inject javascript with the following payload:
  ```java
  \"-alert(1)}//
  ```
- Note: The backslash makes special charecotrs in JSON use their special functionality.
- The } ends the JSON object and // comments out the rest of the code.

## [Stored DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-stored)

- There is a critical bug in the javascript that loads comments into a post.
- The site only filters for the first special charector and ignores all other special charectors.
- You can bypass the filter by adding <> to the begging of a payload so only the first unused angle brackets are filtered.
- Inject the following payload into a comment field:

```html
<><img src='0' onerror='alert()'>
```

## [Reflected XSS into HTML context with most tags and attributes blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked)

- Try to inject a `<h1>` tag into the search value.
- If you get an error that the tag is not allowed it is being blocked by the WAF.
- Send the request to the intruder and fuzz for all tags from the XSS cheatsheet.
- Once you've found a tag that is allowed send the request to intruder and fuzz for events.
- You can use this final payload:
  ```

  ```

## [Reflected XSS into HTML context with all tags blocked except custom ones](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-all-standard-tags-blocked)

- Try to inject a `<h1>` tag into the search value.
- If you get an error that the tag is not allowed it is being blocked by the WAF.
- Send the request to the intruder and fuzz for all tags from the XSS cheatsheet.
- If all tags are blocked try to inject a custom one: `<cutstom-tag>`
- If custom tags are allowed try to inject an attribute that will execute the alert function.

## [Reflected XSS with some SVG markup allowed](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-some-svg-markup-allowed)


- [ ] Fuzz for allowed tags — confirm SVG-related tags work
- [ ] Fuzz for allowed events within SVG elements using cheatsheet

## [Reflected XSS in canonical link tag](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-canonical-link-tag)

- [ ] Confirm the URL parameter is reflected in a `<link rel="canonical" href="...">` tag
- [ ] Inject an `accesskey` + `onclick` attribute to hijack a keyboard shortcut:
```
'accesskey='x'onclick='alert(1)
```
> **Note:** Trigger with `Alt+Shift+X` (Windows/Linux) or `Ctrl+Alt+X` (macOS)


## [Reflected XSS into a JavaScript string with single quote and backslash escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped)

- [ ] Confirm single quotes and backslashes are escaped
- [ ] Break out at the `</script>` tag level instead — close the script block entirely:
```
</script><script>alert(1)</script>
```
> **Why it works:** The browser's HTML parser closes the script block before the JS parser runs, so escaping is irrelevant.


## [Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-double-quotes-encoded-single-quotes-escaped)

- [ ] Confirm angle brackets and double quotes are encoded; single quotes are escaped with `\`
- [ ] Use `\` to neutralize the injected backslash, then terminate the statement:
```
\';alert(1)//
```


## [Stored XSS into `onclick` event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-onclick-event-angle-brackets-double-quotes-html-encoded-single-quotes-backslash-escaped)

## [Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-template-literal-angle-brackets-single-double-quotes-backslash-backticks-escaped)

## [Exploiting cross-site scripting to steal cookies](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-stealing-cookies)

**Need burp collaborator**

## [Exploiting cross-site scripting to capture passwords](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-capturing-passwords)

**Need burp collaborator**

## [Exploiting XSS to bypass CSRF defenses](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-perform-csrf)


## [Reflected XSS protected by very strict CSP, with dangling markup attack](https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-very-strict-csp-with-dangling-markup-attack)

