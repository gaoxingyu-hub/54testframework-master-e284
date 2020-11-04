"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CommentCommand(ROMCommand):
    def __init__(self, Comment=None, **kwargs):
        self._Comment = Comment  # Comment

        properties = kwargs.copy()
        if Comment is not None:
            properties['Comment'] = Comment

        # call base class function, and it will send message to renix server to create a class.
        super(CommentCommand, self).__init__(**properties)

    @property
    def Comment(self):
        """
        get the value of property _Comment
        """
        return self._Comment

    @Comment.setter
    def Comment(self, value):
        self._Comment = value

    def _set_comment_with_str(self, value):
        self._Comment = value

