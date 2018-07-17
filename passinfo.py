import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
trackNumber = form.getvalue('inputTracking')
print trackNumber