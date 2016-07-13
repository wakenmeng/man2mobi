#!/bin/python2
# -*- coding: utf-8 -*-

import commands
import sys

#TARGET_DIR = '~/Documents/manpages'
TARGET_DIR = './'

def man2html(cmd):
    """ transcape a man page of cmd to html, located in ~/Documents/manpages/
    """

    html_file = '%s%s.html' % (TARGET_DIR, cmd)

    # set MANWIDTH(line length) to 10000, avoiding line wrapping,
    # which could cause mobi character escape error.
    set_line_width = 'export MANWIDTH=10000'
    commands.getstatusoutput(set_line_width)

    # man to html
    gen_html = "man {cmd}| man2html -compress -cgiurl "\
              "man$section/$title.$section$subsection.html "\
              "> {html_file}".format(cmd=cmd, html_file=html_file)
    rst, output = commands.getstatusoutput(gen_html)
    if rst != 0 or output.startswith('No manual entry for'):
        raise Exception('man2html Error: %s' % output)
    print output

    # unset MANWIDTH to normal
    unset_width = 'unset MANWIDTH'
    commands.getstatusoutput(unset_width)

    # reformat html
    # Some manpages contains fullwidth format characters, for example tmux,
    # which will occur unreadable characters, mojibake.
    # Also I replace 4 spaces with one space, to make it more readable considering kindle screen size.
    with open(html_file, 'r') as hf:
        content = hf.read().replace('    ', ' ').replace('’', '\'').replace('‘', '\'')

    with open(html_file, 'w') as hf:
        hf.write(content)

    return html_file

def html2mobi(fhtml):
    gen_mobi = 'kindlegen %s' % fhtml
    rst, output =commands.getstatusoutput(gen_mobi)
    print output

    del_html = 'rm %s' % fhtml
    commands.getstatusoutput(del_html)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('What mannual cmd do you want?')
    cmd = sys.argv[1]
    print 'man2html...'
    fhtml = man2html(cmd)
    print 'html2mobi...'
    mobi = html2mobi(fhtml)

