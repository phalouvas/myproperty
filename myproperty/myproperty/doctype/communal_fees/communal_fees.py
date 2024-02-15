# Copyright (c) 2024, KAINOTOMO PH LTD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CommunalFees(Document):
	
	def before_save(self):
		self.monthly_fee = self.yearly_fee / 12
