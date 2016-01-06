import os
import json
import logging
import subprocess
import hashlib

import argh

import giza.operations.make

from giza.config.helper import fetch_config


def hash(path):
    """Return the SHA-256 hash of the given file."""
    hasher = hashlib.sha256()

    with open(path, 'rb') as input_file:
        while True:
            data = input_file.read(2**13)
            if not data:
                break

            hasher.update(data)

    return hasher.hexdigest()

def build_cache(root):
    """Get the hash of each file underneath root, and write it to a file."""
    with open(os.path.join(root, '../review-cache.txt'), 'w') as f:
        for basedir, dirs, files in os.walk(root):
            for file_path in files:
                file_path = os.path.join(basedir, file_path)
                f.write('{0} {1}\n'.format(hash(file_path), file_path))


@argh.arg('--edition', '-e', nargs='*')
@argh.expects_obj
@argh.named('review_stage')
def stage(args):
   """Populates review directory with changed files"""
   
   conf = fetch_config(args)
   
   # edition_suffixes = ['text' + ('-' if edition else '') + edition
   #                 for edition in args.edition]
                    
   # print (edition_suffixes)
   
   edition_suffix = 'review'
   
   # giza.operations.make("text-review") ?

   #roots = [os.path.join(conf.paths.projectroot,
   #    conf.paths.branch_output,
   #    edition_suffix) for edition_suffix in edition_suffixes]
   
   roots = [os.path.join(
      conf.paths.projectroot,
      conf.paths.branch_output,
      edition_suffix
   )]
   
   print (roots)

   #  for root in roots:
   #     build_cache(root)
   
   for root in roots:
      print (root)

   # 1 : run make text

   #2 : run review on text directory

   #3 : celebrate
   
 