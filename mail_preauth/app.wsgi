import os, sys
sys.path.append('/opt/mail_preauth/mail_preauth/mail_preauth')
sys.path.append('/opt/mail_preauth/mail_preauth/venv/lib/python2.7/site-packages')
activate_env=os.path.expanduser('/opt/mail_preauth/mail_preauth/venv/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))
from app import app as application
