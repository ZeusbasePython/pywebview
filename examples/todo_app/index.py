import os
import webview

"""
An example of serverless app architecture using webview.start() function
"""


def load_asset(filename):
    with open(filename) as f:
        return f.read()


class Api():
    def addItem(self, title):
        print('Added item %s' % title)

    def removeItem(self, item):
        print('Removed item %s' % item)

    def editItem(self, item):
        print('Edited item %s' % item)

    def toggleItem(self, item):
        print('Toggled item %s' % item)


if __name__ == '__main__':
    html = load_asset('index.html')
    api = Api()

    #webview.start('TODOS BRAVOS', html=html, css=css, js_api=api, options={'min_size': (600, 450)})
    webview.start('TODOS BRAVOS', 'index.html', js_api=api, options={'min_size': (600, 450)})

