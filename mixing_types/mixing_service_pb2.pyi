from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MixingRequest(_message.Message):
    __slots__ = ["image_url", "text", "language", "voice_gender", "voice_name", "driving_style", "use_enhancer", "target_height", "target_width", "target_size"]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    VOICE_GENDER_FIELD_NUMBER: _ClassVar[int]
    VOICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DRIVING_STYLE_FIELD_NUMBER: _ClassVar[int]
    USE_ENHANCER_FIELD_NUMBER: _ClassVar[int]
    TARGET_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TARGET_WIDTH_FIELD_NUMBER: _ClassVar[int]
    TARGET_SIZE_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    text: str
    language: str
    voice_gender: str
    voice_name: str
    driving_style: str
    use_enhancer: bool
    target_height: int
    target_width: int
    target_size: int
    def __init__(self, image_url: _Optional[str] = ..., text: _Optional[str] = ..., language: _Optional[str] = ..., voice_gender: _Optional[str] = ..., voice_name: _Optional[str] = ..., driving_style: _Optional[str] = ..., use_enhancer: bool = ..., target_height: _Optional[int] = ..., target_width: _Optional[int] = ..., target_size: _Optional[int] = ...) -> None: ...

class MixingResponse(_message.Message):
    __slots__ = ["text", "video", "is_final"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    text: str
    video: bytes
    is_final: bool
    def __init__(self, text: _Optional[str] = ..., video: _Optional[bytes] = ..., is_final: bool = ...) -> None: ...
