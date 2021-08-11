#!/usr/bin/env python3

# terraform validate
import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser(description='Validates the configuration files in a directory')
parser.add_argument('path', help='Terraform project path')
args = parser.parse_args()

COMMAND = ["terraform", "-chdir="+args.path, "validate", "-json"]

try:
    retcode = subprocess.call(COMMAND)
    sys.exit(retcode)
except OSError as e:
    print >>sys.stderr, "Command error:", e
    sys.exit(1)
# Done
