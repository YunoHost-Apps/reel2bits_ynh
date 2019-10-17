from .development import Config as BaseConfig


class Config(BaseConfig):
    # See the Configuration documentation at:
    # https://docs-develop.reel2bits.org/installation/configuration.html
    # For all the config keys you can use

    # Please generate me with: openssl rand -hex 42
    SECRET_KEY = "__SECRET_KEY__"
    # Please generate me with: openssl rand -hex 5
    SECURITY_PASSWORD_SALT = "__SECURITY_PASSWORD_SALT__"
    # Set your DB URI
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://__DB_USER__:__DB_PWD__@localhost/__DB_NAME__"

    # Don't forget that SOUNDS and ARTWORKS, etc. have to be under DEFAULT path folder
    UPLOADS_DEFAULT_DEST = "__DATADIR__/uploads"
    UPLOADED_SOUNDS_DEST = "__DATADIR__/uploads/sounds"
    UPLOADED_ARTWORKALBUMS_DEST = "__DATADIR__/uploads/artwork_albums"
    UPLOADED_ARTWORKSOUNDS_DEST = "__DATADIR__/uploads/artwork_sounds"
    UPLOADED_AVATARS_DEST = "__DATADIR__/uploads/avatars"

    # Where is the audiowaveform binary located
    AUDIOWAVEFORM_BIN = "__FINAL_PATH__/audiowaveform"

    # If you are using Sentry, otherwise, set to None
    SENTRY_DSN = None

    # The domain name your instance will be using
    REEL2BITS_HOSTNAME = "__DOMAIN__"
    # Is the ActivityPub backend active ?
    # Even at False, you needs to setup the AP_DOMAIN because it is used
    # by more things than just ActivityPub
    AP_ENABLED = True

    # Can the users register on your instance ?
    REGISTRATION_ENABLED = True

    # If you are using a modified instance, please set your own repository URL
    SOURCES_REPOSITORY_URL = "https://github.com/YunoHost-Apps/reel2bits_ynh"

    # Email settings
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    # MAIL_USERNAME = None
    # MAIL_PASSWORD = None

    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
