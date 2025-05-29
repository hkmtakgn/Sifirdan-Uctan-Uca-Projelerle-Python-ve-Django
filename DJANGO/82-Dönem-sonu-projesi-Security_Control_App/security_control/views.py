from django.shortcuts import redirect, render
from security_control.forms.registration import VisitorForm, SubcontractorForm
from security_control.models import Visitor, Subcontractor
from django.shortcuts import get_object_or_404

# Create your views here.


def home_views(request):
  context = dict()
  return render(request, "pages/home.html", context)


def visitor_views(request):
  title = "visitor"
  items = Visitor.objects.all()
  context = dict(
      items=items,
      title=title,
  )
  return render(request, "pages/visitor.html", context)


def subcontractor_views(request):
  title = "subcontractor"
  subcontractor_items = Subcontractor.objects.all()
  context = dict(
      subcontractor_items=subcontractor_items,
      title=title,
  )
  return render(request, "pages/subcontractor.html", context)


def visitor_register_views(request):
  form = VisitorForm()
  if request.method == "POST":
    form = VisitorForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("visitor")
  context = dict(VisitorForm=form, )
  return render(request, "pages/register_visitor.html", context)


def subcontractor_register_views(request):
  form = SubcontractorForm()
  if request.method == "POST":
    form = SubcontractorForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("subcontractor")
  context = dict(SubcontractorForm=form, )
  return render(request, "pages/register_subcontractor.html", context)


def visitor_details_views(request, id):
  title = "Visitor Details"
  item = Visitor.objects.filter(id=id).first()
  context = dict(
      item=item,
      title=title,
  )
  return render(request, "pages/profile_details.html", context)


def subcontractor_details_views(request, id):
  title = "Subcontractor Details"
  subcontractor_item = get_object_or_404(Subcontractor, id=id)
  context = dict(
      subcontractor_item=subcontractor_item,
      title=title,
  )
  return render(request, "pages/profile_details.html", context)
