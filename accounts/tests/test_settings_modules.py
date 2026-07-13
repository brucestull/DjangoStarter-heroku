from importlib import import_module, reload
from unittest.mock import patch

from django.test import SimpleTestCase


class SettingsModuleTests(SimpleTestCase):
    def test_dev_settings_use_debug_and_sqlite(self):
        dev_settings = import_module("config.settings.dev")

        self.assertTrue(dev_settings.DEBUG)
        self.assertEqual(
            dev_settings.DATABASES["default"]["ENGINE"],
            "django.db.backends.sqlite3",
        )

    def test_prod_settings_read_required_environment_values(self):
        database_url = (
            "postgres://"
            "db_user:"
            "db_pass@"
            "db.example.com:5432/"
            "db_name"
        )

        with patch.dict(
            "os.environ",
            {
                "THIS_HOST": "example.herokuapp.com",
                "SECRET_KEY": "prod-secret",
                "DATABASE_URL": database_url,
            },
            clear=False,
        ):
            prod_settings = reload(import_module("config.settings.prod"))

        self.assertFalse(prod_settings.DEBUG)
        self.assertEqual(prod_settings.ALLOWED_HOSTS, ["example.herokuapp.com"])
        self.assertEqual(prod_settings.SECRET_KEY, "prod-secret")
        self.assertEqual(
            prod_settings.DATABASES["default"]["ENGINE"],
            "django.db.backends.postgresql",
        )
        self.assertEqual(
            prod_settings.DATABASES["default"]["NAME"],
            "db_name",
        )
