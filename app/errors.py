class VaccineError(Exception):
    """Base class for vaccine-related exceptions."""
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Visitor is not vaccinated"):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Visitor's vaccine is outdated"):
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Visitor is not wearing a mask"):
        super().__init__(message)
