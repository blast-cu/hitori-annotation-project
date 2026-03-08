from flask import render_template 
import glob
import os

def list_proofs(user) : 

    src_dir = "data/generation/"
    experiment_versions = ['annotate' , 'training']

    print(experiment_versions)
    
    if not experiment_versions : 
        experiment_versions = os.listdir(src_dir)

    run2results = {}
    for run in experiment_versions : 
        stages = os.listdir(os.path.join(src_dir , run))
        for stage in stages : 
            fnames = os.listdir(os.path.join(src_dir , run, stage))
            first_file = sorted([f.replace('.json' , '') for f in fnames ])[0]

            if run in run2results : 
                run2results[run].append({'stage':stage, 'first_file':first_file})
            else : 
                run2results[run] = [{'stage':stage, 'first_file':first_file}]

    context = {'run2results' : run2results , 'user' : user}

    return render_template('list_generation.html' , **context)

    
