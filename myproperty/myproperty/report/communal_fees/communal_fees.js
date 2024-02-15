// Copyright (c) 2024, KAINOTOMO PH LTD and contributors
// For license information, please see license.txt

frappe.query_reports["Communal Fees"] = {
	"filters": [
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"reqd": 1
		},
		{
			"fieldname": "year",
			"label": __("Year"),
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"reqd": 1
		}
	]
};
