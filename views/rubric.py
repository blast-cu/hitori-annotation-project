
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
        'name' : '👎 <b>Insignificant Errors: </b> A few errors, that can be overcome easily.' , 
        'value' : 3
    } , 

    
    {
        'name' : '❌<b>Catastrophic Errors: </b> Errors that affect the overall explanation of the puzzle.' , 
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
        'name' : '😊 Understand Completely! ' , 
        'value' : 5
    } , 

    {
        'name' : '🤨 Understand Somewhat.' , 
        'value' : 3
    } , 

    
    {
        'name' : '😭 Did not understand.' , 
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
        'name' : 'Hallucination' , 
        'value' : 0
    } ,


]