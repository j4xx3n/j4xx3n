# How to Enumerate Web Archive History

Single Domain
```bash
curl 'https://web.archive.org/cdx/search/cdx?url=*.target.com/*&output=text&fl=original&collapse=urlkey' > wayback.txt
```

List of Domains
```bash
cat domains.txt | while read url; do curl 'https://web.archive.org/cdx/search/cdx?url=*.$url/*&output=text&fl=original&collapse=urlkey' >> wayback.txt; done
```
