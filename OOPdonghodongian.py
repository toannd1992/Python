
class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def tick(self):
        self.second += 1
        if ( self.second == 60 ):
            self.minute += 1
            self.second = 0
            if ( self.minute == 60):
                self.hour += 1
                self.minute = 0

def main():
    h = int(input())
    m = int(input())
    s = int(input())
    time = Clock(h, m, s)
    t = int(input())
    for i in range(t):
        time.tick()
    print(f"Time after {t} ticks: {time.hour:02}:{time.minute:02}:{time.second:02}")

main()