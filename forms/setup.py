from setuptools import setup

requires = [
    'deform',
    'pyramid',
    'pyramid_chameleon',
    'waitress'
]

dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest'
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ]
    }
)
