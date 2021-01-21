from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileFormItem
# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def resume_form(request):
    form = ProfileFormItem(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cv:landing')

    return render(request, 'add-edit-resume.html', {'form': form})


def delete_item(request, product_id):
    Product.objects.get(id=product_id).delete()
    return HttpResponseRedirect("/")