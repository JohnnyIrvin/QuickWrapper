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

def read_file(file_path: str) -> str:  
    """
    Reads the file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    with open(file_path, 'r') as f:
        return f.read()
    
def read_license(file_path: str) -> str:
    """
    Reads a license file.
    Alias for read_file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    return read_file(file_path)

def write_file(file_path: str, contents: str) -> None:
    """
    Writes the file.

    Args:
        file_path (str): The path to the file.
        contents (str): The contents to write.
    """
    with open(file_path, 'w') as f:
        f.write(contents)

def write_python(file_path: str, contents: str) -> None:
    """
    Writes a Python file.
    Alias for write_file.

    Args:
        file_path (str): The path to the file.
        contents (str): The contents to write.
    """
    write_file(file_path, contents)