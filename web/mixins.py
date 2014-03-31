class SearchMixin(object):
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return self.model.objects.filter(title__icontains=q)
        return self.model.objects.all()