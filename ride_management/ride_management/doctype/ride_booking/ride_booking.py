# Copyright (c) 2024, Dipak and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def calculate_data(self):
		total_amount_data = 0
		for data in self.services:
			data.amount+=total_amount_data
		self.total_amount= total_amount_data+self.price_per_km+self.estimated_km
		
		
