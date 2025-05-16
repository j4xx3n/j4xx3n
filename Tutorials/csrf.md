# How to Hunt for CSRF Vulnerabilities

1. Scan subdomains with xsrfprobe
```bash
xsrfprobe -u example.com --crawl --malicious -o xsrfprobe.txt

cat subs.txt | while read sub; do xsrfprobe -u example.com --crawl --malicious | tee -a xsrfprobe.txt; done
```

2. Check for sign up functionality on the subdomains that are potentially vulnerable to CSRF. Create a list.
3. Sign up for all subdomains and look for any forms.
4. Capter the request for the form and create a POC with CSRF Shark.
5. Validate that the POC can change the account settings. On a new account if possible.
