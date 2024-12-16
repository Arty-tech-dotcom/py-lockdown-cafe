class Cafe:
    def __init__(self,name: str):
        self.name = name
    def visit_cafe(self,visitor : dict) -> dict:
        try