from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Paper


def all_cvs(request):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    if request.method == 'POST':
        request.session['search_by'] = request.POST['search_by']
        request.session['search'] = request.POST['search']

    if not request.session.get('search', None):
        paperlist = Paper.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(paperlist, 60)
        last_page = paginator.num_pages

        try:
            papers = paginator.page(page)
        except PageNotAnInteger:
            papers = paginator.page(1)
        except EmptyPage:
            papers = paginator.page(paginator.num_pages)

        return render(request, 'library/allcvs.html', {'papers': papers, 'last_page': last_page})

    else:
        search_by = request.session['search_by']
        search = request.session['search']

        if search_by == 'title':
            paperlist = Paper.objects.filter(title__icontains=search)
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        elif search_by == 'author':
            paperlist = Paper.objects.filter(author__icontains=search)
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        else:
            paperlist = Paper.objects.filter(
                Q(title__icontains=search) | Q(author__icontains=search)
            )
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        try:
            papers = paginator.page(page)
        except PageNotAnInteger:
            papers = paginator.page(1)
        except EmptyPage:
            papers = paginator.page(paginator.num_pages)

        return render(request, 'library/allcvs.html', {'papers': papers, 'last_page': last_page})


def cvpr_by_year(request, year):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    if request.method == 'POST':
        request.session['search_by'] = request.POST['search_by']
        request.session['search'] = request.POST['search']

    if not request.session.get('search', None):
        paperlist = Paper.objects.filter(
            Q(conference='cvpr'), Q(year=year)
        )
        page = request.GET.get('page', 1)
        paginator = Paginator(paperlist, 60)
        last_page = paginator.num_pages

        try:
            papers = paginator.page(page)
        except PageNotAnInteger:
            papers = paginator.page(1)
        except EmptyPage:
            papers = paginator.page(paginator.num_pages)

        return render(request, f'library/cvpr{year}.html', {'papers': papers, 'last_page': last_page})

    else:
        search_by = request.session['search_by']
        search = request.session['search']

        if search_by == 'title':
            paperlist = Paper.objects.filter(
                Q(conference='cvpr'), Q(year=year),
                Q(title__icontains=search)
            )
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        elif search_by == 'author':
            paperlist = Paper.objects.filter(
                Q(conference='cvpr'), Q(year=year),
                Q(author__icontains=search)
            )
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        else:
            paperlist = Paper.objects.filter(
                Q(conference='cvpr'), Q(year=year),
                Q(title__icontains=search) | Q(author__icontains=search)
            )
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        try:
            papers = paginator.page(page)
        except PageNotAnInteger:
            papers = paginator.page(1)
        except EmptyPage:
            papers = paginator.page(paginator.num_pages)

        return render(request, f'library/cvpr{year}.html', {'papers': papers, 'last_page': last_page})


def other_cvs(request, conf, year):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    if request.method == 'POST':
        request.session['search_by'] = request.POST['search_by']
        request.session['search'] = request.POST['search']

    if not request.session.get('search', None):
        paperlist = Paper.objects.filter(
            Q(conference=conf), Q(year=year),
        )
        page = request.GET.get('page', 1)
        paginator = Paginator(paperlist, 60)
        last_page = paginator.num_pages

        try:
            papers = paginator.page(page)
        except PageNotAnInteger:
            papers = paginator.page(1)
        except EmptyPage:
            papers = paginator.page(paginator.num_pages)

        return render(request, f'library/{conf}{year}.html', {'papers': papers, 'last_page': last_page})

    else:
        search_by = request.session['search_by']
        search = request.session['search']

        if search_by == 'title':
            paperlist = Paper.objects.filter(
                Q(conference=conf), Q(year=year),
                Q(title__icontains=search)
            )
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        elif search_by == 'author':
            paperlist = Paper.objects.filter(
                Q(conference=conf), Q(year=year),
                Q(author__icontains=search)
            )
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        else:
            paperlist = Paper.objects.filter(
                Q(conference=conf), Q(year=year),
                Q(title__icontains=search) | Q(author__icontains=search)
            )
            page = request.GET.get('page', 1)
            paginator = Paginator(paperlist, 60)
            last_page = paginator.num_pages

        try:
            papers = paginator.page(page)
        except PageNotAnInteger:
            papers = paginator.page(1)
        except EmptyPage:
            papers = paginator.page(paginator.num_pages)

        return render(request, f'library/{conf}{year}.html', {'papers': papers, 'last_page': last_page})


def search_retry(request, return_url):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    request.session['search_by'] = 'all'
    request.session['search'] = ''
    return redirect(return_url)
