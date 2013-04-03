#!/usr/bin/env python

import re

commentRegex = r'<!--(?!.*build-o-matic)'

# removes html comments (except for build-o-matic tags)
def removeComments(html):

    modHtml = html

    while re.search(commentRegex, modHtml):
        start = re.search(commentRegex, modHtml).start()
        end = modHtml[start:].find("-->") + 3
        modHtml = modHtml.replace(modHtml[start:end+start], "")

    return modHtml


def removeWhitespace(html):
    mod = re.sub(r'  ', "", html)
    mod = re.sub(r'\n\n', "", mod)
    return mod
