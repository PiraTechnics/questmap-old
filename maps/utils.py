from django.db.models import Model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

"""
def validate_ownership(request, Model):
    if request.user != Model.user:
        return False
    else:
        return True

def filter_entries(request, Model):
    filtered = Model.objects.filter(user=request.user)

"""

def validate_submitted_form(form, request):
    form_url = request.build_absolute_uri() #does this do what I think it does?

    if form.is_valid():
        validated = form.save(commit=False)
        validated.user = request.user
        validated.save()
        # Return to index
        return redirect('maps:index')

    else:
        # Return Blank form, let user try again -- and give an error message
        context = {'form': form}
        return render(request, form_url, context)