man2mobi
==========
Convert linux manpage to kindle mobi file.

This is just a snippet which features converting linux manual page to mobi, a Kindle support format. Invoking this script need man2html and kindlegen. It converts manual page to html with man2html, and then genenrates mobi file from html with kindlegen. So basically I have did nothing:P But well, just for fun and enjoying the process.

####Requirements
* man2html
* kindlegen

####Usage
Example

	python man2mobi.py tmux

This will convert tmux manpage to a tmux.mobi in the current directory. It works on python2.7.

