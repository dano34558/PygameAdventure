class Item:
    def __init__(self, item_type, stats=None):
        self.item_type = item_type
        self.stats = stats or {}