
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Whitespace


__all__ = ['FortyFiveStyle']


class FortyFiveStyle(Style):

    name = 'forty_five_style'

    background_color = "#f0f0f0"
    line_number_color = "#666666"

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #60a0b0",
        Comment.Preproc:           "noitalic #007020",
        Comment.Special:           "noitalic bg:#fff0f0",

        Keyword:                   "bold #3163c5",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #3163c5",

        # Operator:                  "#666666",
        # Operator.Word:             "bold #007020",

        Name.Builtin:              "#228831",
        Name.Function:             "#4985ef",
        Name.Class:                "bold #34a8a4",
        Name.Namespace:            "bold #34a8a4",
        Name.Exception:            "#007020",
        Name.Variable:             "#9a2fc8",
        Name.Constant:             "#9a2fc8",
        Name.Label:                "bold #002070",
        Name.Entity:               "bold #d55537",
        Name.Attribute:            "#4070a0",
        Name.Tag:                  "bold #062873",
        Name.Decorator:            "bold #555555",

        String:                    "#35d44c",
        String.Doc:                "italic",
        String.Interpol:           "italic #70a0d0",
        String.Escape:             "bold #4070a0",
        String.Regex:              "#235388",
        String.Symbol:             "#517918",
        String.Other:              "#3c6355",
        Number:                    "#40a070",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.EmphStrong:        "bold italic",
        Generic.Prompt:            "bold #c65d09",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
