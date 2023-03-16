LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"\/\/.*", "COMMENT"),
    (r"[ \t\n]+", None),
    (r"^true","TRUE"),
    (r'false','FALSE'),
    (r'bool','BOOL'),
    # Special characters
    (r"\(", "L_PAREN"),
    (r"\)", "R_PAREN"),
    (r"\{", "L_CURL_BRACKET"),
    (r"\}", "R_CURL_BRACKET"),
    (r'\;', 'TERMINATOR'),
    (r'\=', 'ASSIGN'),
    (r'\+', 'ADDITION'),
    (r'\-', 'SUBTRACTION'),
    (r'\*', 'MULTIPLICATION'),
    (r'\/', 'DIVISION'),
    (r'\[','CROCHET['),
    (r'\]','CROCHET]'),
    
    # Keywords
    (r"int", "TYPE_INT"),
    (r"main", "KW_MAIN"),
    (r"\w+","IDENTIFIER"),
]
