from inventory import Inventory
from equipment import Item


def test_inventory_initialization():
    inv = Inventory()
    assert isinstance(inv.items, list)
    assert len(inv.items) == 0


def test_inventory_with_items():
    item = Item(
        name="Rope",
        description="A sturdy rope.",
        item_type="gear",
        weight=2.0,
        cost=1.0,
        location=None,
    )
    inv = Inventory(items=[item])
    assert len(inv.items) == 1
    assert inv.items[0].name == "Rope"
    assert inv.items[0].weight == 2.0
