from home.appHome import Home

URLS = [
    ('/',Home.as_view('Home'),['GET']),
]