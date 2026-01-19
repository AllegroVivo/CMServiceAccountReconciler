from __future__ import annotations

from typing import List, Dict, Optional

from .Classes import *
from Database import UnitOfWork
from Utilities import Utilities as U
################################################################################

__all__ = ("RoutingRuleManager", )

################################################################################
class RoutingRuleManager:

    __slots__ = (
        "rules",
    )

################################################################################
    def __init__(self) -> None:

        self.rules: List[SheetRoutingRuleRead] = []
        self.refresh()

################################################################################
    def refresh(self) -> None:

        with UnitOfWork() as db:
            self.rules = db._rules.list_all()

################################################################################
    def list_rules(self) -> List[SheetRoutingRuleRead]:

        return self.rules.copy()

################################################################################
    def create_rule(self, rule: SheetRoutingRuleWrite) -> SheetRoutingRuleRead:

        if any(r.name == rule.name for r in self.rules):
            raise ValueError(f"Rule with name '{rule.name}' already exists.")

        with UnitOfWork() as db:
            new_rule = db._rules.add(rule)

        self.rules.append(new_rule)
        return new_rule

################################################################################
    def update_rule(self, rule_id: int, data: Dict) -> SheetRoutingRuleRead:

        if "name" in data:
            n = str(data["name"])
            if any(r.name == n for r in self.rules if r.id != rule_id):
                raise ValueError(f"Rule with name '{n}' already exists.")

        with UnitOfWork() as db:
            updated_rule = db._rules.update(rule_id, data)

        for idx, r in enumerate(self.rules):
            if r.id == rule_id:
                self.rules[idx] = updated_rule
                break

        return updated_rule

################################################################################
    def delete_rule(self, rule_id: int) -> None:

        assert any(r.id == rule_id for r in self.rules)

        with UnitOfWork() as db:
            db._rules.remove(rule_id)

        self.rules = [r for r in self.rules if r.id != rule_id]

################################################################################
    def add_rule(self) -> None:

        print("\nAdding a new Interpretation Threshold:")
        name = input("Enter threshold name: ").strip()
        if any((t.name == name for t in self.rules)):
            print(f"Threshold with name '{name}' already exists. Please choose a different name.")
            return

        min_val = input("Enter minimum value: ")
        success, min_parsed = U.make_numeric(min_val)
        if not success:
            print("Invalid format for minimum value. Threshold not added.")
            return

        max_val = input("Enter maximum value: ")
        success, max_parsed = U.make_numeric(max_val)
        if not success:
            print("Invalid format for maximum value. Threshold not added.")
            return

        print(
            "Select the sheet this threshold applies to:\n"
            "1. Annual\n"
            "2. Monthly\n"
            "3. Plumbing\n"
            "4. Generator\n"
            "5. Duct Cleaning\n"
            "0. Cancel\n"
        )
        sheet_choice = input("Enter your choice: ")
        if sheet_choice == "0":
            return
        if sheet_choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid sheet choice. Threshold not added.")
            return

        sheet_choice = int(sheet_choice)
        sheet_map = U.get_sheet_map()

        rule = SheetRoutingRuleWrite(
            name=name,
            sheet=sheet_map[sheet_choice],
            min_amount=min_parsed,
            max_amount=max_parsed
        )

        with UnitOfWork() as db:
            new_rule = db._rules.add(rule)
        self.rules.append(new_rule)

        print(f"Threshold '{name}' (${min_parsed}-${max_parsed}) added successfully.")

