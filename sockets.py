import traceback

from flask_socketio import SocketIO, join_room, leave_room


class Socket:
    def init_app(self, app):
        self.io = SocketIO(app)

        @self.io.on_error_default
        def socketio_error_handler(e):
            traceback.print_exc()

        @self.io.on('join', namespace="/ns")
        def on_join(room_name):
            join_room(room_name)

        @self.io.on('leave', namespace="/ns")
        def on_leave(room_name):
            leave_room(room_name)

    def __init__(self):
        self.io = None

    def emit_task(self, task_name, task, group):
        self.io.emit(task_name, task.serialize(), namespace="/ns", room=group)


socket = Socket()
