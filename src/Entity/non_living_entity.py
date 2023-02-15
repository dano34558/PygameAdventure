from Entity import Entity

class NonLivingEntity(Entity):
    def __init__(self, name):
        super().__init__(name=name, entity_type='non-living')