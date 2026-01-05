from django.contrib import admin
from .models import HomeContent, Category, Product, AboutContent, WhyCard, ContactContent, ContactMessage, LegalPage, SiteSettings, FooterLinkGroup, FooterLink, ProductsPageContent

@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "updated_at")

    fieldsets = (
        ("Hero Section", {
            "fields": ("hero_title", "hero_subtitle", "hero_image")
        }),

        ("Best Sellers Heading", {"fields": ("bestseller_title", "bestseller_subtitle")}),

        ("Story Section", {
            "fields": (
                "story_title",
                "story_paragraph_1",
                "story_paragraph_2",
                "story_image",
            )
        }),
        ("CTA Section", {
            "fields": (
                "cta_title",
                "cta_text",
                "cta_image",
                "cta_button_label",
            )
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    ordering = ("order",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price_per_kg",
        "is_best_seller",
        "order",
        "whatsapp_number",
    )
    list_filter = ("category", "is_best_seller")
    search_fields = ("name",)
    ordering = ("order",)
    list_editable = ("price_per_kg", "is_best_seller", "order", "whatsapp_number")




class WhyCardInline(admin.TabularInline):
    model = WhyCard
    extra = 1
    fields = ("order", "icon", "title", "paragraph")
    ordering = ("order",)


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "updated_at")
    inlines = [WhyCardInline]
    fieldsets = (
        ("Hero", {"fields": ("hero_title", "hero_subtitle")}),
        ("Why Choose Us Heading", {"fields": ("why_choose_title", "why_choose_subtitle")}),
        ("Story", {"fields": ("story_heading", "story_paragraph_1", "story_paragraph_2", "story_image")}),
        ("CTA", {"fields": ("cta_title", "cta_text", "cta_button_label", "cta_button_url")}),
    )



@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "contact_phone", "contact_email", "updated_at")
    fieldsets = (
        ("Hero", {"fields": ("hero_title", "hero_subtitle")}),
        ("Best Sellers Heading", {"fields": ("bestseller_title", "bestseller_subtitle")}),
        ("Intro / Contact", {"fields": ("intro_heading", "intro_paragraph", "contact_phone", "contact_email", "contact_address", "image")}),
        ("CTA", {"fields": ("cta_title", "cta_text", "cta_button_label", "cta_button_url")}),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "handled")
    list_filter = ("handled", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)


@admin.register(LegalPage)
class LegalPageAdmin(admin.ModelAdmin):
    list_display = ("title", "page_type", "updated_at")
    list_filter = ("page_type",)
    search_fields = ("title",)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "phone_number", "updated_at")

    fieldsets = (
        ("Branding", {"fields": ("site_name", "logo_image")}),
        ("Contact Details", {"fields": ("phone_number", "email_address", "address_line")}),
        ("Copyright", {"fields": ("copyright_text",)}),
    )

    def has_add_permission(self, request):
        # Prevent creating more than one instance
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion
        return False


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1
    fields = ("order", "text", "url")
    ordering = ("order",)


@admin.register(FooterLinkGroup)
class FooterLinkGroupAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    ordering = ("order",)
    inlines = [FooterLinkInline]


@admin.register(ProductsPageContent)
class ProductsPageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevents creating multiple instances; only one "Settings" object allowed
        return not ProductsPageContent.objects.exists()