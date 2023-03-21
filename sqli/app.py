from argparse import ArgumentParser

from aiohttp.web import Application
from aiohttp_jinja2 import setup as setup_jinja
from jinja2.loaders import PackageLoader
from trafaret_config import commandline

from sqli.middlewares import session_middleware, error_middleware
from sqli.schema.config import CONFIG_SCHEMA
from sqli.services.db import setup_database
from sqli.services.redis import setup_redis
from sqli.utils.jinja2 import csrf_processor, auth_user_processor
from .routes import setup_routes


def init(argv):
    ap = ArgumentParser()
    commandline.standard_argparse_options(ap, default_config='./config/dev.yaml')
    options = ap.parse_args(argv)

    config = commandline.config_from_options(options, CONFIG_SCHEMA)

    app = Application(
        debug=True,
        middlewares=[
            session_middleware,
            # csrf_middleware,
            error_middleware,
        ]
    )
    app['config'] = config

    setup_jinja(app, loader=PackageLoader('sqli', 'templates'),
                context_processors=[csrf_processor, auth_user_processor],
                autoescape=False)
    setup_database(app)
    setup_redis(app)
    setup_routes(app)

    return app

AWS_ACCESS_KEY = 'AKIAQWESQRFOQ4KOQAPK'
AWS_SECRET_KEY = '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'
AWS_CONSOLE_PASSWORD = '$ecureAdmin1000'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE10000/2DWbl'


Subdomain enumeration: discovering all subdomains related to the domain of an organization.
DNS records analysis: inspecting DNS records to gather information about the infrastructure of an organization.
Web server fingerprinting: identifying the technology stack of a web server by analyzing the HTTP response headers.
IP address mapping: discovering how many subdomains are mapped to the same IP address.
Open port scanning: identifying open ports on servers to identify potential attack vectors.
Screenshots of web applications: taking screenshots of web applications to visually inspect them for potential security issues.
Service enumeration: identifying which services are running on open ports and their versions.
Operating system detection: identifying the operating system running on a target system.
Subdomain expiry date analysis: discovering the expiry date of subdomains to identify potential domains that could be claimed by malicious actors.
SSL certificate analysis: determining which Certificate Authority (CA) has issued SSL certificates for a target domain and when they will expire.
Reputation analysis: analyzing an organization's reputation in the cybersecurity community.
Hosted Region
