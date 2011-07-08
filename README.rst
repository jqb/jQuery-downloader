Simple JQuery downloader
------------------------

Simple command line utility for fast jquery downloading.
Right now it works only for jquery (jquery-uj etc is not supported).


Why?
====

I've found it usefull. Maybe you will found it usefull too.


Usage
=====

::

   $ jquerydownloader.py [options]


With no options downloads latest version of jquery


Options
-------

::

  -h, --help            show this help message and exit
  -v, --version         Prints version of downloader
  -j JQUERY_VERSION, --jquery-version=JQUERY_VERSION
                        Specify version of jquery
  -m, --min             Download minified version
  -s, --show-url        Show costructed url only
