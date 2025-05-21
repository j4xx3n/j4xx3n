# How to Hunt for Hidden Parameters

Arjun
```bash
cat urls.txt | grep '?' | cut -d '?' -f 1 | sort -u > baseurls.txt

cat baseurls.txt | while read url; do arjun -u $url -m post; done
cat baseurls.txt | while read url; do arjun -u $url -m get; done
```
Fuzzing Parameters with Common Wordlist
```bash
cat subs.txt | while read $url; do python ParamHunter.py -u https://$url -w commonParams.txt -a -j; done
```


Fuzzing Parameters with Custom Wordlist
```bash
cat urls.txt | unfurl keys | anew customParams.txt

cat urls.txt | cewl | anew customParams.txt

cat subs.txt | while read $url; do python ParamHunter.py -u https://$url -w customParams.txt -a -j; done
```
