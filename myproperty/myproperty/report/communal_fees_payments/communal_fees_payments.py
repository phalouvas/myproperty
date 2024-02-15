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
			"label": _("Party"),
			"fieldtype": "data",
			"fieldname": "party",
			"width": 300,
		},
		{
			"label": _("Mode of Payment"),
			"fieldtype": "data",
			"fieldname": "mode_of_payment",
			"width": 200,
		},	
		{
			"label": _("Date"),
			"fieldtype": "date",
			"fieldname": "posting_date",
			"width": 150,
		},
		{"label": _("Paid Amount"), "fieldtype": "Currency", "fieldname": "paid_amount", "width": 150},
	]


def get_data(filters):

	new_filters = []
	if filters.get("company"):
		new_filters.append(['company', '=', filters["company"]])
	if filters.get("mode_of_payment"):
		new_filters.append(['mode_of_payment', '=', filters["mode_of_payment"]])
	if filters.get("posting_date"):
		new_filters.append(['posting_date', 'between', [filters["posting_date"][0], filters["posting_date"][1]]])

	data = []
	
	communal_fees = frappe.get_all("Payment Entry", new_filters, ["party", "mode_of_payment", "posting_date", "paid_amount"])
	for fee in communal_fees:
		data.append(
			{
				"party": fee.party,
				"mode_of_payment": fee.mode_of_payment,
				"posting_date": fee.posting_date,
				"paid_amount": fee.paid_amount
			}
		)

	return data

