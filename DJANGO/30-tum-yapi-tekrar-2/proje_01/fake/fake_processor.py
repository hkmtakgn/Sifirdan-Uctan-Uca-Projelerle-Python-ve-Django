def global_processor (request):
    carousel_picsum = [
        f"https://picsum.photos/id/{id}/1200/300" for id in range (1,4)
    ]

    one_picsum = "https://picsum.photos/id/1/1200/300"

    card_picsum = [
        f"https://picsum.photos/id/{id}/150/150" for id in range (1,21)
    ]

    return dict (
        carousel_picsum=carousel_picsum,
        one_picsum=one_picsum,
        card_picsum=card_picsum,
    )
