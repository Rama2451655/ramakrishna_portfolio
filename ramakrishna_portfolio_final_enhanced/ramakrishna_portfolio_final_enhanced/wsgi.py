import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ramakrishna_portfolio_final_enhanced.settings')
application = get_wsgi_application()
