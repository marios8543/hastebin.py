from distutils.core import setup
setup(
  name = 'hastebin.py',
  packages = ['hastebin'],
  version = '0.2',
  description = 'A simple Hastebin API wrapper for Python.',
  author = 'LyricLy',
  author_email = 'hanson.twentytwo@gmail.com',
  url = 'https://github.com/LyricLy/hastebin.py',
  download_url = 'https://github.com/LyricLy/hastebin.py/archive/0.1.tar.gz',
  keywords = ['hastebin'],
  install_requires = ['requests','aiohttp']
)
