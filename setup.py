from setuptools import setup

APP = ['main2.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['certifi', 'customtkinter'],
    'excludes': ['client_secret.json'],
    'plist': {
        'CFBundleName': "ProductInfoFetcher",
        'CFBundleDisplayName': "Product Info Fetcher",
        'CFBundleGetInfoString': "Fetches product information from Amazon and Flipkart",
        'CFBundleIdentifier': "com.yourdomain.ProductInfoFetcher",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0",
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
