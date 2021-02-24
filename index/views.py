from django.shortcuts import render, redirect
# from django.views.generic import TemplateView, ListView
from users.models import UserProfile
from django.contrib.auth.decorators import login_required
# from .models import Post
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from collections import Counter
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post


# Create your views here.
def Index(request):
    address = UserProfile.objects.values('address')
    ad_list = []  # list of all addresses

    for i in address:
        ad_list.append(i['address'])

    num_uniq_address = len(Counter(ad_list))  # Total unique address
    n = Counter(ad_list)  # unique address info
    aoo = []
    for i in range(len(n)):
        aoo.append(list(n.values())[i])

    # print(n)

    if request.method == 'POST':
        data = request.POST
        i_d = request.user.id
        blood_group = data.get('blood')
        location = data.get('location')
        hospital = data.get('hospital')
        contact = data.get('contact')
        details = data.get('details')

        post = Post(user_id=i_d, blood_group=blood_group, location=location,
                    hospital=hospital, contact=contact, details=details)
        post.save()
        # print(post)
        context = {
            'details': details
        }
        # return JsonResponse(context, safe=False)
        return redirect('home')

    all_posts = Post.objects.all()

    context = {
        'uniq_address': num_uniq_address,
        'info': n,
        'add_list': aoo,

        'posts': all_posts
    }

    # return JsonResponse(context, safe=False)
    return render(request, 'base/index.html', context)
