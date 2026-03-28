## Recon

- Find attacker controlled values reflected in the HTML
    - Test payloads to identify the template engine
    - Find payload to execute code based on template engine
- Generate a tempalte engine error that identifies the type of template engine by modifying parameters to random values
    - Find payload to execute code based on template engine
- Find function to edit template
    - Generate error to find the template engine
    - Find payload based on template engine


## [Basic server-side template injection](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic)

- Test for attacker controlled values reflected in the HTML
- Fuzz the value with payloads to identify the template engine
- Once you know the template engine find a payload that can execute code
- Change the payload to delete the moral.txt file in Carlos home directory

## [Basic server-side template injection (code context)](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic-code-context)

- Check for a function to change preferred name and capture request in burp
- Modify the value to be a random string and make a comment. You should see and error indicating the template engine failed to parse the prefered username when creating the comment from a template. The error will contain the template engine.
- Once you know the template engine read the documentation and look for how expressions are placed inside the template and how to execute code via the template engine. 
- This lab uses Tornato (Python) and places the expressions inside two currly brackets `{{name.firstname}}`. You can use the os python library to inject code into the template engine.
- The following payload will inject code into the Tornato template engine:

```python
user.name}}{%25+import+os+%25}{{os.system('pwd')}}
```
- This will set the RCE payload as the prefered username and inject the code when a post is made via this user.

## [Server-side template injection using documentation](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-using-documentation)

- Check for a function to edit the template of a blog.
- Change the expression to be a random value and check for any error codes identifying what the template engine is.
- Once you find the template engine, read the documentation to find how to craft a payload that will execute code.
- There should be a payload that works in hacktricks or payloads all the things.

## [Server-side template injection in an unknown language with a documented exploit](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-in-an-unknown-language-with-a-documented-exploit)

- Look for attacker controlled values being reflected in the response
- Send the request to intruder and fuzz with payloads to identify the template engine.
- Look for verbose error messages that reveal the templating engine.
- Find a public exploit for the templating engine and change the command to delete the morale.txt file.

## [Server-side template injection with information disclosure via user-supplied objects](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-with-information-disclosure-via-user-supplied-objects)

- Check for a function to edit the template of a blog.
- Change one of the template expressions to something invalid, such as a fuzz string ${{<%[%'"}}%\
- Once you find the template engine, read the documentation to find how to craft a payload that will execute code.

- Use this payload to extract secret key from django template
{{settings.SECRET_KEY}}

#### Payloads to ID Template Engine
```
{{7*7}}
${7*7}
<%= 7*7 %>
${{7*7}}
#{7*7}
```

