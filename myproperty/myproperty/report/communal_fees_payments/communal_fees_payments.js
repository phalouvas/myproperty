// Copyright (c) 2024, KAINOTOMO PH LTD and contributors
// For license information, please see license.txt

frappe.query_reports["Communal Fees Payments"] = {
	"filters": [
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"reqd": 1
		},
		{
			"fieldname": "posting_date",
			"label": __("Dates"),
			"fieldtype": "DateRange",
			"reqd": 0
		},
		{
			"fieldname": "payment_type",
			"label": __("Payment Type"),
			"fieldtype": "Select",
			"options": "Receive\nPay\nInternal Transfer",
			"reqd": 1,
			"default": "Receive"
		}
	]
};
