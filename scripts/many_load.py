import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category,Iso,Region,Site,State

def run():
    fhand = open('scripts/whc-sites.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()
    State.objects.all().delete()

    # Format
    # name,description,justification,year,longitude,latitude,/
    # area_hectares,category,states,region,iso


    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        state, created = State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])
        site, created = Site.objects.get_or_create(
            name=row[0],
            year=row[3],
            state=state,
            category=cat,
            region=reg,
            iso=iso,
        )

        site.save()
