#!/usr/bin/env python
"""Unpack a MIME message into a directory of files."""
from __future__ import print_function
from argparse import ArgumentParser
import email
import errno
import mimetypes
import os
import sys

def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('-v', dest='verbose', action='store_true',
        help='List while extracting')
    parser.add_argument('-l', dest='list', action='store_true',
        help='List without extracting')
    parser.add_argument('msgfile', nargs='+', help='MIME multipart/* file to '
        'extract content from')
    args = parser.parse_args()
    if args.list:
        args.verbose = True
        extract = False
    else:
        extract = True
    for msgfile in args.msgfile:
        base_file = os.path.basename(msgfile)
        noext_file = os.path.splitext(base_file)[0]
        if noext_file == base_file:
            noext_file += '-out'
        directory = os.path.normpath(noext_file)
        if os.path.exists(directory):
            print(
                '%s: %s exists, skipping...' % (msgfile, directory),
                file=sys.stderr,
            )
        with open(msgfile) as fp:
            msg = email.message_from_file(fp)

        counter = 1
        for part in msg.walk():
            # multipart/* are just containers
            if part.get_content_maintype() == 'multipart':
                continue
            rel_path = part.get_filename()
            full_path = os.path.normpath(os.path.join(
                directory,
                rel_path or 'part-%03d%s' % (
                    counter,
                    mimetypes.guess_extension(
                        part.get_content_type()
                    ) or '.bin',
                )
            ))
            if not full_path.startswith(directory):
                print(
                    '%s: %r tries to exit base directory, skipping...' % (
                        msgfile,
                        rel_path,
                    ),
                    file=sys.stderr,
                )
                continue
            counter += 1
            if args.verbose:
                print(full_path)
            if extract:
                dirname = os.path.dirname(full_path)
                if dirname:
                    try:
                        os.makedirs(dirname)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise
                with open(full_path, 'wb') as fp:
                    payload = part.get_payload(decode=True)
                    if payload:
                        fp.write(payload)

if __name__ == '__main__':
    main()
