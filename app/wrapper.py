from glam import Geocoder
from glam.types import NZSA


class Wrapper:
    gc = None

    @classmethod
    def load_geocoder(cls):
        cls.gc = Geocoder("glamdeps")

    @classmethod
    def parse_address(cls, address):
        as_dict = cls.gc.parse_addresses([address])[0].to_dict()
        return {k: v for k, v in as_dict.items() if v is not None}

    @classmethod
    def match_address(cls, address) -> tuple[dict[str, str | None], float]:
        tidied = cls.gc.parse_addresses([address])[0].format_address(human=True)

        matched = cls.gc.geocode_addresses([tidied])[0]

        conf = matched.confidence
        linz = matched.matched_address

        if linz is None:
            return {"error": "No match found."}, 0
        else:
            as_dict = linz.to_dict()

        return {k: v for k, v in as_dict.items() if v is not None}, conf

    @classmethod
    def search_address(cls, address):
        results = NZSA.df[
            NZSA.df["full_address_ascii"].str.contains(address, case=False)
        ]
        return results[
            [
                "address_id",
                "unit_value",
                "address_number",
                "address_number_suffix",
                "address_number_high",
                "suburb_locality",
                "town_city",
                "full_road_name",
                "full_address",
                "shape_X",
                "shape_Y",
            ]
        ]
