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


def final_resume(request, id):
    profile = Profile.objects.get(pk=id)

    context = {
        'profile': profile
    }

    return render(request, 'final-resume.html', context)

def list_view(request):
    profiles = Profile.objects.all()
    
    return render(request, 'list.html', {'profiles':profiles})



def delete_item(request, pk):
    Product.objects.get(pk=id).delete()
    return HttpResponseRedirect("/")