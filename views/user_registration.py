from flask import render_template ,  request , redirect , url_for

import glob
import os
import json

data_path = 'data/generation'

user_data_path = "data/users.json"
user_data = json.load(open(user_data_path))

assigned_task_sets_path = 'data/task_set_assignment.json'
assigned_task_sets = json.load(open(assigned_task_sets_path))

print("At LOAD: assigned_task_sets")
print(assigned_task_sets)

# Update any new task sets 
print("Updating assigned task sets with new tasks....")
for task_set in os.listdir(data_path) : 
    if (task_set != 'training') and (task_set not in assigned_task_sets) : 
        assigned_task_sets[task_set] = []

def write_assign_task_set() : 
    with open(assigned_task_sets_path , 'w') as f : 
        json.dump(assigned_task_sets , f , indent=4)

    print("Updated Assigned Tasks...")

def write_user_data() : 

    with open(user_data_path , 'w') as f : 
        json.dump(user_data , f , indent=4)


def user_registration(user) : 
    print("AFTER LOAD: assigned_task_sets")
    print(assigned_task_sets)

    if request.method == 'POST' :

        if (user in user_data) :  
            print(f"Found {user} in {user_data}.")
            if ('assigned_task_set' in user_data[user] ) : 
                print(f"Found assigned task set {user_data[user]['assigned_task_set']} for {user}")
                return redirect(url_for('list_proofs', user=user))


        print(f"Did not find {user} in {user_data}.")
        print("Registering User...")
    
        hitori_xp = request.form.get('hitori_xp')
        puzzle_xp = request.form.get('puzzle_xp')
        z3_xp = request.form.get('z3_xp')

        user_data[user] = {
                        'hitori_xp' : hitori_xp, 
                        'puzzle_xp' : puzzle_xp,
                        'z3_xp' : z3_xp
                        }
        
        print(f"user_data after registering user : {user_data}")
        
        task_set_to_assign = [] 
        print('assigned_task_sets before assigning the user a task...')
        print(assigned_task_sets)


        # Check if there is any task with only one annotator
        for task_set , users in assigned_task_sets.items() : 

            if len(users) == 1 : 
                print(task_set , users)
                task_set_to_assign = task_set 
                users.append(user)
                assigned_task_sets[task_set] = users
                user_data[user]['assigned_task_set'] = task_set_to_assign
                write_assign_task_set()
                break 
        
        # If there is no task with only one annotator, find a task 
        # with 0 anntoators. 
        if task_set_to_assign == [] : 
            print("Task set to asign is none...")
            for task_set , users in assigned_task_sets.items() : 

                print(f"task_set = {task_set } | users  = {users}")

                if len(users) == 0 : 
                    print(f"len(users) = 0 check has passed. ")
                    task_set_to_assign = task_set 
                    users.append(user)
                    assigned_task_sets[task_set] = users
                    print("After assigning tasks and everything...")
                    print(assigned_task_sets)
                    break
        
        # If there are no tasks remaining that have less than 2 annotators 
        # no way to handle for now
        if task_set_to_assign == [] : 
            return "All the annotation jobs have been completed! Stay tuned for more"
        
        print("Checking state of user_data and task_sets before writing.")
        user_data[user]['assigned_task_set'] = task_set_to_assign
        print(user_data)
        print(assigned_task_sets)
        write_assign_task_set()
        write_user_data()
                        
        return redirect(url_for('list_proofs', user=user))
    
    else : 

        return render_template("user_registration.html" , user=user)