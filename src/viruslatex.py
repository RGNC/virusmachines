import os.path
import re
filesdir = 'genlatex/'

def viruslatex(vm, vertical_hosts = 2, horizontal_hosts = 2, filename = '', verbose=False):
    beg_code = \
        r'''\documentclass{standalone}

\usepackage{ifthen}
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta}

\tikzset {
  host/.style n args = {2}{
    draw,rectangle,
    minimum width=2cm,
    minimum height=1cm,
    rounded corners=2mm,
    name=#1,
    label={south east:#2}
  },
  instruction/.style n args = {2}{
    draw=cyan,fill=cyan,circle,
    minimum width=1cm,
    minimum height=1cm,
    name=#1,
    label={south east:{\color{cyan} #2}}
  },
  env/.style = {},
  hostconn/.style = {
    -{Latex[open]},double,
    font=\footnotesize
  },
  instconn/.style = {
    -Latex,
    font=\footnotesize
  },
  loop/.style = {
    -Latex,
    looseness=10
  },
  insthost/.style = {
    draw=red,dashed,thick
  }
}

\newcommand{\host}[4]{\node[host={h#1}{$h_{#1}$}] at (#2,#3) {#4};}
\newcommand{\instruction}[3]{\node[instruction={i#1}{$i_{#1}$}] at (#2,#3)
  {};}
\newcommand{\env}[2]{\node[env] (henv) at (#1,#2) {};}
\newcommand{\hostconn}[5][0]{\draw[hostconn] (h#4) to [bend right=#1] node[#3] (h#4h#5) {#2} (h#5);}
\newcommand{\instconn}[5][0]{%
  \ifthenelse{\equal{#4}{#5}}%
  {\draw[instconn] (i#4) edge [loop #3] node {#2} (i#5);}% Caso loop
  {\draw[instconn] (i#4) to [bend left=#1] node[#3] {#2} (i#5);}% Caso normal
}
\newcommand{\insthost}[3][0]{%
  \draw[insthost] (#2) to [bend left=#1] (#3);%
}
\newcommand{\legend}[5]{%
  \node at (#1,#2) {$#3$ activates $#4 \rightarrow #5$};%
}

\begin{document}
'''
    mid_code = vm.generate_LaTeX(vertical_hosts, horizontal_hosts, verbose)

    end_code = r'''\end{document}'''

    if filename:
        number = 0
        fn = filesdir + filesname
        if filename.endswith('.tex'):
            fn = fn[:-4]
        if os.path.isfile(fn):
            fn += '-0'
        while os.path.isfile(fn):
            number += 1
            fn = re.match('(.*)-(.*?)', fn).group(1) + '-' + str(number)
        f = open(fn + '.tex', 'w')
        f.write(beg_code)
        f.write(mid_code)
        f.write(end_code)
        f.close()
    else:
        print(mid_code)
