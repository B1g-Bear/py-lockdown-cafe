import datetime

from errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name', 'Visitor')} is not vaccinated.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor.get('name', 'Visitor')} has an outdated vaccine.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor.get('name', 'Visitor')} is not wearing a mask.")

        return f"Welcome to {self.name}"
