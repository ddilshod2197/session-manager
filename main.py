class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id, user_data):
        if session_id not in self.sessions:
            self.sessions[session_id] = user_data
            return True
        return False

    def get_session(self, session_id):
        return self.sessions.get(session_id)

    def update_session(self, session_id, user_data):
        if session_id in self.sessions:
            self.sessions[session_id] = user_data
            return True
        return False

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False

    def list_sessions(self):
        return list(self.sessions.keys())

# Misol:
session_manager = SessionManager()

# Session yaratish
session_id = "12345"
user_data = {"name": "John", "email": "john@example.com"}
session_manager.create_session(session_id, user_data)

# Session olish
print(session_manager.get_session(session_id))  # {"name": "John", "email": "john@example.com"}

# Session yangilash
user_data["email"] = "john2@example.com"
session_manager.update_session(session_id, user_data)

# Session olish (yangilangan)
print(session_manager.get_session(session_id))  # {"name": "John", "email": "john2@example.com"}

# Session o'chirish
session_manager.delete_session(session_id)

# Sessionlar ro'yxati
print(session_manager.list_sessions())  # []
