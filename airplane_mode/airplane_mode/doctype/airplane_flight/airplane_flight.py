# Copyright (c) 2026, Nilanjan Banerjee and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


def update_ticket_gates(flight_name, gate_number):
    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={
            "flight": flight_name
        },
        pluck="name"
    )

    frappe.log_error(
        message=f"Tickets found: {tickets}",
        title="Gate Update Debug"
    )

    for ticket in tickets:
        frappe.db.set_value(
            "Airplane Ticket",
            ticket,
            "gate_number",
            gate_number
        )

    # CRITICAL: Background jobs require an explicit commit to save db changes
    frappe.db.commit()


class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.db_set("status", "Completed")

    def on_update_after_submit(self):
        if self.has_value_changed("gate_number"):
            frappe.log_error(
                message=f"Gate changed to: {self.gate_number}",
                title="Gate Update Trigger Debug"
            )

            frappe.enqueue(
                "airplane_mode.airplane_mode.doctype.airplane_flight.airplane_flight.update_ticket_gates",
                flight_name=self.name,
                gate_number=self.gate_number,
                queue="short"
            )
			
			