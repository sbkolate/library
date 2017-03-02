from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

def update_publishing_date(self, method):
	frappe.msgprint("In Python - update_publishing_date")

	if self.status == "Open":
		self.priority = "High"
	else:
		self.priority = "Low"