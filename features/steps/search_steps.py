from behave import *
from nose.tools import assert_equal, assert_true


@given(u'I navigate to the PyPi Home page')
def step_impl(context):
    context.home_page.navigate("https://pypi.python.org/pypi")
    assert_equal(context.home_page.get_page_title(), "PyPI · The Python Package Index")


@when(u'I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)


@then(u'I am taken to the PyPi Search Results page')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), "Search results · PyPI")
