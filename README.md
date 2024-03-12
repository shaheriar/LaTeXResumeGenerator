# LaTeX Resume Generator
LuaLaTeX Resume Generator using Python and LuaLatex, using the McDowell CV class.

## Requirements
- Python
- LuaLaTeX

## Usage
- Edit the JSON file in configs/data.json.
- The tags are the different kinds of resumes you want to make.
- The tags in the different subsections are what resumes you want that information to be included in. For example, if you have a project that seems good for both a Data Science and Software Engineering resume, you can add ['ds', 'swe'] to the tags, or however you want to customize it.
- Run the Python script `generateResume.py`.
- The generated TeX files are in GeneratedTexFiles and the generated PDFs are in GeneratedPDFs.

## Notes
- Currently, the python script is catered towards my tech resume but you can edit it however you want.
- The OS commands at the bottom of the script are for Linux but you can edit it for your own OS.
- If you dont have LaTeX installed on your system, simply upload the `mcdowellcv.cls` file along with the generated .tex file to Overleaf and it will compile the PDF for you.
