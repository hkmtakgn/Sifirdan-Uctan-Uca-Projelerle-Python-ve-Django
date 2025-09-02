<!-- Static ↓ -->
1- <link rel="stylesheet" href="{% static 'css/tagify.css' %}">

2- <script src="{% static 'js/tagify.js' %}"></script>
                        &
<script src="{% static 'js/tagify.polyfills.min.js' %}"></script>

3- <script>
  var input = document.querySelector('input[name=addTag]');
                        &
  new Tagify(input)
</script>

<!-- CDN ↓ -->
{% block content %}
1- <link href="https://cdn.jsdelivr.net/npm/@yaireo/tagify/dist/tagify.css" rel="stylesheet" type="text/css" />

2- <script src="https://cdn.jsdelivr.net/npm/@yaireo/tagify"></script>
3- <script src="https://cdn.jsdelivr.net/npm/@yaireo/tagify/dist/tagify.polyfills.min.js"></script>

4- <script>
  var input = document.querySelector('input[name=addTag]')
  new Tagify(input)
</script>

{% endblock content %}

-------------------------------------

class Tag(models.Model):
title = models.CharField(max_length=100)
is_active = models.BooleanField(default=True)

def __str__(self):
  return self.title

-------------------------------------

class Post(BaseModel):
----addTag = models.CharField(max_length=100)
----tag = models.ManyToManyField(Tag)
favs = models.BooleanField(default=False)
post_img = models.ImageField(upload_to="post-img/", blank=True, null=True)

def __str__(self):
  return self.title

-------------------------------------

