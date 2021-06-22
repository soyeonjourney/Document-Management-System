from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Collection
from users.models import User
from library.models import Paper


def my_collection(request):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    request.session['search_by'] = 'all'
    request.session['search'] = ''
    user_id = request.session['user_id']
    collections = Collection.objects.filter(user_id=user_id)
    return render(request, 'collection/my-collection.html', {'collections': collections})


def add_collection(request, paper_id, return_url):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    paper = Paper.objects.get(id=paper_id)
    if paper:
        user_id = request.session['user_id']
        duplicated_paper = Collection.objects.filter(
            Q(user_id=user_id), Q(paper=paper)
        )
        if duplicated_paper:
            return redirect(return_url)
        else:
            new_collection = Collection(user_id=user_id, paper=paper)
            new_collection.save()
    return redirect(return_url)


def delete_collection(request, paper_id, return_url):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    paper = Paper.objects.get(id=paper_id)
    if paper:
        user_id = request.session['user_id']
        collection_paper = Collection.objects.filter(
            Q(user_id=user_id), Q(paper=paper)
        )
        if collection_paper:
            collection_paper.delete()
    return redirect(return_url)
