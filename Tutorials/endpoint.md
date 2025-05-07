# How to Enumerate Endpoints

Katana
```bash
katana -list subs.txt | anew urls.txt
```

Wayback Machine
```bash
cat subs.txt | while read url; do curl 'https://web.archive.org/cdx/search/cdx?url=*.$url/*&output=text&fl=original&collapse=urlkey' | anew urls.txt; done
```




Arjun
```bash
cat baseurls.txt | while read url; do arjun -u $url -m post; done

cat baseurls.txt | while read url; do arjun -u $url -m get; done
```
