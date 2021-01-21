(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("tauthesis" "english")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "tex/johdanto"
    "tex/esitystyyli"
    "tex/viittaustekniikat"
    "tex/yhteenveto"
    "./tex/liite"
    "tauthesis"
    "tauthesis10"
    "amsmath"
    "amssymb"
    "amsthm")
   (TeX-add-symbols
    '("verbcommand" 1))
   (LaTeX-add-labels
    "ch:johdanto"
    "ch:esitystyyli"
    "ch:viittaustekniikat"
    "ch:yhteenveto"
    "ch:liite")
   (LaTeX-add-bibliographies
    "tex/references"))
 :latex)

