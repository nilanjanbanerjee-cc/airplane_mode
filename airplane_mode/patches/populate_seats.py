import frappe
import random


def execute():
    tickets = frappe.get_all("Airplane Ticket", pluck="name")
    for ticket in tickets:
        if not ticket.seat:
            seat = f"{random.randint(1, 100)}{random.choice('ABCDE')}"
            frappe.db.set_value("Airplane Ticket", ticket, "seat", seat)