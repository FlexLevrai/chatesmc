
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
