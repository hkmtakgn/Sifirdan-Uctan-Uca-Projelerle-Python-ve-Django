def fake_db_picsum (request):
    fake_db_picsum = [
        f"https://picsum.photos/id/{id}/1200/300" for id in range (1,4)
    ]
    return dict(
        fake_db_picsum=fake_db_picsum,
    )

def lorem_for_products (request):
    lorem_for_products = [
        f"https://picsum.photos/id/{id}/200/300" for id in range (1,21)
    ]
    return dict (
        lorem_for_products=lorem_for_products,
    )
