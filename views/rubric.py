
rubrics = [

    {
        'name' : 'Is this explanation factual?',
        'definition' : '<br><em>If not factual, please use the notes to describe the error.</em>', 
        'shortname': 'corr'
    } , 

]


rubric_dimensions = [

    {
        'name' : 'No Errors 👍' , 
        'value' : 5
    } , 

    {
        'name' : '1-2 Small Errors 👎' , 
        'value' : 3
    } , 

    
    {
        'name' : 'Too Erroneous ❌' , 
        'value' : 1
    } , 
]

understand_rubrics = [

    {
        'name' : 'Did you understand the explanation?',
        'definition' : '', 
        'shortname': 'understand'
    } 

]

understand_rubric_dimensions = [

    {
        'name' : 'Understand Completely! 😊' , 
        'value' : 5
    } , 

    {
        'name' : 'Understand Somewhat. 🤨' , 
        'value' : 3
    } , 

    
    {
        'name' : 'Did not understand 😭' , 
        'value' : 1
    } , 


]

quality_rubrics = [

    {
        'name' : 'Quality Assurance.',
        'definition' : '', 
        'shortname': 'quality'
    } 
    
]


quality_rubric_dimensions = [

    {
        'name' : 'Repetition' , 
        'value' : 5
    } , 

    {
        'name' : 'Verbose' , 
        'value' : 3
    } , 

    
    {
        'name' : 'Proof Artifacts' , 
        'value' : 1
    } , 


]