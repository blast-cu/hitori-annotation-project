
rubrics = [

    {
        'name' : 'Is this explanation factual?',
        'definition' : '<br><em>If not factual, please use the notes to describe the error.</em>', 
        'shortname': 'corr'
    } , 

]


rubric_dimensions = [

    {
        'name' : ' 👍 <b>No Errors</b>' , 
        'value' : 5
    } , 

    {
        'name' : '👎 <b>Minor Errors: </b> Small errors that can be ignored and don\'t affect the whole explanation.' , 
        'value' : 3
    } , 

    
    {
        'name' : '❌<b>Major Errors: </b> Significant errors that can\'t be overcome, and affect the overall explanation of the puzzle.' , 
        'value' : 1
    } , 
]

understand_rubrics = [

    {
        'name' : 'Does explanation provided help you understand the step?',
        'definition' : 'Does the step\'s outcome become clear by following the explanation?', 
        'shortname': 'understand'
    } 

]

understand_rubric_dimensions = [

    {
        'name' : '😊 Helps understand Completely! ' , 
        'value' : 5
    } , 

    {
        'name' : '🤨 Helps understand somewhat.' , 
        'value' : 3
    } , 

    
    {
        'name' : '😭 Did not help at all.' , 
        'value' : 1
    } , 


]

quality_rubrics = [

    {
        'name' : 'Quality Assurance',
        'definition' : '<br> <em>Did you find occurances of the following in the proof?</em>', 
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

    {
        'name' : 'Explanation has nothing to do with puzzle.' , 
        'value' : 0
    } ,


]