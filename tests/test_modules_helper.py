import pytest
from modules import helper

@pytest.mark.parametrize(
    'query, expected',
    [
        ({'search': 'search'}, '?search=search'),
        ({'search': 'search', 'test': 'test'}, '?test=test&search=search'),
        ({},'')
    ]
)
def test_should_pass_parametrize(query, expected):
    actual_result = helper.build_query_strings(query)
    assert actual_result == expected