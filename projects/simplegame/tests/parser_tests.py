from nose.tools import *
from ex49.parser import *


def test_peek():
    result = peek([('verb', 'run'), ('direction', 'north')])
    assert_equal(result, 'verb')


def test_match():
    result = match([('verb', 'run'), ('direction', 'north')], 'verb')
    assert_equal(result, ('verb', 'run'))


def test_skip():
    result = [('stop', 'at'), ('stop', 'the'), ('direction', 'north')]
    skip(result, 'stop')
    assert_equal(result, [('direction', 'north')])


def test_parse_verb():
    result = parse_verb([('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(result, ('verb', 'eat'))


def test_parse_object():
    result = parse_object([('stop', 'the'), ('noun', 'honey')])
    assert_equal(result, ('noun', 'honey'))


def test_parse_subject():
    result = parse_subject([('verb', 'run'), ('direction', 'south')])
    assert_equal(result, ('noun', 'player'))


def test_parse_sentence():
    result = parse_sentence([('noun', 'bear'), ('verb', 'eat'),
                             ('stop', 'the'), ('noun', 'honey')])

    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'eat')
    assert_equal(result.object, 'honey')


def test_fails():
    assert_raises(Exception, parse_verb, [('stop', 'the'), ('noun', 'honey')])
    assert_raises(Exception, parse_object, [('stop', 'the'), ('verb', 'run')])
    assert_raises(Exception, parse_subject, [('stop', 'the'),
                                             ('direction', 'north')])
