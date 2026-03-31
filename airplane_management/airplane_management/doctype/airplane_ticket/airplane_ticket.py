# Copyright (c) 2026, Samiul Sakib and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname
import random


class AirplaneTicket(WebsiteGenerator):
	def autoname(self):
		# if not self.flight or not self.source_airport or not self.destination_airport:
		# 	frappe.throw("Flight, Source Airport, and Destination Airport are required to generate the name")
		
		source_code = self.source_airport_code
		dest_code = self.destination_airport_code
		
		key = f"{self.flight}-{source_code}-to-{dest_code}-"
		# Generate sequence per  airplane + route
		self.name = make_autoname(key + ".###")
	

	def validate(self):
		self.remove_duplicate_add_ons()
		self.get_total_amount()
  
	def remove_duplicate_add_ons(self):
		unique = []
		seen = set()
		duplicates_removed = False

		for row in self.add_ons:
			if row.item not in seen:
				unique.append(row)
				seen.add(row.item)
			else:
				duplicates_removed = True

		self.set("add_ons", unique)

		if duplicates_removed:
			frappe.msgprint("Duplicate Add-ons removed.")
  
	def get_total_amount(self):
		total_add_ons = sum([row.amount for row in self.add_ons if row.amount])
     
		self.total_amount =  (self.flight_price or 0) + total_add_ons