# pip install django-crispy-forms
# pip install crispy-bootstrap5
# INSTALLED_APPS = [
#    ...
#    "crispy_forms",
#    "crispy_bootstrap5",
# ]
# CRISPY_TEMPLATE_PACK = "bootstrap5"
# {% load crispy_forms_tags %}

# <form method="post" enctype="multipart/form-data" class="m-3">
#  {% csrf_token %}
#  {{ post_form|crispy }}
#  <button type="submit" class="btn btn-info">Kaydet</button>
# </form>
# 🧪 Son Kontrol ↓
#  → django-crispy-forms yüklü mü?
#  → INSTALLED_APPS içinde "crispy_forms" var mı?
#  → Template’in başında {% load crispy_forms_tags %} var mı?
#  → CRISPY_TEMPLATE_PACK tanımlı mı?
# 