import socket, threading, pickle

class NetworkClient:
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))
        self.state={}
        self.lock=threading.Lock()
        threading.Thread(target=self.receive_loop,daemon=True).start()

    def send(self,data):
        try:
            self.sock.sendall(pickle.dumps(data))
        except: pass

    def receive_loop(self):
        while True:
            try:
                data = self.sock.recv(8192)
                if not data: break
                s = pickle.loads(data)
                with self.lock:
                    self.state = s
            except: pass

    def get_states(self):
        with self.lock:
            return self.state.copy()