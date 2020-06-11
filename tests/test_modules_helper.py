from modules import helper

def test_should_pass_with_normal_query():
    query = {'search': 'search'}
    expected_result = '?search=search'

    actual_result = helper.build_query_strings(query)

    assert actual_result == expected_result




