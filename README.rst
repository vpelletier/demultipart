Unpack a MIME message into a directory of files.

Overview
========

MIME messages can be useful as cheap archives: unlike zipfile/tarfile standard
modules, email.mime.multipart does not require a full-functional file to
create an archive. MIME messages lack the ability to seek to a given file
efficiently (much like tar), they have no standard compression (but it can be
handled independently anyway), and lack a standard tool to extract them.

Inspired from python's _email_examples .

Usage
=====

Extract to current folder::

  $ demultipart /path/to/multipart_file

Extract to another folder::

  $ demultipart --directory /path/to/destination /path/to/multipart_file

Any number of multipart files can be specified, they will be extracted in
provided order.

Will overwrite files without asking.
Tries to prevent escaping extraction directory, but not tested on Windows.

TODO
====

- Provide compatibility with standard CLI archive manipulation tools (tar,
  unzip...) so GUI can wrap this command too.

- Maybe add multipart creation support.

.. _email_examples: http://docs.python.org/2/library/email-examples.html
