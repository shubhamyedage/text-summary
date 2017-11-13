"""
This module creates and saves files.
"""

import os
from random import choice
from string import ascii_letters
import cloudstorage
from google.appengine.api import app_identity

cloudstorage.set_default_retry_params(
        cloudstorage.RetryParams(
            initial_delay=0.2, max_delay=5.0, backoff_factor=2,
            max_retry_period=15
        ))


class FileUtils:
    # Create a file.
    def create_file(self, data):
        bucket_name = os.environ.get(
            "precise-ego-185409.appspot.com",
            app_identity.get_default_gcs_bucket_name()
        )
        bucket = '/' + bucket_name
        file_name = ''.join(choice(ascii_letters) for _ in range(16))
        file_name = bucket + '/{}'.format(file_name)
        # The retry_params specified in the open call will override the default
        # retry params for this particular file handle.
        write_retry_params = cloudstorage.RetryParams(backoff_factor=1.1)
        with cloudstorage.open(
                file_name, 'w', content_type="text/plain",
                options={"x-goog-meta-foo": "foo", "x-goog-meta-bar": "bar"},
                retry_params=write_retry_params) as cloudstorage_file:
            cloudstorage_file.write(data)
