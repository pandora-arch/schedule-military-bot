AVAILABLE = "Список доступних команд"
NOW_REPLY = "/now - зараз на екрані"

class Replies:
    """Class for /help replies"""
    def __init__(self):
        self._list = [AVAILABLE, NOW_REPLY]
    
    def __str__(self):
        return "\n".join(self._list)
