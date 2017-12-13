

        if request.method == 'POST':

            date_begin = datetime.strptime(
                request.POST.get('date_begin', ''), date_format)
            date_end = datetime.strptime(
                request.POST.get('date_end', ''), date_format)
            lower_range = request.POST.get('lower_range', '')
            upper_range = request.POST.get('upper_range', '')

            samples = PressureSample.objects.filter(date_entry__range=(
                date_begin, date_end)).select_related('city').values('city__name', 'city')

            samples = samples.annotate(irregular_samples=Count(Case(When(Q(pressure_value__lte=lower_range) |
                                                                         Q(pressure_value__gte=upper_range),
                                                                         then=1,))),
                                                                         normal_samples=Count('city__name'),
                                                                         max_sample=Max('pressure_value'),
                                                                         min_sample=Min('pressure_value')).order_by('city__name')
 
            content.update({'samples': samples})
            return render(request, 'pressure/outstanding_samples.html', content)
        else:
            return render(request, 'pressure/outstanding_samples.html', content)