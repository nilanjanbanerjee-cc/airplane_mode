# Copyright (c) 2026, Nilanjan Banerjee and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestShop(IntegrationTestCase):

	def test_shop_creation(self):
		shop = frappe.get_doc({
			"doctype": "Shop",
			"shop_name": "Test Airport -For testing",
			"shop_type": "Stall",
			"location": "Terminal 1",
			"size_sq_ft": 250,
			"status": "Available",
			"airport": "Netaji Subhas Chandra Bose International Airport"
		})

		shop.insert()

		self.assertEqual(shop.shop_name, "Test Airport -For testing")
		self.assertEqual(shop.shop_type, "Stall")
		self.assertEqual(shop.status, "Available")
