import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Copy media files to the public web directory (production deployment)'

    def handle(self, *args, **options):
        src = settings.MEDIA_ROOT
        dst = getattr(settings, 'MEDIA_PUBLIC', None)

        if not dst:
            self.stderr.write('MEDIA_PUBLIC is not defined in settings.')
            return

        if not os.path.exists(src):
            self.stderr.write(f'Source media folder not found: {src}')
            return

        os.makedirs(dst, exist_ok=True)

        copied = 0
        for root, dirs, files in os.walk(src):
            rel = os.path.relpath(root, src)
            target_dir = os.path.join(dst, rel)
            os.makedirs(target_dir, exist_ok=True)
            for file in files:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(target_dir, file)
                shutil.copy2(src_file, dst_file)
                copied += 1

        self.stdout.write(self.style.SUCCESS(
            f'{copied} file(s) copied from {src} to {dst}'
        ))
