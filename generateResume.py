import json
import subprocess

#### Header ####
def Header(data):
    return r'''%%!TEX program = lualatex

\documentclass[]{mcdowellcv}

\usepackage{amsmath}
\usepackage{multicol}

\name{%s}
\address{%s \linebreak %s \linebreak %s}
\contacts{\href{%s}{%s} \linebreak \href{%s}{%s} \linebreak \href{%s}{%s}}

\begin{document}

\makeheader
''' % (data["name"], data["email"], data["phone"], data["location"], data["linkedin"], data["linkedin"].split("www.")[1], data["github"], data["github"].split("www.")[1], data["website"], data["website"].split("https://")[1])

#### Education ####
def Education(data):
    resumeStr = r'''
\begin{cvsection}{Education}
'''
    for education in data["Education"]:
        resumeStr += r'''
    \begin{cvsubsection}{\mbox {%s}}{}{%s -- %s}
        %s in %s - GPA: %s
    \end{cvsubsection}
    ''' % (education["university"], education["from"], education["to"], education["degree"], education["major"], education["gpa"])
    resumeStr += r''' 
\end{cvsection}
'''
    return resumeStr

#### Experience ####
def Experience(data, type):
    resumeStr = r'''
\begin{cvsection}{Experience}
''' 
    for experience in data["Experience"]:
        if type in experience["tags"]:
            resumeStr += r'''
    \begin{cvsubsection}{%s}{%s}{%s -- %s}
        %s
        \vspace{2.5mm}
        \begin{itemize}
    ''' % (experience["title"], experience["company"], experience["from"], experience["to"], experience["location"])

            for desc in experience["description"]:
                resumeStr += r'''        \item %s
    ''' % desc

            resumeStr += r'''    \end{itemize}
    \end{cvsubsection}
    '''
    resumeStr += r'''
\end{cvsection}
'''
    return resumeStr

#### Projects ####
def Projects(data, type):
    resumeStr = r'''
\begin{cvsection}{Projects}
'''
    for project in data["Projects"]:
        if type in project["tags"]:
            resumeStr += r'''
    \begin{cvsubsection}{}{}{}
        \begin{itemize}
            \setlength\itemsep{3pt}
            \item\textbf{\href{%s}{%s}} \\
            %s
        \end{itemize}
    \end{cvsubsection}
    ''' % (project["link"], project["title"], project["description"])

    resumeStr += r'''
\end{cvsection}
'''
    return resumeStr

#### Skills ####
def Skills(data, type):
    resumeStr = r'''
\begin{cvsection}{Skills}
    \begin{cvsubsection}{}{}{}
        \begin{itemize}
            \item \textbf{Programming Languages:} %s
            \item \textbf{Software:} %s
            \item \textbf{Technologies:} %s
        \end{itemize}
    \end{cvsubsection}
\end{cvsection}
''' % (", ".join(data["Skills"]["ProgrammingLanguages"]), ", ".join(data["Skills"]["Software"][type]), ", ".join(data["Skills"]["Technologies"][type]))
    return resumeStr

#### End ####
def Footer():
    return r'''
\end{document}'''

# Change the order of the sections to change the order of the resume
def generateResume(data, type):
    return Experience(data, type) + Projects(data, type) + Skills(data, type) + Education(data)

def main():
    with open("configs/data.json", "r") as file:
        data = json.load(file)

    for type in data['Tags']:
        filepath = "TexFiles/"+ type.capitalize() + "Resume.tex"
        with open(filepath, "w") as file:
            file.write(Header(data) + generateResume(data, type.lower()) + Footer())

        # Compile into PDF
        subprocess.run(["lualatex", "-output-directory=PDFs", "TexFiles/{}Resume.tex".format(type.capitalize())])

    # Clean directory of auxiliary files
    for ext in ["aux", "log", "out"]:
        subprocess.call("rm PDFs/*."+ext, shell=True)

if __name__ == "__main__":
    main()
