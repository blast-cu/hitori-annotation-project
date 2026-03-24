
rubrics = [

    {
        'name' : 'Factual Accuracy: Does the explanation correctly apply Hitori rules without missing anything? ',
        'definition' : '<br><em>Errors may include mistakes in indentifying uniqueness, shading logic, adjacency constraints, or connectivity.<br>Gaps include skipping steps or missing important information.</em>', 
        'shortname': 'corr'
    } , 

]


rubric_dimensions = [

    {
        'name' : ' 👍 <b>No errors and no gaps.</b>' , 
        'value' : 3
    } , 

    {
        'name' : '👎 <b>Minor errors or minor gaps: </b> Small mistakes that don\'t invalidate the overall reasoning or small gaps in explanation that can easily be inferred.' , 
        'value' : 2
    } , 

    
    {
        'name' : '❌ <b>Major Errors or Major Gaps: </b> Catastrophic mistakes that make the reasoning wrong or misleading, or significant gaps that cannot be be overcome.' , 
        'value' : 1
    } , 
]

understand_rubrics = [

    {
        'name' : 'Clarity After reading the explanation, do you understand why this step was taken?',
        'definition' : '<br><em>Does the step\'s outcome become clear by following the explanation?</em>', 
        'shortname': 'understand'
    } 

]

understand_rubric_dimensions = [

    {
        'name' : '😊 <b>Completely clear — </b>I can follow the reasoning and understand the outcome! ' , 
        'value' : 3
    } , 

    {
        'name' : '🤨 <b>Somewhat clear — </b>I get the general idea but parts are confusing or vague.' , 
        'value' : 2
    } , 

    
    {
        'name' : '😭 <b>Not clear — </b>I cannot follow what the explanation is trying to say.' , 
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