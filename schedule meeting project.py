class Schedule:
    def __init__(self, time, desc):
        self.time = time
        self.desc = desc

    def __str__(self):
        return f"{self.time} - {self.desc}"


class Attendee:
    def __init__(self, a_id, a_name, a_company, a_feedback=None):
        self.a_id = a_id
        self.a_name = a_name
        self.a_company = a_company
        self.a_feedback = a_feedback

    def __str__(self):
        feedback = self.a_feedback if self.a_feedback is not None else "No Feedback is mentioned"
        return f"Id: {self.a_id}, Name: {self.a_name}, Company: {self.a_company}, Feedback: {feedback}"

    def set_feedback(self, feedback):
        self.a_feedback = feedback


class Event:
    def __init__(self, e_id, e_name, e_start, e_end):
        self.e_id = e_id
        self.e_name = e_name
        self.e_start = e_start
        self.e_end = e_end
        self.schedule = []
        self.attendees = []

    def __str__(self):
        result = [
            f"Event details for: {self.e_id}",
            f"Event Name: {self.e_name}",
            f"Starting at: {self.e_start}",
            f"Ending at: {self.e_end}"
        ]
        if not self.schedule:
            result.append("There are no schedules added.")
        else:
            result.append("Event Schedules are:")
            for s in self.schedule:
                result.append(str(s))
        if not self.attendees:
            result.append("No attendees registered to this.")
        else:
            result.append("Event Attendees:")
            for a in self.attendees:
                result.append(str(a))
        return "\n".join(result)

    def add_schedule(self, time, desc):
        schedule = Schedule(time, desc)
        self.schedule.append(schedule)

    def add_attendee(self, id, name, company, feedback=None):
        attendee = Attendee(id, name, company, feedback)
        self.attendees.append(attendee)


# Managing Events
events = {}

def create_event(id, name, start, end):
    if id not in events:
        event = Event(id, name, start, end)
        events[id] = event
    else:
        raise Exception("Event Already Exists.")

def show_events():
    for e_id in events:
        print(events[e_id])
        print("-" * 40)  # Just to separate events visually


# Example Usage
create_event("E_4Y5", "Developer Camp", "04/05/2025", "06/05/2025")
events["E_4Y5"].add_schedule("12:00", "Introduction of the meeting")
events["E_4Y5"].add_schedule("01:00", "Giving thanks to some important persons")
events["E_4Y5"].add_attendee("A_4Y3", "John Wick", "Wipro", "Good developer")
events["E_4Y5"].add_attendee("A_4Y4", "Radhika Komali", "Google", "She is a good scrum master")

show_events()
