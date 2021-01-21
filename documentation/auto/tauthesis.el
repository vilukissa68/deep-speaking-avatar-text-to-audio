(TeX-add-style-hook
 "tauthesis"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "12pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("pdfx" "a-1b" "mathxmp") ("inputenc" "utf8") ("helvet" "scaled=0.91") ("fontenc" "T1") ("titlesec" "explicit") ("babel" "\\@otherlanguage" "main=\\@mainlanguage") ("datetime2" "en-GB" "finnish") ("glossaries" "automake" "nonumberlist" "nopostdot")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "report"
    "rep12"
    "pdfx"
    "inputenc"
    "helvet"
    "fontenc"
    "fancyhdr"
    "titlesec"
    "setspace"
    "parskip"
    "babel"
    "csquotes"
    "xcolor"
    "datetime2"
    "graphicx"
    "listings"
    "glossaries"
    "titletoc"
    "enumitem")
   (TeX-add-symbols
    '("examiner" ["argument"] 1)
    '("preface" 2)
    '("otherabstract" 1)
    '("keywords" 2)
    '("programmename" 2)
    '("finishdate" 3)
    '("facultyname" 2)
    '("thesistype" 2)
    '("subtitle" 2)
    '("xselectlanguage" 1)
    "frontmatter"
    "mainmatter"
    "finalandcomma")
   (LaTeX-add-environments
    "appendices")
   (LaTeX-add-lengths
    "chapterspace")
   (LaTeX-add-xcolor-definecolors
    "taupurple"))
 :latex)

