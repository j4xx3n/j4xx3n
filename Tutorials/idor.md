# How to Hunt for IDORs

1. Run the following commands to find signup pages and create a file to store usernames and passwords for each site.

```bash
echo 'example.com' | subfinder -o subs.txt

echo subs.txt | httpx-toolkit | katana -o urls.txt

echo urls.txt | grep -iE 'sign[-_]?up|register|create[-_]?account|join[-_]?now' | sort -u > signup.txt

echo signup.txt | while read url; do echo $url && echo 'UN:' && echo 'PW' > IDOR.txt; done

nano IDOR.txt
```

2. Go through each site and do the following:

a. Create an account and add info to the IDOR.txt sheet.
b. Find the following mechanisums and any more and create a list or the urls.

`Common Features Vulnerable to IDOR`
1. User Profile Access

- GET /user/12345

- GET /profile?user_id=12345

  Often gives away personal data or allows editing someone else's profile.

2. File Downloads or Uploads

- GET /files/receipt_6789.pdf

- POST /upload?userid=123

Could expose confidential documents or allow overwriting others' files.

3. Order Details / Invoices

- GET /order/9999

- GET /invoice?invoice_id=4567

May let you view others' purchases, invoices, or payment info.

4. Tickets / Support Requests

- GET /support/ticket/1234

- GET /helpdesk/view?id=9876

Access or respond to someone else’s support issue.

5. Messaging Systems

- GET /message/1122

- GET /chat/thread?id=abcd

Read other users’ private messages.

6. Password Reset / Email Verification Tokens

- GET /reset-password?token=abc123

Often not directly IDOR but may combine with predictable tokens for exploitation.

7. Project / Task Management Systems

- GET /task?id=33

- GET /project/88/overview

Access or manipulate unauthorized tasks or project data.

8. APIs with predictable or enumerable IDs

- GET /api/v1/users/101

- GET /api/v1/posts?user=222

RESTful APIs often lack proper access control at the object level.

9. Booking Systems / Appointments

- GET /appointments/1500

- GET /booking?id=2001

View or cancel others’ appointments.

10. Admin or Staff-Only Actions

- POST /user/delete?id=4321

- POST /permissions/change?user=1001&role=admin

Privilege escalation via IDOR to perform unauthorized actions.


c. Capture the request for each of these features and remove all headers and parameters that are not needed to receive a 200 status code.

d. Look for numeric IDs, UUIDs, or usernames used for authentication.

3. If you find encoded or encrypted values search the response bodys for that value to try to find the request that generated the value. 

4. If the authentication value is encoded run it through hash-identifier and try to brute force with iteratable numbers or use a rianbow table.

5. If the authentication value is a UUID v1 execute a sandwich attack.
