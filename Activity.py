class ActivityNode:
    def __init__(self, duration, activity_type):
        self.duration = duration
        self.activity_type = activity_type
        self.left = None
        self.right = None


class ActivityBST:
    def __init__(self):
        self.root = None

    def add_activity(self, duration, activity_type):
        new_node = ActivityNode(duration, activity_type)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.duration < current.duration:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    def delete_activity(self, duration):
        self.root = self._delete(self.root, duration)

    def _delete(self, current, duration):
        if current is None:
            return current
        if duration < current.duration:
            current.left = self._delete(current.left, duration)
        elif duration > current.duration:
            current.right = self._delete(current.right, duration)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            temp = self._find_min(current.right)
            current.duration = temp.duration
            current.activity_type = temp.activity_type
            current.right = self._delete(current.right, temp.duration)
        return current

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search_activity(self, duration=None, activity_type=None):
        results = []
        self._search(self.root, duration, activity_type, results)
        return results

    def _search(self, current, duration, activity_type, results):
        if current is not None:
            if (duration is None or current.duration == duration) and \
               (activity_type is None or current.activity_type == activity_type):
                results.append((current.duration, current.activity_type))
            self._search(current.left, duration, activity_type, results)
            self._search(current.right, duration, activity_type, results)

    def generate_statistics(self):
        stats = {"total_activities": 0, "total_duration": 0}
        self._gather_stats(self.root, stats)
        return stats

    def _gather_stats(self, current, stats):
        if current is not None:
            stats["total_activities"] += 1
            stats["total_duration"] += current.duration
            self._gather_stats(current.left, stats)
            self._gather_stats(current.right, stats)


def main():
    activity_tree = ActivityBST()

    while True:
        print("\n--- Sports Activity Tracker ---")
        print("1. Add Activity")
        print("2. Delete Activity")
        print("3. Search Activity")
        print("4. View Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                duration = int(input("Enter activity duration (in minutes): "))
                activity_type = input("Enter activity type (e.g., Running, Cycling): ").strip()
                activity_tree.add_activity(duration, activity_type)
                print("Activity added successfully!")
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == "2":
            try:
                duration = int(input("Enter the duration of the activity to delete: "))
                activity_tree.delete_activity(duration)
                print("Activity deleted successfully!")
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == "3":
            print("Search by:")
            print("1. Duration")
            print("2. Activity Type")
            search_choice = input("Enter your choice: ")
            if search_choice == "1":
                try:
                    duration = int(input("Enter duration to search for: "))
                    results = activity_tree.search_activity(duration=duration)
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue
            elif search_choice == "2":
                activity_type = input("Enter activity type to search for: ").strip()
                results = activity_tree.search_activity(activity_type=activity_type)
            else:
                print("Invalid choice.")
                continue

            if results:
                print("Found activities:")
                for duration, activity_type in results:
                    print(f"  - {activity_type}: {duration} minutes")
            else:
                print("No matching activities found.")

        elif choice == "4":
            stats = activity_tree.generate_statistics()
            print("Statistics:")
            print(f"  Total Activities: {stats['total_activities']}")
            print(f"  Total Duration: {stats['total_duration']} minutes")

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()