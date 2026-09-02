class MinStack:

    def __init__(self):
        self.data = []
        self.min_track = []

    def push(self, val: int) -> None:
        if not self.data:
            self.min_track.append(val)
        else:
            self.min_track.append(min(val, self.min_track[-1]))
        self.data.append(val)

    def pop(self) -> None:
        self.min_track.pop()
        self.data.pop()
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.min_track[-1]        
