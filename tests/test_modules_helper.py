from modules import helper

def test_should_pass_with_normal_query():
    query = {'search': 'search'}
    expected_result = '?search=search'

    actual_result = helper.build_query_strings(query)

    assert actual_result == expected_result

def test_should_pass_with_several_queries():
    query = {'search': 'search', 'test': 'test'}
    expected_result = '?test=test&search=search'

    actual_result = helper.build_query_strings(query)

    assert actual_result == expected_result

def test_should_pass_with_no_query():
    query = {}
    expected_result = ''

    actual_result = helper.build_query_strings(query)

    assert actual_result == expected_result

