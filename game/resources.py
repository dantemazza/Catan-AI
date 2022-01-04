from gameconfig import *

class BankNote:
    def __init__(self, start=0, ore=0, brick=0, wood=0, sheep=0, wheat=0):
        self.quantities = {
            "ore": start or ore,
            "brick": start or brick,
            "wood": start or wood,
            "sheep": start or sheep,
            "wheat": start or wheat
        }

    def get_resource(self, resource):
        return self.quantities[resource]

    def expend(self, resource, amount):
        if amount > self.get_resource(resource):
            raise AssertionError("Negative Resource Count")
        self.quantities[resource] -= amount

    def acquire(self, resource, amount):
        self.quantities[resource] += amount

    def print(self):
        for resource, amount in self.quantities.items():
            print(resource, amount)


class ResourceConsumer:
    def __init__(self, player=False):
        if not player:
            self.account = BankNote(start=TOTAL_RESOURCES)
        else:
            self.account = BankNote()

    def pay(self, payee, bank_note):
        for resource, amount in bank_note.items():
            subtract = min(amount, self.account.get_resource(resource))
            payee.acquire(resource, subtract)
            self.account.expend(resource, subtract)

    def print_resources(self):
        self.account.print()