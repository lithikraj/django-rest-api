# nellore_maha_ruchulu_app/context_processors.py

from .models import SiteSettings, FooterLinkGroup

def site_data(request):
    """
    Context processor that adds SiteSettings and FooterLinkGroup data to every template context.
    """
    try:
        # Get the single instance of SiteSettings
        settings = SiteSettings.objects.get(pk=1)
    except SiteSettings.DoesNotExist:
        # Provide sensible defaults or None if not created yet
        settings = None

    # Fetch all footer link groups and their related links
    footer_groups = FooterLinkGroup.objects.prefetch_related('links').all()

    return {
        'SITE_SETTINGS': settings,
        'FOOTER_GROUPS': footer_groups,
    }