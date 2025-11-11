from django.shortcuts import redirect, render, get_object_or_404
from xdevs.models import Developer, Web_Pages
from xdevs.forms.forms import Add_Page_Form

# Create your views here.


def x_home_views(request):
  web_pages = Web_Pages.objects.filter(is_active=True)
  title = "X-Developers"
  page_title = title
  context = dict(
      page_title=page_title,
      web_pages=web_pages,
  )
  return render(request, "pages/x_home.html", context)


def web_views(request, page_slug, lang_slug=None):
  if page_slug == "front-end" and not lang_slug:
    page = get_object_or_404(Web_Pages, slug=page_slug)
    dept = get_object_or_404(Web_Pages, slug=page_slug)
    tags = dept.tag.filter(is_active=True)
    title = "Front End"
    context = dict(
        page=page,
        page_title=title,
        items=tags,
    )
    return render(request, "pages/data_list.html", context)
  if page_slug == "back-end" and not lang_slug:
    page = get_object_or_404(Web_Pages, slug=page_slug)
    dept = get_object_or_404(Web_Pages, slug=page_slug)
    tags = dept.tag.filter(is_active=True)
    title = "Back End"
    context = dict(
        page=page,
        page_title=title,
        items=tags,
    )
    return render(request, "pages/data_list.html", context)
  if page_slug == "full-stack":
    page = get_object_or_404(Web_Pages, slug=page_slug)
    dept = get_object_or_404(Web_Pages, slug=page_slug)
    tags = dept.tag.filter(is_active=True)
    title = "Full Stack"
    context = dict(
        page=page,
        page_title=title,
        items=tags,
    )
    return render(request, "pages/data_list.html", context)
  elif page_slug == "add-page":
    if request.method == "POST":
      Add_Form = Add_Page_Form(request.POST)
      if Add_Form.is_valid():
        Add_Form.save()
        return redirect("x_home")
    else:
      Add_Form = Add_Page_Form()  # GET isteği için boş form

    title = "Add Page"
    context = dict(
        page_title=title,
        Add_Form=Add_Form,
    )
    return render(request, "pages/add_page.html", context)
  else:
    Add_Form = None
    page = None
    developers = None
    tags = None
    title = None
  context = dict(
      page_title=title,
      items=tags,
      page=page,
  )
  return render(request, "pages/data_list.html", context)


def lang_views(request, page_slug, lang_slug):
  title = "X-Developers"
  web_page = get_object_or_404(Web_Pages, slug=page_slug)
  w_lang = web_page.tag.filter(slug=lang_slug)
  developers = Developer.objects.filter(tag__slug=lang_slug)
  context = dict(
      page_title=title,
      items=developers,
  )
  return render(request, "pages/lang_details.html", context)


def dev_details(request, id):
  developer = get_object_or_404(Developer, pk=id)
  context = dict(developer=developer, )
  return render(request, "pages/dev_details.html", context)
