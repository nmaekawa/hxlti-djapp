hxlti
============

django app to implement a lti provider


quick start
============

hxlti requires a redis instance running, and by default it will look for
`redis://localhost:6379/0`.

1. add "hxlti" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'hxlti',
    ]

2. include the hxlti urlconf in your project `urls.py` like this:

    path('lti/', include('hxlti.urls')),

3. run `python manage.py migrate` to create hxlti models for consumer keys

4. start the development server and visit `http://127.0.0.1:8000/admin/` to
   create a consumer (you will need the `Admin` app enabled)

5. configure your lti consumer with the created consumer keys in the previous
   step, and use the launch url `http://127.0.0.1:8000/lti/launch/`


other configs
=============

some other settings for hxlti:

    # hxlti app settings
    HXLTI_ENFORCE_SSL = True  # check if request protocol is https, default is false
    HXLTI_DUMMY_CONSUMER_KEY = os.environ.get('HXLTI_DUMMY_CONSUMER_KEY', 'dummy')
    HXLTI_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')










