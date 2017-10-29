# This file is for testing while in development!
from FileIO import FileIO


def test_file_io():
    FileIO.load_rules('JSON/test_rules.json')
    FileIO.load_phones('JSON/phones.json')
    FileIO.load_questions('JSON/test_questions.json')

test_file_io()
