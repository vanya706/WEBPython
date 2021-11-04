import cgi
import sys
import codecs
import os
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
cookie_value = cookie.get("count_f")
if cookie_value is None:
    print(f"Set-cookie: count_f={1}")
    count_forms = 1
else:
    count_forms = int(cookie_value.value) + 1
    print(f"Set-cookie: count_f={count_forms}")

print("Content-type: text/html\r\n")
print()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()

lastname = form.getfirst("lastname", "Not Entered")
firstname = form.getfirst("firstname", "Not Entered")
if form.getvalue('experience'):
    experience = form.getvalue('experience')
else:
    experience = "Not Entered"
programming_language = form.getlist('prog_language')
print("""
<!DOCTYPE HTML>
 <html>
 <head>
 <meta charset="utf-8">
 <title>Form Processing</title>
 </head>
 <body>
 """)
print(f"""
<div>
<b>Your Last Name:</b>{lastname}<br>
<b>Your First Name:</b>{firstname}<br>
<b>Your know this languages:</b>
""")
if len(programming_language) == 0:
    text = 'Not Entered'
else:
    text = ''
    for elem in programming_language:
        text += elem + ', '
    text = text[0:-2]
print(f"""
{text}<br>
<b>Your Work experience:</b>{experience}<br>
<b>Wow! Your fill so many form!: </b>{count_forms}
</div>
<br>
<div>
<a href='../index.html'>Go Back!</a>
</div>
</body>
</html>
""")
