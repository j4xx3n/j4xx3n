# How to Enumerate Endpoints

Katana
```bash
katana -list subs.txt | anew urls.txt
```

GAU
```bash
getallurls 
```

Wayback Machine
```bash
cat subs.txt | while read url; do curl 'https://web.archive.org/cdx/search/cdx?url=*.$url/*&output=text&fl=original&collapse=urlkey' | anew urls.txt; done
```

