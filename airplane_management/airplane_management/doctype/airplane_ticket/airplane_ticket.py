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