# Hitori Annotation Pilot 

## Overview 

Hitori is a Japanese puzzle game, much like Sudoku. 
There are a set of rules in order to "solve" the puzzle, and the solution is NP-hard complexity. 

Needless to say, LLMs can't solve the puzzle by itself. 

A group of researchers and I came up with a neurosymbolic method to solve the puzzle. 
The method ties in the rigor of symbolic solvers with the experessivity of neural methods, allowing to come up with terse solutions that are still understandable to humans. 

We want to do a human evaluation to measure the usefulness of the solution. 

## Where you come in

Prior to doing a full-scale annotation evaluation, we want to pilot the solution in this lab meeting to get feedback on the annotation tool itself. 

Today, **you will**

1. be taught how Hitori works 
2. will learn to use the tool 
3. will conduct annotation on a small number of steps

We hope to get:

1. Preliminary results from your annotation. 
2. Feedback on the user experience when using the annotation. 
3. Feedback on the training session. 

## Schedule Overview 

- 10:30-10:35 Setup and Overview of annotation tool 
- 10:35-10:50 Explanation of Hitori Rules
- 10:50-11:00 Exploring Rubric through some select examples

## Start by: 

1. Cloning `hitori-annotation-project` from the BLAST repository. 
2. Install dependencies with `pip install -r requirements.txt` 
3. Run the app with `python -m app`