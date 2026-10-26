
from decimal import Decimal


def product_fits_box(product, box):
    """
    Return True if the product fits inside the box,
    allowing the product to be rotated.
    """

    product_dimensions = sorted([
        Decimal(str(product["length"])),
        Decimal(str(product["width"])),
        Decimal(str(product["height"])),
    ])

    box_dimensions = sorted([
        box.length,
        box.width,
        box.height,
    ])

    dimensions_fit = all(
        product_side <= box_side
        for product_side, box_side in zip(
            product_dimensions, box_dimensions
        )
    )

    weight_fits = (
        Decimal(str(product["weight"])) <= box.max_weight
    )

    return dimensions_fit and weight_fits


def recommend_box(product, boxes):
    """
    Return the cheapest suitable box.

    If costs are equal, prefer the box with the smaller
    internal volume, then the alphabetically first name.
    """

    suitable_boxes = [
        box for box in boxes
        if product_fits_box(product, box)
    ]

    if not suitable_boxes:
        return None

    return min(
        suitable_boxes,
        key=lambda box: (
            box.cost,
            box.length * box.width * box.height,
            box.name.lower(),
        ),
    )
