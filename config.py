import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Cm.40l4EDE7EzPM~a7-.u400jF3i~Uz~.Q'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'shreyarticlecms'
    BLOB_STORAGE_KEY = os.environ.get('AZURE_STORAGE_KEY') or 'MejF65EWjR+6xq1X9H6nH37h2C9cc4RsYJfv0OphWkr7J2Wb+afH/kUqJqlPcMr8cEy4ZJA/W08NmR7D2z9XyA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'shrey-article-cms'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'shrey-article-cms.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'shrey-article-cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'shrey-article-cms'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Qwerty98765!'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = "Cm.40l4EDE7EzPM~a7-.u400jF3i~Uz~.Q"
    # if not CLIENT_SECRET:
    #   raise ValueError("Need to define AD_CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    
    CLIENT_ID = "0330a26a-c006-4913-aac8-3c787b4945de"

    # only works for my tenant (itesm.mx) and only in local mode until I upgrade to https.
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
