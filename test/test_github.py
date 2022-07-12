"""
Testing github
"""
import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

url = 'https://github.com'
search_element = '.header-search-input'
repository = 'eroshenkoam/allure-example'
issue_tab = '#issues-tab'
issue_value = 'e.sh'


def test_selene():
    """
    Selene
    """

    browser.open(url)

    s(search_element).click()
    s(search_element).send_keys(repository)
    s(search_element).submit()

    s(by.link_text(repository)).click()

    s(issue_tab).click()

    s(by.partial_text(issue_value)).should(be.visible)


def test_dynamic_steps():
    """
    Lambda
    """

    with allure.step(f'Open: {url}'):
        browser.open(url)

    with allure.step(f'Find repository: {repository}'):
        s(search_element).click()
        s(search_element).send_keys(repository)
        s(search_element).submit()

    with allure.step(f'Choice repository: {repository}'):
        s(by.link_text(repository)).click()

    with allure.step('Open tab Issues'):
        s(issue_tab).click()

    with allure.step(f'Check Issue with name: {issue_value}'):
        s(by.partial_text(issue_value)).should(be.visible)


def test_decorator_steps():
    """
    Decorator
    """
    open_page(url)
    search_for_repository(repository)
    go_to_repository(repository)
    open_issue_tab()
    should_see_issue_with_name(issue_value)


@allure.step(f'Open: {url}')
def open_page(url: str):
    """
    Open page
    """
    browser.open(url)


@allure.step(f'Find repository: {repository}')
def search_for_repository(repository):
    """
    Search for repository
    """
    s(search_element).click()
    s(search_element).send_keys(repository)
    s(search_element).submit()


@allure.step(f'Choice repository: {repository}')
def go_to_repository(repository):
    """
    Go to repository
    """
    s(by.link_text(repository)).click()


@allure.step('Open tab Issues')
def open_issue_tab():
    """
    Open issue tab
    """
    s(issue_tab).click()


@allure.step(f'Check Issue with name: {issue_value}')
def should_see_issue_with_name(issue_value):
    """
    Check issue by name
    """
    s(by.partial_text(issue_value)).click()


@allure.tag('web', 'ui')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'evgenyshandrik')
@allure.feature('Testing github')
@allure.story(f'Find issue by name: {issue_value}')
@allure.link('https://github.com/evgenyshandrik', name='Owner')
def test_decorator_steps_with_label():
    """
    Test with labels
    """
    test_decorator_steps()
