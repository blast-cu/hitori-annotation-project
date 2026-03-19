from flask import Flask , render_template , request

from views.annotation import interact
from views.list_proofs import list_proofs
from views.user_login import user_login
from views.user_registration import user_registration

import os
import glob 
import json
import random

app = Flask(__name__)

app.add_url_rule('/' , view_func=user_login, methods=['GET' , 'POST'])
app.add_url_rule('/results/<user>/' , view_func=list_proofs)
app.add_url_rule('/register/<user>/' , view_func=user_registration, methods=['GET' , 'POST'])
app.add_url_rule('/interact/<user>/<run>/<stage>/<fname>/', view_func=interact, methods=['GET' , 'POST'])

if __name__ == "__main__" : 
    app.run(host='localhost' , port=8080, debug=True)