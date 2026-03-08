from flask import render_template ,  request , redirect , url_for , flash
import json 
import random
import os
import markdown
import time

from views.rubric import *



base_generated_dir = 'data/generation/'
base_save_dir = 'data/annotation'


def find_adjacent_items(lst, target, adjacent_type='next'):
    index = lst.index(target)
    
    if adjacent_type == 'next':
        return lst[index + 1] if index < len(lst) - 1 else None
    
    elif adjacent_type == 'previous':
        return lst[index - 1] if index > 0 else None


def interact(user, run , stage , fname) :

    result_dir = os.path.join(base_generated_dir, run, stage)
    
    gen_files = sorted([f.replace('.json' , '') for f in os.listdir(result_dir)])
    save_dir = os.path.join(base_save_dir , run , stage)

    if not os.path.exists(save_dir) : os.makedirs(save_dir)

    if request.method == 'POST' : 

        next_file = find_adjacent_items(gen_files, fname, 'next')
        prev_file = find_adjacent_items(gen_files, fname, 'previous')

        #---- Create output path  ----#

        
        save_path = os.path.join(save_dir, user+'_'+fname+'.json')

        #---- Read the input ----#

        result_path = os.path.join(result_dir,  fname+'.json')
        results = json.load(open(result_path))
        # for result in results : result['puzzle_img'] = result.pop('puzzle-img')

        #---- Get the selection of inputs ----#

        idx = int(request.form.get('first_step'))
        sampled_result = results[idx:idx+5]

        #---- Prepare results for saving ----#

        print("request.form")
        print(request.form)

        save_dict = {} 
        save_dict['sample_steps'] = sampled_result
        save_dict['fname'] = fname+'.json'
        save_dict['stage'] = stage
        save_dict['run'] = run
        save_dict['user'] = user
        save_dict['notes'] = request.form.get('notes')
        save_dict['reject'] = request.form.get('reject')
        save_dict['correctness'] = request.form.get('corr')
        save_dict['understand'] = request.form.get('understand')
        save_dict['quality'] = request.form.getlist('quality')

        #---- Save results ----#

        with open(save_path, 'w') as f : 
            json.dump(save_dict , f , indent=4)

        #---- Move to the next puzzle----#

        if next_file : 

            return redirect(url_for('interact' , 
                            user=user,
                            run=run, 
                            stage=stage, 
                            fname=next_file))

        else : 

            return redirect(url_for('list_proofs', user=user,))

    
    next_file = find_adjacent_items(gen_files, fname, 'next')
    prev_file = find_adjacent_items(gen_files, fname, 'previous')

    #--- Read JSON file name ----# 

    result_path = os.path.join(result_dir, fname+'.json')
    results = json.load(open(result_path))
    print('result_path : ' , result_path)
    # for result in results : result['puzzle_img'] = result.pop('puzzle-img')


    #---- Create output path  ----#

    save_dir = os.path.join(base_save_dir , run , stage)
    get_save_path = os.path.join(save_dir, fname+'.json')


    #---- Register error if there is already an annotation with the save path ----#

    
    if os.path.exists(get_save_path) : 

        warning = f'WARNING: There already exists a file at {get_save_path}. \
            Please move it to a different location to not overwrite, and revisit this URL.'

    else : 
        warning = False
    
    #---- Indicate last sample from sampeld_result ----#

    results[0]['is_first'] = True
    results[-1]['is_last'] = True

    #---- convert markdown to html ----#

    for r in results : 
        r['answer'] = markdown.markdown(r['answer'])
        r['reasoning'] = markdown.markdown(r['reasoning'])
        if 'puzzle_img' in r : 
            r['puzzle_img'] = r.pop('puzzle_img') # correct way
        else :  
            r['puzzle_img'] = r.pop('puzzle-img') # old, incorrect way

        grid = r['grid']
        all_shaded = r['all_shaded_cells']
        all_unshaded = r['all_unshaded_cells']

        #---- unshade target cell -----#

        row , col = r['target'].split('c')
        row = int(row.replace('r' , ''))-1
        col = int(col)-1

        all_shaded[row][col] = False
        all_unshaded[row][col] = False


    #---- unshade all cells if unstaged -----#

    if stage.lower() in ['unstaged' , 'typeu'] : 
        all_shaded = [[False]*len(all_shaded[0])]*len(all_shaded)
        all_unshaded = [[False]*len(all_unshaded[0])]*len(all_unshaded)


    #---- Make context ----#

    context = {
                'sampled_result' : results,
                'curr_file' : fname,
                'next_file' : next_file, 
                'prev_file' : prev_file,
                'first_step_index' : 0, 
                'warning' : warning,
                'run' : run,
                'stage' : stage,
                'target_row' : row,
                'target_col' : col,
                'rubrics' : rubrics,
                'rubric_dimensions' : rubric_dimensions,
                'quality_rubrics' : quality_rubrics,
                'quality_rubric_dimensions' : quality_rubric_dimensions,
                'understand_rubrics' : understand_rubrics,
                'understand_rubric_dimensions' : understand_rubric_dimensions,
                'user':  user,
                'grid' : grid,
                'all_shaded' : all_shaded,
                'all_unshaded' : all_unshaded,

            } 

    return render_template('interactive.html', **context )