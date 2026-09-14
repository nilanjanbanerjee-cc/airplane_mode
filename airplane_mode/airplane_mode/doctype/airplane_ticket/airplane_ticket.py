# Copyright (c) 2026, Nilanjan Banerjee and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random


class AirplaneTicket(Document):
	def validate(self):
		unique_items = set()
		unique_add_ons = []
		for add_on in self.add_ons:
			if add_on.item not in unique_items:
				unique_items.add(add_on.item)
				unique_add_ons.append(add_on)

		self.add_ons = unique_add_ons
		add_on_sum = sum(add_on.amount for add_on in self.add_ons)
		self.total_amount = self.flight_price + add_on_sum

	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("Status must be 'Boarded'.")	

	def before_insert(self):
		self.seat = f"{random.randint(1, 100)}{random.choice('ABCDE')}"	

				