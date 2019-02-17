import webview
import pytest

from .util import run_test


def test_load_html():
    run_test(webview, main_func, load_html, destroy_delay=0)


def main_func():
    webview.create_window('Load HTML test')


def load_html():
    webview.load_html('<h1>This is dynamically loaded HTML</h1>')


