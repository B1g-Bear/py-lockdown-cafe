from cafe import Cafe
from errors import VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except VaccineError:
        return "All friends should be vaccinated"

    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"

        expiration_date = friend["vaccine"].get("expiration_date")
        today = __import__("datetime").date.today()
        if expiration_date is None or expiration_date < today:
            return "All friends should be vaccinated"

        if not friend.get("wearing_a_mask", False):
            masks_to_buy += 1

    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
