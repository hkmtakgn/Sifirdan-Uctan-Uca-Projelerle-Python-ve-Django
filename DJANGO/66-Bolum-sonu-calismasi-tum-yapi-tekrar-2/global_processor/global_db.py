from django.template.loader import render_to_string


def global_user (request):
    user = request.user
    return dict (
        user=user,
    )

def global_picsum (request):
    picsum = [
        f'https://picsum.photos/id/{id}/1200/300' for id in range (1,4)
    ]
    return dict (
        picsum=picsum,
    )

def global_pages (request):
    text_html_content = render_to_string('components/text.html')
    pages = [
        {
            'url':'vision',
            'details':f'''
            <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1>Vizyonumuz sayfasina hosgeldiniz!</h1>
    {text_html_content}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
            '''
            },
    ]
    return dict (
        pages=pages,
    )

def global_products (request):
    web_products = [
        'Html',
        'Css',
        'BootStrap',
        'JavaScript',
        'React',
        'Django',
        'Python',
    ]
    general_products = [
        'C',
        'C++',
        'C#',
        'Python',
        'Java',
        'Dart',
        'Go',
        'Lua',
    ]
    return dict (
        web_products=web_products,
        general_products=general_products,
    )

