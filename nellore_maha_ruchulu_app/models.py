from django.db import models
from tinymce.models import HTMLField


class HomeContent(models.Model):
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.CharField(max_length=300, blank=True)
    hero_image = models.ImageField(upload_to="home/hero/", blank=True, null=True)

    story_title = models.CharField(max_length=200, blank=True)
    story_paragraph_1 = models.TextField(blank=True)
    story_paragraph_2 = models.TextField(blank=True)
    story_image = models.ImageField(upload_to="home/story/", blank=True, null=True)

    bestseller_title = models.CharField(max_length=200, blank=True, default="Our Best Sellers")
    bestseller_subtitle = models.TextField(blank=True, default="Tried, loved, and reordered. Here are the top picks our customers can’t get enough of.")


    cta_title = models.CharField(max_length=200, blank=True)
    cta_text = models.TextField(blank=True)
    cta_image = models.ImageField(upload_to="home/cta/", blank=True, null=True)
    cta_button_label = models.CharField(
        max_length=100,
        blank=True,
        default="View all Products →",
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Home Page Content"
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=150)
    price_per_kg = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    is_best_seller = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    whatsapp_number = models.CharField(
        max_length=20,
        blank=True,
        default="9618500442",
        help_text="WhatsApp number, e.g. 9618500442",
    )

    whatsapp_message = models.CharField(
        max_length=255,
        blank=True,
        help_text="Pre-filled WhatsApp message. If empty, a default based on product name will be used.",
    )

    def __str__(self):
        return self.name

    def get_whatsapp_message(self):

        if self.whatsapp_message:
            return self.whatsapp_message
        return f"I wanna buy this {self.name}"
    
class ProductsPageContent(models.Model):
    hero_title = models.CharField(max_length=200, blank=True, default="Explore Our Products")
    hero_subtitle = models.CharField(
        max_length=300, 
        blank=True, 
        default="Discover everything we make with care, love, and authentic Andhra taste."
    )
    sidebar_heading = models.CharField(max_length=100, blank=True, default="Categories")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Products Page Content"
        verbose_name_plural = "Products Page Content"

    def __str__(self):
        return "Products Page Content"


class AboutContent(models.Model):
    hero_title = models.CharField(max_length=200, blank=True, default="About Nellore Maharuchulu")
    hero_subtitle = models.CharField(max_length=300, blank=True, default="Bringing the flavors of Andhra’s kitchens to your home.")

    story_heading = models.CharField(max_length=200, blank=True)
    story_paragraph_1 = models.TextField(blank=True)
    story_paragraph_2 = models.TextField(blank=True)
    story_image = models.ImageField(upload_to="about/story/", blank=True, null=True)

    why_choose_title = models.CharField(max_length=200, blank=True, default="Why Choose Us")
    why_choose_subtitle = models.TextField(blank=True, default="At Nellore Maharuchulu, we don’t just make food — we preserve tradition. Every item is prepared with care, just like it’s done in Andhra homes. Here’s what makes us special:")

    cta_title = models.CharField(max_length=200, blank=True, default="Ready to Taste the Tradition?")
    cta_text = models.TextField(blank=True)
    cta_button_label = models.CharField(max_length=100, blank=True, default="View all Products →")
    cta_button_url = models.CharField(max_length=255, blank=True, default="/products/")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return "About Page Content"


class WhyCard(models.Model):

    about = models.ForeignKey(AboutContent, related_name="why_cards", on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    paragraph = models.TextField(blank=True)
    icon = models.ImageField(upload_to="about/icons/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order",)
        verbose_name = "Why Card"
        verbose_name_plural = "Why Cards"

    def __str__(self):
        return f"{self.title}"


class ContactContent(models.Model):

    hero_title = models.CharField(max_length=200, blank=True, default="Contact Us")
    hero_subtitle = models.CharField(
        max_length=300, blank=True,
        default="We’d love to hear from you — whether it’s for orders, feedback, or questions about our products."
    )

    intro_heading = models.CharField(max_length=200, blank=True, default="We’re Just a Message Away")
    intro_paragraph = models.TextField(blank=True)

    contact_phone = models.CharField(max_length=50, blank=True, default="+91 89657 56562")
    contact_email = models.EmailField(blank=True, default="info@nelloremaharuchulu.com")
    contact_address = models.CharField(max_length=255, blank=True, default="Nellore, Andhra Pradesh")
    image = models.ImageField(upload_to="contact/", blank=True, null=True)

    bestseller_title = models.CharField(max_length=200, blank=True, default="Our Best Sellers")
    bestseller_subtitle = models.TextField(blank=True, default="Tried, loved, and reordered — top picks customers can’t get enough of.")

    cta_title = models.CharField(max_length=200, blank=True, default="Ready to Taste the Tradition?")
    cta_text = models.TextField(blank=True)
    cta_button_label = models.CharField(max_length=100, blank=True, default="View all Products →")
    cta_button_url = models.CharField(max_length=255, blank=True, default="/products/")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Page Content"
        verbose_name_plural = "Contact Page Content"

    def __str__(self):
        return "Contact Page Content"


class ContactMessage(models.Model):

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.created_at:%Y-%m-%d %H:%M}"




class LegalPage(models.Model):
    PAGE_CHOICES = [
        ("refund", "Refund Policy"),
        ("terms", "Terms & Conditions"),
        ("privacy", "Privacy Policy"),
    ]

    page_type = models.CharField(
        max_length=20,
        choices=PAGE_CHOICES,
        unique=True
    )
    title = models.CharField(max_length=200)
    content = HTMLField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Legal Page"
        verbose_name_plural = "Legal Pages"

    def __str__(self):
        return self.title




class SiteSettings(models.Model):

    site_name = models.CharField(max_length=100, default="Nellore Maharuchulu")
    logo_image = models.ImageField(upload_to="site/", blank=True, null=True,
                                   help_text="Logo used in Navbar and Footer.")
    phone_number = models.CharField(max_length=20, default="+91 89657 56562",
                                    help_text="Contact number for Navbar/Footer.")
    email_address = models.EmailField(blank=True, default="info@nelloremaharuchulu.com")
    address_line = models.CharField(max_length=150, blank=True, default="Nellore, Andhra Pradesh")
    copyright_text = models.CharField(max_length=200, default="All Rights reserved Lagran.in")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings (Navbar/Footer)"
        verbose_name_plural = "Site Settings (Navbar/Footer)"

    def __str__(self):
        return "Global Site Settings"


class FooterLinkGroup(models.Model):

    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order", "title")
        verbose_name = "Footer Link Group"
        verbose_name_plural = "Footer Link Groups"

    def __str__(self):
        return self.title


class FooterLink(models.Model):

    group = models.ForeignKey(FooterLinkGroup, related_name="links", on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    url = models.CharField(max_length=255, help_text="The URL path (e.g., /products/ or a Django URL name)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order", "text")
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"

    def __str__(self):
        return f"{self.text} under {self.group.title}"
