from flask import render_template ,  request , redirect , url_for

import glob
import os
import json

src_dir = "data/generation/"
user_data_path = 'data/users.json'
user_data = json.load(open(user_data_path))

print("In login screen; this is what user_data looks like...")
print(user_data)

def user_login() : 

    if request.method == 'POST' :
        user = request.form.get('username').strip()

        if user in user_data : 
            print("KNOWN USER. INFO :  " , user_data[user])
            return redirect(url_for('list_proofs', user=user))
        
        else : 
            return redirect(url_for('user_registration', user=user))
        
    return render_template("user_login.html")