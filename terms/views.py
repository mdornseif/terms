# encoding: utf-8
"""
views.py

Created by Christian Klein on 2010-09-27.
Copyright (c) 2010 HUDORA. All rights reserved.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from terms.forms import AgreementForm
from terms.models import Terms


def agree(request):
    
    next = request.REQUEST.get('next', '/')
    
    if 'terms_pk' in request.POST:
        terms = Terms.objects.get(pk=request.POST.get('terms_pk'))
    else:
        terms = Terms.objects.latest()
    
    if request.method == "POST":
        form = AgreementForm(request.user, terms, request.POST)
        if form.is_valid():
            agreement = form.get_agreement_object()
            agreement.save()
            return HttpResponseRedirect(next)
    else:
        form = AgreementForm(request.user, terms)
    
    return render_to_response('terms/agree.html',
                              {'form': form, 'next': next, 'terms': terms},
                              context_instance=RequestContext(request))