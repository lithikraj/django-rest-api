from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import (
    Category,
    Product,
    HomeContent,
    AboutContent,
    ContactContent,
    LegalPage,
    ContactMessage,
    ProductsPageContent
)
from django.contrib import messages

def handle_contact_form(request, contact_content):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            messages.success(request, 'Thank you! Your message has been received and we will get back to you shortly.')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Please fill in all required fields (Name, Email, Message).')
            return render(request, "nellore_maha_ruchulu_app/contact.html", {
                "contact": contact_content,
                "best_sellers": Product.objects.filter(is_best_seller=True).order_by("order")[:8],
            })

    return None


def home(request):

    home_content = HomeContent.objects.first()
    categories = Category.objects.all().order_by("order")
    best_sellers = Product.objects.filter(is_best_seller=True).order_by("order")

    context = {
        # Added this line so index.html can access bestseller_title and bestseller_subtitle
        "home": home_content, 

        "hero_title": getattr(home_content, "hero_title", None),
        "hero_subtitle": getattr(home_content, "hero_subtitle", None),
        "hero_image": getattr(home_content, "hero_image", None),

        "story_title": getattr(home_content, "story_title", None),
        "story_paragraph_1": getattr(home_content, "story_paragraph_1", None),
        "story_paragraph_2": getattr(home_content, "story_paragraph_2", None),
        "story_image": getattr(home_content, "story_image", None),

        "cta_title": getattr(home_content, "cta_title", None),
        "cta_text": getattr(home_content, "cta_text", None),
        "cta_image": getattr(home_content, "cta_image", None),
        "cta_button_label": getattr(home_content, "cta_button_label", None),

        "categories": categories,
        "best_sellers": best_sellers,
    }
    return render(request, "nellore_maha_ruchulu_app/index.html", context)


def products(request):
    # Fetch the dynamic content for the page
    products_page = ProductsPageContent.objects.first()
    
    categories = Category.objects.all()
    selected_category_slug = request.GET.get('category')
    products_queryset = Product.objects.all()

    if selected_category_slug and selected_category_slug != 'all':
        try:
            selected_category = Category.objects.get(
                name__iexact=selected_category_slug.replace('-', ' ')
            )
            products_queryset = products_queryset.filter(category=selected_category)
        except Category.DoesNotExist:
            pass
            
    context = {
        'products_page': products_page, # This is the dynamic content variable
        'categories': categories,
        'products': products_queryset,
        'initial_category_slug': selected_category_slug,
    }

    return render(request, 'nellore_maha_ruchulu_app/products.html', context)


def about(request):

    about_content = AboutContent.objects.first()
    why_cards = about_content.why_cards.all().order_by("order") if about_content else []

    context = {
        "about": about_content, # Already exists, covers why_choose_title/subtitle
        "why_cards": why_cards,
    }
    return render(request, "nellore_maha_ruchulu_app/about.html", context)


def contact(request):

    contact_content = ContactContent.objects.first()
    best_sellers = Product.objects.filter(is_best_seller=True).order_by("order")[:8]


    form_response = handle_contact_form(request, contact_content)
    if form_response:
        return form_response

   
    context = {
        "contact": contact_content, # Already exists, covers bestseller_title/subtitle
        "best_sellers": best_sellers,
    }
    return render(request, "nellore_maha_ruchulu_app/contact.html", context)


def legal_page(request, page_type):

    page = get_object_or_404(LegalPage, page_type=page_type)

    context = {
        "page": page
    }
    return render(request, "nellore_maha_ruchulu_app/legal_page.html", context)