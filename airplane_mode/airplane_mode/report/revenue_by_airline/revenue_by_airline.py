# Copyright (c) 2026, Nilanjan Banerjee and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()

	total_revenue = sum(row[1] for row in data)

	report_summary = [
		{
			"label": _("Total Revenue"),
			"value": total_revenue,
			"datatype": "Currency",
		}
	]

	chart = {
		"data": {
			"labels": [row[0] for row in data],
			"datasets": [
				{
					"name": _("Revenue"),
					"values": [row[1] for row in data],
				}
			],
		},
		"type": "donut",
	}

	return columns, data, None, chart, report_summary

def execute_snapshot_report(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for snapshot report. When 'Synced
	Report' is enabled in report, framework will call this method
	every time the report is refreshed or a filter is updated. It
	accepts the same filters as normal execute. But a utility method -
	get_latest_sync, is also imported.

	"""
	from frappe.database.duckdb.database import get_latest_sync

	columns = get_columns()
	data = get_data()

	return columns, data

def get_columns() -> list[dict]:
	return [
		{
			"label": _("Airline"),
			"fieldname": "airline",
			"fieldtype": "Link",
			"options": "Airline",
		},
		{
			"label": _("Revenue"),
			"fieldname": "revenue",
			"fieldtype": "Currency",
		},
	]


def get_data() -> list[list]:
	airlines = frappe.get_all(
		"Airline",
		pluck="name"
	)

	data = []

	for airline in airlines:
		airplanes = frappe.get_all(
			"Airplane",
			filters={
				"airline": airline
			},
			pluck="name"
		)
		flights = frappe.get_all(
			"Airplane Flight",
			filters={
			"airplane": ["in", airplanes]
			},
			pluck="name"
		)
		tickets = frappe.get_all(
			"Airplane Ticket",
			filters={
				"flight": ["in", flights],
				"docstatus": 1
			},
			fields=["total_amount"]
		)
		revenue = sum(ticket.total_amount for ticket in tickets)
		data.append([airline, revenue])

	return data
