from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import Service, GalleryItem, Expert, Partner, Reservation, CustomUser

# Create your views here.

def home(request):
    services = Service.objects.all()
    gallery_items = GalleryItem.objects.all()
    experts = Expert.objects.all()
    partners = Partner.objects.all()
    
    context = {
        'services': services,
        'gallery_items': gallery_items,
        'experts': experts,
        'partners': partners,
    }
    return render(request, 'index.html', context)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'success': True,
                'user_type': user.user_type,
                'has_new_messages': False  # Implémentez la logique des messages plus tard
            })
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True})

from django.contrib.auth.decorators import login_required, user_passes_test

def is_special_user(user):
    return user.user_type == 'special'

@login_required
@user_passes_test(is_special_user)
def partner_admin(request):
    # Logique pour la page d'administration des partenaires
    return render(request, 'main/partner_admin.html')

from django.contrib.auth.decorators import login_required

@login_required
@csrf_exempt
def reserve_service(request):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        message = request.POST.get('message')
        service = Service.objects.get(id=service_id)
        reservation = Reservation.objects.create(
            user=request.user,
            service=service,
            message=message
        )
        return JsonResponse({'success': True, 'reservation_id': reservation.id})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

from django.contrib.auth.decorators import user_passes_test

def is_partner(user):
    return user.user_type in ['special', 'admin']

@user_passes_test(is_partner)
@csrf_exempt
def add_service(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        service = Service.objects.create(
            title=title,
            description=description,
            price=price,
            image=image
        )
        return JsonResponse({'success': True, 'service_id': service.id})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
