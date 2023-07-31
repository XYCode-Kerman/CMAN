import config
import importlib
from config.languages import fake_localization

language: fake_localization = importlib.import_module('config.languages.' + config.LANGUAGE.value)