from flask import render_template ,  request , redirect , url_for

import glob
import os
import json

user_data_path = "data/users.json"

user_data = json.load(open(user_data_path))


def user_registration(user) : 

    if request.method == 'POST' :

        hitori_xp = request.form.get('hitori_xp')
        puzzle_xp = request.form.get('puzzle_xp')
        z3_xp = request.form.get('z3_xp')

        print("USER. = " , user)
        return redirect(url_for('list_proofs', user=user))
    
    else : 

        return render_template("user_login.html")