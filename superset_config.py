import os
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
# ROW_LIMIT = 5000
SUPERSET_WORKERS = 1 # for it to work in heroku basic/hobby dynos increase as you like

# SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = "mysimplesecret"  # noqa

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# Superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

# Flask-WTF flag for CSRF
CSRF_ENABLED = True
