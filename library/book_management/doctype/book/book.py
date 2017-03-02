# -*- coding: utf-8 -*-
# Copyright (c) 2015, SBK and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Book(Document):
	def validate(self):
		frappe.msgprint("In Python")

	def onload(self):
		frappe.msgprint("In Python onload")

	def autoname(self):
		self.name = "SBK - " + self.book_name