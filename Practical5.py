class CallCenterQueue:
    def __init__(self):
        self.queue = []

    def addCall(self, customerID, callTime):
        self.queue.append((customerID, callTime))
        print(f"Call from {customerID} added.")

    def answerCall(self):
        if not self.isQueueEmpty():
            call = self.queue.pop(0)
            print(f"Answered call from {call[0]} (Duration: {call[1]} mins).")
        else:
            print("No calls to answer.")

    def viewQueue(self):
        if self.isQueueEmpty():
            print("Queue is empty.")
        else:
            print("Calls waiting in queue:")
            for i, (cid, time) in enumerate(self.queue, 1):
                print(f"{i}. Customer ID: {cid}, Call Time: {time} mins")

    def isQueueEmpty(self):
        return len(self.queue) == 0


def run_call_center():
    call_center = CallCenterQueue()

    while True:
        print("\nMenu:")
        print("1. Add Call")
        print("2. Answer Call")
        print("3. View Queue")
        print("4. Check if Queue is Empty")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            cid = input("Enter Customer ID: ").strip()
            call_time = input("Enter Call Time (minutes): ").strip()
            if not call_time.isdigit():
                print("Please enter a valid number for call time.")
                continue
            call_center.addCall(cid, int(call_time))

        elif choice == '2':
            call_center.answerCall()

        elif choice == '3':
            call_center.viewQueue()

        elif choice == '4':
            print("Queue is empty." if call_center.isQueueEmpty() else "Queue is not empty.")

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the interactive call center program
run_call_center()


