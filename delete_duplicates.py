import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba_getxerpa.settings')
django.setup()

from transactions.models import Keyword
from django.db.models import Count

duplicates = Keyword.objects.values('keyword', 'merchant').annotate(count=Count('id')).filter(count__gt=1)

for dup in duplicates:
    print(f"Eliminando duplicados de keyword: {dup['keyword']} y merchant: {dup['merchant']}")
    duplicates_to_delete = Keyword.objects.filter(
        keyword=dup['keyword'], merchant=dup['merchant']
    ).order_by('created_at')[1:] 

    for record in duplicates_to_delete:
        print(f"Eliminando registro: {record.id}")
        record.delete()

print("Duplicados eliminados correctamente.")
