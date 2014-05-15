import os
import logging
import sqlite3

from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.httpexceptions import HTTPFound
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.view import view_config

from wsgiref.simple_server import make_server

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    log.warn('Initializing database...')
    with open(os.path.join(here, 'data', 'schema.sql')) as f:
        stmt = f.read()
        settings = event.app.registry.settings
        db = sqlite3.connect(settings['db'])
        db.executescript(stmt)

@subscriber(NewRequest)
def new_request_subscriber(event):
    request = event.request
    settings = request.registry.settings
    request.db = sqlite3.connect(settings['db'])
    request.add_finished_callback(close_db_connection)

def close_db_connection(request):
    request.db.close()

@view_config(route_name='splash', renderer='splash.mako')
def splash_view(request):
    return {}

@view_config(route_name='signup', renderer='notfound.mako')
def signup_view(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            try:
                request.db.execute("insert into signups (source, email) "
                                   "values (?, ?)",
                                   [request.POST.get('source', 'default'),
                                    request.POST['email']])
                msg = "Thank you for signing up!"
            except sqlite3.IntegrityError:
                msg = "This email address has already signed up."
            request.db.commit()
            request.session.flash(msg)
            return HTTPFound(location=request.route_url('splash'))
        else:
            request.session.flash('Please enter an email address!')
    request.response.status = '404 Not Found'
    return {}

@view_config(context='pyramid.exceptions.NotFound', renderer='notfound.mako')
def notfound_view(request):
    request.response.status = '404 Not Found'
    return {}

# configuration settings
settings = {}
settings['reload_all'] = True
settings['debug_all'] = True
settings['db'] = os.path.join(here, 'data', 'stenosaurus.db')
settings['mako.directories'] = os.path.join(here, 'templates')
# session factory
session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
# configuration setup
config = Configurator(settings=settings, session_factory=session_factory)
# add mako templating
config.include('pyramid_mako')
# routes setup
config.add_route('splash', '/')
config.add_route('signup', '/signup')
config.add_static_view('static', os.path.join(here, 'static'))
# scan for @view_config and @subscriber decorators
config.scan()
# serve app
application = config.make_wsgi_app()

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8080, application)
    server.serve_forever()
