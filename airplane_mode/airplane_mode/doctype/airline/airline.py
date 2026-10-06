# Copyright (c) 2026, Nilanjan Banerjee and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class Airline(Document):
	def validate(self):
		if self.customer_care_number:	
			if len(self.customer_care_number) < 10:
				frappe.throw("Customer care number must be at least 10 digits long.")
			if self.customer_care_number and not self.customer_care_number.isdigit():
				frappe.throw("Customer care number must contain only digits.")	
