# How to Hunt for XSS

```bash
cat urls.txt | gf xss | urldedupe | sed 's/=.*/=/' | sort -u > xss.txt

cat xss.txt | kxss | grep "\" ' < >" > tee kxss.txt

cat kxss.txt | while read url; do dalfox url $url; done
```
