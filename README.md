# Manage Courses
-  Manage your courses and generate hw and TODOs from markdown notes
* Generates daily TODOs based on your notes.
* Manages course directory structure based on weeks.

### Installation
``````````````
git clone https://github.com/harrysandhu/manage-courses.git
pip install python-dateutil
pip install markdown2
``````````````

### Create folder structure
```````````````
./create.sh
```````````````
(Shown here is a sample directory structure, modify your courses and term duration (no. of weeks) in create.sh)
This will give you a directory structure like the following:
<img src="https://raw.githubusercontent.com/harrysandhu/manage-courses/master/dir.png" />

## IMPORTANT:
- Notes format: must be a markdown file
- Second line must be "## <Date in any format>"
- have a "TODO:" to signify start of the todo or homework section in any notes.



## Generate Homework/TODOs from notes:
`````````````
./generate.py 1
`````````````

## Example hw file

# 2020-09-08
## algo-COMP3760:
- TODO: 
#### lecture
    - nested loop - summation translation
    - writing psuedocode
    - kleinberg chapter 2

#### lab
    - CLRS AVL trees
    - CLRS Hashtables revise
    - Assignment 4 

---------------------------
## pstat-MATH3042:
- TODO:
#### lecture
    - Buy the book
    - Read Chapter 1
    - Submit the lab assignment
    
---------------------------
