#!/usr/bin/env python3
from subprocess import call
from uuid import uuid4

from flask import Flask
from flask import request
from flask import send_from_directory

# Import from the 21 Bitcoin Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Charge a fixed fee of 1000 satoshis per request to the
# /snap endpoint
@app.route('/snap')
@payment.required(1000)
def snap():
    file = str(uuid4()) + '.jpeg'

    call(['streamer', '-f', 'jpeg', '-o', '/tmp/' + file])

    return send_from_directory(
      '/tmp',
      file,
      as_attachment=True
    )

# Initialize and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')