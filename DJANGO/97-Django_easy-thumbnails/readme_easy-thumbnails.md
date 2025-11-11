1- pip install easy-thumbnails


2- INSTALLED_APPS = (
    ...
    'easy_thumbnails',
)

3- python manage.py migrate easy_thumbnails

4- THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
    },
}

5- {% load thumbnail %}
<!-- <img src="{{ post.post_img|thumbnail_url:'avatar' }}" alt="post_img" style="width:33%;height:33vh;margin:3px;border-radius:33px;"> -->
