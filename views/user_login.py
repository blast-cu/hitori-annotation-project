from flask import render_template ,  request , redirect , url_for

from flask import render_template 
import glob
import os

src_dir = "data/generation/"
experiment_versions = []

def user_login() : 

    if request.method == 'POST' :
        print(request.form)
        user = request.form.get('username')
        print("USER. = " , user)
        return redirect(url_for('list_proofs', user=user))

    return render_template("user_login.html")