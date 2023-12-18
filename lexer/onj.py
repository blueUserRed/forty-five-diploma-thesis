"""
    pygments.lexers.onj
    ~~~~~~~~~~~~~~~~~~~
"""

import re

# from pygments.lexer import bygroups, combined, default, do_insertions, include, \
#     inherit, Lexer, RegexLexer, this, using, words, line_re
# from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
#     Number, Punctuation, Other, Generic, Whitespace
# from pygments.util import get_bool_opt
# import pygments.unistring as uni

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = [ "OnjLexer" ]

class OnjLexer(RegexLexer):

    name = 'Onj'
    aliases = ['onj', "onjschema", "OnjSchema"]
    filenames = ['*.onj', "*.onjschema"]
    mimetypes = ['text/onj']

    flags = re.DOTALL | re.MULTILINE
    tokens = {
        "root": [
            (r'/\*.*?\*/', Comment.Multiline),
            (r'//.*?$', Comment.Singleline),
            (r'(\.\.\.)([a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Operator, Name.Constant)),
            (r'([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(:)', bygroups(Name.Attribute, Text.Whitespace, Punctuation)),
            (r'(var)(\s+)([a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Keyword.Declaration, Text.Whitespace, Name.Constant)),
            (r'(use)(\s+)([a-zA-Z_][a-zA-Z0-9_]*)(;)', bygroups(Keyword.Reserved, Text.Whitespace, Name.Namespace, Punctuation)),
            (r'(import)(\s+)(["\'].*?["\'])(\s+)(as)(\s+)([a-zA-Z_][a-zA-Z0-9_]*)',
             bygroups(Keyword.Reserved, Text.Whitespace, String, Text.Whitespace, Keyword.Reserved, Text.Whitespace, Name.Constant)),
            (r'(\$)([a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Punctuation, Name.Class)),
            (r'([a-zA-Z_][a-zA-Z0-9_]*)(\()', bygroups(Name.Function, Punctuation)),
            (r'(#)([a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Punctuation, Name.Function)),
            (r'0[bB][01]+', Number.Bin),
            (r'0[oO][0-7]+', Number.Oct),
            (r'0[xX][0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'(\.[0-9]+|[0-9]+\.[0-9]*|[0-9]+)', Number.Float),
            (r'\+|-|\*|/|\.\.\.|!', Operator),
            (r':|,|;|=|\.', Punctuation),
            (r'\(|\)|\[|\]|\{|\}', Punctuation),
            (r'true|false|null|NaN|Infinity', Keyword.Constant),
            (r'int|string|boolean|float', Keyword.Type),
            (r'\s+', Text.Whitespace),
            (r'".*?"', String),
            (r'\'.*?\'', String),
            (r'([a-zA-Z_][a-zA-Z0-9_]*)', Name.Constant)
        ]
    }

