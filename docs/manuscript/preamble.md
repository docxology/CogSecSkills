# LaTeX Preamble

This file contains project-local LaTeX additions consumed by the template renderer.
The manuscript uses narrow margins and compact long-table spacing because the
generated supplements include a full 100-skill catalogue and metadata matrices.

```latex
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{geometry}
\geometry{margin=0.55in}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{hyperref}
\usepackage[capitalise,noabbrev]{cleveref}
\usepackage{natbib}
\setlength{\LTpre}{6pt}
\setlength{\LTpost}{6pt}
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.08}
```
