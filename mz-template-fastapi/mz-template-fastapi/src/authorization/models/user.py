from typing import List


class User:
    def __init__(self, id, name='', preferred_username='', roles=None):
        self.id = id
        self.name = name
        self.preferred_username = preferred_username
        self.roles = roles if roles is not None else []