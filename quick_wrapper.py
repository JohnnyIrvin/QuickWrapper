#!/usr/bin/env python3
# Copyright (c) 2022 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import argparse

import utilities

parser = argparse.ArgumentParser(description='Wraps the exportable symbols from a PE file into a Python wrapper.')
parser.add_argument('analyzable', help='The file to analyze.', type=str)
parser.add_argument(
    '--license',
    help='The license file to use.',
    type=str,
    default=utilities.read_license('LICENSE')
)
parser.add_argument(
    '--output',
    help='The output file to write to.',
    type=str,
    default='output.py'
)
args = parser.parse_args()

code = "# " + args.license.replace('\n', '\n# ') + '\n'
code += "import ctypes\n"
code += "import typing\n"
code += '\n'
code += f'WRAPPER = ctypes.CDLL("{args.analyzable}")\n'
code += '\n'

for symbol in utilities.get_pe_export_symbols(args.analyzable):
    code += f'def {symbol}(*args: list) -> typing.Any:\n'
    code += f'    return WRAPPER.{symbol}(*args)\n'
    code += '\n'

utilities.write_python(args.output, code)
