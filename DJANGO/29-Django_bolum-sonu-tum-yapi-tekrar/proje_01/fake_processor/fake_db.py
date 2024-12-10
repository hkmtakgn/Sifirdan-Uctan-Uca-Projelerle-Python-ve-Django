

def my_db_processor (request):
    one_pic_url = [
    f"https://picsum.photos/id/1/200/300"]

    three_pic_carousel = [
    f"https://picsum.photos/id/{id}/1200/300" for id in range (1,4)]
    return dict (
        one_pic_url=one_pic_url,
        three_pic_carousel=three_pic_carousel,
    )
