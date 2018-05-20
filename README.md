# hastebin.py
A simple Hastebin API wrapper for Python.
## Installation
`pip3 install hastebin.py`
## Usage
function `post` - takes a string and returns a URL.

## Example
`import hastebin` for blocking request. `import async_hastebin as hastebin` for non-blocking request (in a coroutine).
`print(hastebin.post(input("Enter text to upload to Hastebin: ")))`
