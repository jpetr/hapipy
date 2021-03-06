from hapi_plus.base import BaseClient
from urllib import quote

CONTACTS_API_VERSION = '1'


class ContactsClient(BaseClient):

    def _get_path(self, subpath):
        return 'contacts/v%s/%s' % (CONTACTS_API_VERSION, subpath)

    def get_contact(self, contact_id, **options):
        return self._call('contact/vid/%s/profile' % contact_id, **options)

    def get_contact_by_email(self, email, **options):
        return self._call('contact/email/%s/profile' % quote(email), **options)

    def create_contact(self, data, **options):
        return self._call('contact/', data=data, method='POST', **options)

    def update_contact(self, contact_id, data, **options):
        return self._call('contact/vid/%s/profile' % contact_id, data=data, method='POST', **options)

    def archive_contact(self, contact_id, **options):
        return self._call('contact/vid/%s' % contact_id, method='DELETE', **options)

    def get_statistics(self, **options):
        return self._call('contacts/statistics', **options)

    def search(self, query, properties=None, **options):
        params = {'q': query}

        if properties:
            params['property'] = properties

        return self._call('search/query', params, doseq=True, **options)
