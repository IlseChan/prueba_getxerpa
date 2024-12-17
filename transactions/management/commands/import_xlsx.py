import openpyxl
from django.core.management.base import BaseCommand
from transactions.models import Transaction
from datetime import datetime
import uuid

class Command(BaseCommand):
    help = 'Import transactions from an Excel file (.xlsx)'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                print(f"Row read: {row}")
                description = row[1] if row[1] else ""
                amount = row[2] if row[2] is not None else None
                date_str = row[3] if row[3] else None

               
                if date_str:
                    try:
                        date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Invalid date format in row: {row}"))
                        date = None
                else:
                    date = None

                
                Transaction.objects.create(
                    id=uuid.uuid4(),
                    description=description,
                    amount=amount,
                    date=date
                )

            self.stdout.write(self.style.SUCCESS('Successfully imported transactions from Excel'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing file: {e}'))
