import json
import os

def generate_latex_resume(data, type):

###### Header ######
    
    latex_resume = r'''
%%!TEX program = lualatex

\documentclass[]{../mcdowellcv}

\usepackage{amsmath}
\usepackage{multicol}

\name{%s}
\address{%s \linebreak %s \linebreak %s}
\contacts{\href{%s}{%s} \linebreak \href{%s}{%s} \linebreak \href{%s}{%s}}

\begin{document}

\makeheader
''' % (data["name"], data["email"], data["phone"], data["location"], data["linkedin"], data["linkedin"].split("www.")[1], data["github"], data["github"].split("www.")[1], data["website"], data["website"].split("https://")[1])

###### Education ######

    latex_resume += r'''
\begin{cvsection}{Education}
'''
    for education in data["Education"]:
        latex_resume += r'''
    \begin{cvsubsection}{\mbox {%s}}{}{%s -- %s}
        %s in %s - GPA: %s
    \end{cvsubsection}
    ''' % (education["university"], education["from"], education["to"], education["degree"], education["major"], education["gpa"])

###### Experience ######

    latex_resume += r'''
\end{cvsection}

\begin{cvsection}{Experience}
''' 

    for experience in data["Experience"]:
        if type in experience["tags"]:
            latex_resume += r'''
        \begin{cvsubsection}{%s}{%s}{%s -- %s}
            %s
            \vspace{2.5mm}
            \begin{itemize}
    ''' % (experience["title"], experience["company"], experience["from"], experience["to"], experience["location"])

            for desc in experience["description"]:
                latex_resume += r'''            \item %s
    ''' % desc

        latex_resume += r'''        \end{itemize}
    \end{cvsubsection}
'''

###### Projects ######

    latex_resume += r'''
\end{cvsection}

\begin{cvsection}{Selected Projects}
'''

    for project in data["Projects"]:
        if type in project["tags"]:
            latex_resume += r'''
        \begin{cvsubsection}{}{}{}
            \begin{itemize}
                \setlength\itemsep{3pt}
                \item\textbf{\href{%s}{%s}} \\
                %s
            \end{itemize}
        \end{cvsubsection}
    ''' % (project["link"], project["title"], project["description"])
            
###### Skills ######

    latex_resume += r'''
\end{cvsection}

\begin{cvsection}{Skills}
'''

    latex_resume += r'''
    \begin{cvsubsection}{}{}{}
        \begin{itemize}
            \item \textbf{Programming Languages:} %s
            \item \textbf{Software:} %s
            \item \textbf{Technologies:} %s
        \end{itemize}
    \end{cvsubsection}
''' % (", ".join(data["Skills"]["ProgrammingLanguages"]), ", ".join(data["Skills"]["Software"][type]), ", ".join(data["Skills"]["Technologies"][type]))

    latex_resume += r'''
\end{cvsection}

\end{document}
'''
    return latex_resume

###### FUNCTION END ######

def main():
    with open("configs/data.json", "r") as file:
        data = json.load(file)

    types = data['Tags']
    
    for type in types:
        latex_resume = generate_latex_resume(data, type.lower())
        filepath = "GeneratedTexFiles/"+ type.capitalize() + "Resume.tex"
        with open(filepath, "w") as file:
            file.write(latex_resume)
        os.system("lualatex -interaction=nonstopmode -output-directory=GeneratedPDFs " + filepath)
        os.system("del GeneratedPDFs\*.log GeneratedPDFs\*.aux GeneratedPDFs\*.out")

if __name__ == "__main__":
    main()
