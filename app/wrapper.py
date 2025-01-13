
class Geocoder:
    
    def __init__(self, parser, matcher):
        self.parser = parser
        self.matcher = matcher

    def parse_address(self, address):
        return address

    def match_address(self, address):
        return address

class Wrapper:

    desired_parser = None
    desired_matcher = None

    parser = None
    matcher = None

    gc = None

    def set_parser(cls, parser):
        cls.desired_parser = parser

    def set_matcher(cls, matcher):
        cls.desired_matcher = matcher

    def init_geocoder(cls):
        if cls.gc is None:
            cls.gc = Geocoder(cls.parser, cls.matcher)
            


    def parse_address(cls, address):
        pass

    def match_address(cls, address):
        pass