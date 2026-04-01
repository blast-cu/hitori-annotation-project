from flask import render_template 
import glob
import os
import json

def list_proofs(user) : 

    src_dir = "data/generation/"
    user_data = json.load(open('data/users.json'))
    experiment_versions = ['training' , user_data[user]['assigned_task_set']] + [os.path.basename(dir) for dir in glob.glob('data/generation/*gemini2.5')]

    print(experiment_versions)
    
    if not experiment_versions : 
        experiment_versions = sorted(os.listdir(src_dir))

    run2results = {}
    for run in experiment_versions : 
        stages = sorted(os.listdir(os.path.join(src_dir , run)))
        for stage in stages : 
            fnames = os.listdir(os.path.join(src_dir , run, stage))
            first_file = sorted([f.replace('.json' , '') for f in fnames ])[0]

            if run in run2results : 
                run2results[run].append({'stage':stage, 'first_file':first_file})
            else : 
                run2results[run] = [{'stage':stage, 'first_file':first_file}]

    context = {'run2results' : run2results , 'user' : user}

    return render_template('list_generation.html' , **context)

    
