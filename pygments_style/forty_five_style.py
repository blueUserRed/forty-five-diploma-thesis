
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
        Comment:                   "#60a0b0",
        Comment.Preproc:           "#007020",
        Comment.Special:           "#fff0f0",

        Keyword:                   "#cf222e",
        Keyword.Pseudo:            "#cf222e",
        Keyword.Type:              "#6639ba",

        # Operator:                  "#666666",
        # Operator.Word:             "bold #007020",

        Name.Builtin:              "#6639ba",
        Name.Function:             "#6639ba",
        Name.Class:                "#6639ba",
        Name.Namespace:            "#6639ba",
        
        Operator:                   "#cf222e",

        String:                    "#13c623",
        String.Interpol:           "#6639ba",
        String.Escape:             "#cf222e",
        String.Regex:              "#13c623",
        String.Symbol:             "#13c623",
        String.Other:              "#13c623",
        
        Number:                    "#0550ba",

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