################################################################################
    def list_edit_rules(self) -> None:

        if not self.rules:
            print("\nNo Interpretation Thresholds found.")
            return

        while True:
            print("\nInterpretation Thresholds:")
            rule_dict: Dict[int, SheetRoutingRuleRead] = {}
            for idx, rule in enumerate(self.rules, start=1):
                print(
                    f"{idx}. Name: {rule.name}, "
                    f"Min: ${rule.min_amount}, "
                    f"Max: ${rule.max_amount}, "
                    f"Routes to Sheet: '{rule.sheet}'"
                )
                rule_dict[idx] = rule

            choice = input(
                "\nEnter the number of the threshold to edit, "
                "or press Enter to return to the previous menu: "
            ).strip()
            if not choice:
                return
            if not choice.isdigit():
                print("Invalid input. Returning to previous menu.")
                return

            choice_idx = int(choice)
            if choice_idx not in rule_dict:
                print("Invalid threshold number. Returning to previous menu.")
                return
            rule_to_edit = rule_dict[choice_idx]

            print(
                f"\nEditing Threshold '{rule_to_edit.name}':\n"
                "1. Edit Name\n"
                "2. Edit Minimum Value\n"
                "3. Edit Maximum Value\n"
                "4. Edit Linked Sheet\n"
                "0. Cancel\n"
            )
            edit_choice = input("Enter your choice: ").strip()
            if edit_choice not in {"1", "2", "3", "4", "0"}:
                print("Invalid choice. Returning to previous menu.")
                return

            data = {}
            match int(edit_choice):
                case 0:
                    return
                case 1:
                    new_name = input("Enter new threshold name: ").strip()
                    if any((t.name == new_name for t in self.rules if t.id != rule_to_edit.id)):
                        print(f"Threshold with name '{new_name}' already exists. Name not changed.")
                        return
                    data = {"name": new_name}
                case 2:
                    candidate = input("Enter new minimum value: ").strip()
                    success, min_parsed = U.make_numeric(candidate)
                    if not success:
                        print("Invalid format for minimum value. Minimum not changed.")
                        return
                    data = {"min_amount": min_parsed}
                case 3:
                    candidate = input("Enter new maximum value: ").strip()
                    success, max_parsed = U.make_numeric(candidate)
                    if not success:
                        print("Invalid format for maximum value. Maximum not changed.")
                        return
                    data = {"max_amount": max_parsed}
                case 4:
                    print(
                        "Select the new sheet this threshold applies to:\n"
                        "1. Annual\n"
                        "2. Monthly\n"
                        "3. Plumbing\n"
                        "4. Generator\n"
                        "5. Duct Cleaning\n"
                        "0. Cancel\n"
                    )
                    sheet_choice = input("Enter your choice: ").strip()
                    if sheet_choice == "0":
                        return
                    if sheet_choice not in {"1", "2", "3", "4", "5"}:
                        print("Invalid sheet choice. Linked sheet not changed.")
                        return

                    sheet_map = U.get_sheet_map()
                    sheet_choice = int(sheet_choice)
                    data = {"sheet": sheet_map[sheet_choice]}
                case _:
                    raise ValueError("Unreachable code reached in RoutingRuleManager.list_edit_rules")

            with UnitOfWork() as db:
                new_rule = db._rules.update(rule_to_edit.id, data)

            # Update in-memory
            for idx, r in enumerate(self.rules):
                if r.id == rule_to_edit.id:
                    self.rules[idx] = new_rule
                    break

################################################################################
    def remove_rule(self) -> None:

        if not self.rules:
            print("\nNo Interpretation Thresholds found.")
            return

        while True:
            print("\nInterpretation Thresholds:")
            rule_dict: Dict[int, SheetRoutingRuleRead] = {}
            for idx, rule in enumerate(self.rules, start=1):
                print(
                    f"{idx}. Name: {rule.name}, "
                    f"Min: ${rule.min_amount}, "
                    f"Max: ${rule.max_amount}, "
                    f"Routes to Sheet: '{rule.sheet}'"
                )
                rule_dict[idx] = rule

            choice = input(
                "\nEnter the number of the threshold to remove, "
                "or press Enter to return to the previous menu: "
            ).strip()
            if not choice:
                return
            if not choice.isdigit():
                print("Invalid input. Returning to previous menu.")
                return

            choice_idx = int(choice)
            if choice_idx not in rule_dict:
                print("Invalid threshold number. Returning to previous menu.")
                return
            rule_to_remove = rule_dict[choice_idx]

            while True:
                confirm = input(
                    f"Are you sure you want to remove the threshold '{rule_to_remove.name}'? (y/n): "
                ).strip().lower()
                if confirm not in {"y", "n"}:
                    continue
                if confirm == "n":
                    print("Removal cancelled. Returning to previous menu.")
                    return

                with UnitOfWork() as db:
                    db._rules.remove(rule_to_remove.id)

                # Update in-memory
                self.rules = [r for r in self.rules if r.id != rule_to_remove.id]

                print(f"Threshold '{rule_to_remove.name}' removed successfully.")
                break

################################################################################
    def get_target_sheet(self, record: QBServiceRecord) -> Optional[str]:

        return next(
            (rule.sheet for rule in self.rules if rule.matches(record)),
            "Monthly"
        )

################################################################################
