AVATAR_PREFIX = 'https://storage.googleapis.com/maika-ai-ext/virtual-avatar/preset_avatar'

AVATARS = ['maika', 'old-male-eu-2', 'young-female-eu-1', 'young-male-asia-1', 'young-male-eu-1']

LANG_MAP = {
    'Vietnamese': 'vi-VN',
    'English (US)': 'en-US',
    'English (UK)': 'en-GB'
}

GENDERS = ['MALE', 'FEMALE']

INTERNAL_VOICES = {
    'Maika': dict(
        language = 'vi-VN',
        voice_gender = '',
        voice_name = '',
    ),
}

NO_RESIZE = 'No resize (not recommended)'
OPTIMAL = 'Optimal'
BY_WIDTH = 'By width'
BY_HEIGHT = 'By height'
BY_WIDTH_HEIGHT = 'By width and height'

RESIZE_CHOICES = [NO_RESIZE, OPTIMAL, BY_WIDTH, BY_HEIGHT, BY_WIDTH_HEIGHT]