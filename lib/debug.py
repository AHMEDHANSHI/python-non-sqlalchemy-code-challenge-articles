#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

author = Article("Carry Bradshaw")
magazine = Article("Vogue", "Fashion")
article_1 = Article(author, magazine, "How to wear a tutu with style")
article_1.title ="How to wear a tutu with style"
article_1.author ="Carry Bradshaw"
article_2=Article(author,magazine,"")

author_1=Author("Carry Bradshaw")
author_2=Author("Nathaniel Hawthorne")

magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")

magazine_1.name="New Yorker"
magazine_2.name="AD"

magazine_1.








ipdb.set_trace()