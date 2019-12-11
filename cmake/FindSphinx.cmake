### UseSphinx.cmake ---
##
## Filename: UseSphinx.cmake
## Author: Fred Qi
## Created: 2014-09-03 21:57:10(+0400)
##
## Last-Updated: 2015-07-01 19:20:51(+0300) [by Fred Qi]
##     Update #: 32
######################################################################
##
### Commentary:
##
##
######################################################################
##
### Change Log:
##
##
######################################################################

find_program(SPHINX_BUILD sphinx-build)
if(SPHINX_BUILD)
  execute_process(COMMAND "${SPHINX_BUILD}" "--version"
	OUTPUT_VARIABLE SPHINX_OUTPUT
	OUTPUT_STRIP_TRAILING_WHITESPACE)
  if(SPHINX_OUTPUT MATCHES "Sphinx [^ ]* ([0-9][^ \n]*)")
	set(SPHINX_VERSION "${CMAKE_MATCH_1}")
	set(HAVE_SPHINX TRUE)
  elseif(SPHINX_OUTPUT MATCHES "sphinx-build ([0-9][^ \n]*)")
	set(SPHINX_VERSION "${CMAKE_MATCH_1}")
	set(HAVE_SPHINX TRUE)
  endif()
endif()

find_program(JAVASPHINX_EXECUTABLE javasphinx-apidoc)
if(JAVASPHINX_EXECUTABLE)
  execute_process(COMMAND "pip" "show" "javasphinx"
	OUTPUT_VARIABLE PIPLIST_OUTPUT
	OUTPUT_STRIP_TRAILING_WHITESPACE)
  if(PIPLIST_OUTPUT MATCHES "Version: ([0-9.]+)")
	set(JAVASPHINX_VERSION "${CMAKE_MATCH_1}")
	set(HAVE_JAVASPHINX TRUE)
  endif()
endif()

find_program(XELATEX_COMPILER xelatex)
if(XELATEX_COMPILER)
  execute_process(COMMAND "${XELATEX_COMPILER}" "--version"
	OUTPUT_VARIABLE XELATEX_OUTPUT
	OUTPUT_STRIP_TRAILING_WHITESPACE)
  if(XELATEX_OUTPUT MATCHES "XeTeX ([0-9][^ \n]+)")
	set(XELATEX_VERSION "${CMAKE_MATCH_1}")
	set(HAVE_XELATEX TRUE)
  endif()
endif()

find_program(BIBTEX_COMPILER bibtex)
if(BIBTEX_COMPILER)
  execute_process(COMMAND "${BIBTEX_COMPILER}" "--version"
	OUTPUT_VARIABLE BIBTEX_OUTPUT
	OUTPUT_STRIP_TRAILING_WHITESPACE)
  if(BIBTEX_OUTPUT MATCHES "BibTeX ([0-9a-z][^ \n]+)")
	set(BIBTEX_VERSION "${CMAKE_MATCH_1}")
	set(HAVE_BIBTEX TRUE)
  endif()
endif()

######################################################################
### UseSphinx.cmake ends here
