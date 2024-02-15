# Copyright (c) 2024, KAINOTOMO PH LTD and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Name"),
			"fieldtype": "Link",
			"fieldname": "customer",
			"options": "Customer",
			"width": 300,
		},	
		{"label": _("Monthly"), "fieldtype": "Currency", "fieldname": "monthly_fee", "width": 150},
		{"label": _("Yearly"), "fieldtype": "Currency", "fieldname": "yearly_fee", "width": 150},
	]


def get_data(filters):
	data = []
	
	communal_fees = frappe.get_all("Communal Fees", filters, ["customer", "monthly_fee", "yearly_fee"])
	for fee in communal_fees:
		data.append(
			{
				"customer": fee.customer,
				"monthly_fee": fee.monthly_fee,
				"yearly_fee": fee.yearly_fee
			}
		)

	return data

