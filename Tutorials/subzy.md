# How to Hunt for Subdomain Takovers

Method 1: Subzy
```bash
echo example.com | subfinder | httpx-toolkit > subs.txt

subzy run --targets subs.txt --hide_fails
```

Method 2: MassDNS
```bash
echo example.com | subfinder | httpx-toolkit > subs.txt

massdns -r resolvers.txt -t A -o S -w resolved.txt subs.txt

cat resolved.txt | grep -Ei 'CNAME|NXDOMAIN|SERVFAIL' > suspicious.txt

grep -Ei 'animaapp\.io|bitbucket\.io|trydiscourse\.com|hatenablog\.com|helpjuice\.com|helpscoutdocs\.com|helprace\.com|s\.strikinglydns\.com|na-west1\.surge\.sh|surveysparrow\.com|read\.uberflip\.com|wordpress\.com|worksites\.net'
```


## Resolvers List
129.250.35.251
208.67.222.222
208.67.220.222
1.0.0.1
8.8.4.4
8.8.8.8 
