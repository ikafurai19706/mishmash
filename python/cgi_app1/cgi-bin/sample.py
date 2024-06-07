#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi

Forms = cgi.FieldStorage()

Value1 = int(Forms["Value1"].value)
Value2 = int(Forms["Value2"].value)
Answer = (Value1 ** Value2)  

Text = """
<html>

    <head>
        <meta charset="utf-8">
        <title>Exponents Calculator</title>
    </head>

    <body>
        <h1>Exponents Calculator</h1>
        The answer is %s.
        <br>
        <br>
        <a href="../index.html">Back</a>
    </body>

</html>
"""%Answer

print(Text)