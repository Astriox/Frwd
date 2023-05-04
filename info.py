from os import environ

API_ID = int(environ.get('API_ID', '7822571'))
API_HASH = environ.get('API_HASH', '067329e70bfc5b3022f77080703da788')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
OWNER = int(environ.get('OWNER', '1908563535'))
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', True))
