from flask import Flask, session

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.index
import controllers.client
import controllers.record
import controllers.days
import controllers.masters
import controllers.new_client
import controllers.cancel_record
import controllers.new_pet