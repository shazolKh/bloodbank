from django.shortcuts import render, redirect
from users.models import UserProfile
from collections import Counter
from django.core.paginator import Paginator
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

    all_posts = Post.objects.all().order_by('-id')
    paginator = Paginator(all_posts, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'uniq_address': num_uniq_address,
        'info': n,
        'add_list': aoo,
        'page_obj': page_obj,
    }

    # return JsonResponse(context, safe=False)
    return render(request, 'base/index.html', context)


def Managed(request, pk):
    if request.method == 'POST':
        managed = request.POST.get('managed')
        Post.objects.filter(id=pk).update(managed=managed)
        return redirect('home')


def Write_Blog(request):
    return render(request, 'blog/write_post.html')
