import os
import json
class MyFamilies:
    _instance_ = None
    _initialized_ = False
    
    families = []
    # Format of families: [{"code": str, "is_enterprise": boolean}]
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance_:
            cls._instance_ = super().__new__(cls)
        return cls._instance_

    def __init__(self):
        if not self._initialized_:
            if os.path.exists("families.json"):
                self.load_families()
            else:
                # Create empty file
                with open("families.json", "w", encoding="utf-8") as f:
                    json.dump([], f, indent=4)