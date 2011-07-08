#!/usr/bin/python
# -*- coding: utf-8 -*-
__VERSION__ = "0.1"

import sys
import urllib2
from optparse import OptionParser


def parse_options():
    parser = OptionParser(description="Simple jquery downloader.")
    parser.add_option("-v", "--version", action="store_true",
                      dest="version", default=False,
                      help="Prints version of downloader")
    parser.add_option("-j", "--jquery-version", dest="jquery_version", default="",
                      help="Specify version of jquery")
    parser.add_option("-m", "--min", action="store_true", dest="min",
                      default=False,
                      help="Download minified version")
    parser.add_option("-s", "--show-url", action="store_true", dest="show_url",
                      default=False,
                      help="Show costructed url only")
    options, args = parser.parse_args()
    return options

JQUERY_URL = "http://code.jquery.com/jquery{version}{min}.js"

def format_version(version):
    """
    >>> format_version("1.3.4")
    >>> "-1.3.4"
    >>>
    >>> format_version("")
    >>> ""
    >>>
    >>> format_version("-1.5.6")
    >>> "-1.5.6"
    """
    if not version:
        return version
    if version.startswith('-'):
        return version
    return ''.join(['-', version])

def format_min(min_):
    """
    >>> format_min(True)
    >>> ".min"
    >>>
    >>> format_min(False)
    >>> ""
    """
    if min_:
        return ".min"
    return ""

def download(opts):
    url = JQUERY_URL.format(version=format_version(opts.jquery_version), min=format_min(opts.min))

    if opts.version:
        print "jQuery downloader v{version}".format(version=__VERSION__)
        return

    if opts.show_url:
        print url
        return

    for line in urllib2.urlopen(url):
        print line,

if __name__ == '__main__':
    download(parse_options())
