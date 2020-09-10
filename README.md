# Manage your courses and generate hw and TODOs from markdown notes
* Generates daily TODOs based on your notes.
* Manages course directory structure based on weeks.

### Installation
``````````````
pip install python-dateutil
pip install markdown2
``````````````

### Create folder structure
```````````````
./create.sh
```````````````
(Shown here is a sample directory structure, modify your courses and term duration (no. of weeks) in create.sh)
This will give you a directory structure like the following:



## IMPORTANT:
- Notes format: must be a markdown file
- Second line must be "## <Date in any format>"
- have a "TODO:" to signify start of the todo or homework section in any notes.



## Generate Homework/TODOs from notes:
`````````````
./generate
`````````````
