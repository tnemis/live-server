from django.contrib.auth.models import User
class RecipientsLookup(ModelLookup):
    model = User
    search_fields = ('username__icontains','group__icontains' )
registry.register(RecipientsLookup)