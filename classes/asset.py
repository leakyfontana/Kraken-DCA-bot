class Asset(): 
    def __init__(self, dict):
        self.aclass: str
        self.altname: str
        self.decimals: int
        self.display_decimals: int
        self.status: str

        for key in dict:
            setattr(self, key, dict[key])

    def __str__(self):
        return f'Asset({self.altname})'