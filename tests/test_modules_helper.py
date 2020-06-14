import pytest
from modules import helper

# Using simple parametrize
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

# Using fixture
@pytest.fixture
def get_search_data():
        return [
            ({'search': 'search'}, '?search=search'),
            ({'search': 'search', 'test': 'test'}, '?test=test&search=search'),
            ({},'')
        ]


def test_should_pass_fixtures(get_search_data):
    for search_data in get_search_data:
        actual_result = helper.build_query_strings(search_data[0])
        assert actual_result == search_data[1]