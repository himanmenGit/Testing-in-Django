from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from whatever.models import Whatever
from whatever.forms import WhateverForm
from django.http import HttpResponseRedirect


def whatever(request):
    args = {}
    args.update(csrf(request))
    args['whatever'] = Whatever.objects.all()

    return render_to_response('index.html', args)


def add(request):
    if request.POST:
        form = WhateverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = WhateverForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('add.html', args)
