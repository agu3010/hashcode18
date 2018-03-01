class Ride:
    def __init__(self, a, b, x, y, s, f):
        self.startPoint = [int(a),int(b)]
        self.finishPoint = [int(x),int(y)]
        self.minStart = int(s)
        self.maxFinish = int(f)
        self.distance = abs(int(y)-int(b)) + abs(int(x)-int(a))
        self.completed = False
        self.possible = self.isPossible()

    def __repr__(self):
        return "Start: ({},{}) on or after {} | End: ({},{}) on or before {} | Distance: {} | Possible : {}".\
            format(self.startPoint[0], self.startPoint[1], self.minStart, self.finishPoint[0], self.finishPoint[1], self.maxFinish, self.distance, self.possible)

    def isPossible(self):
        if self.maxFinish - self.minStart > self.distance:
            return True
        return False

    def complete(self):
        self.completed = True




lines = [line.rstrip('\n') for line in open('a_example.in')]
print lines
info = lines.pop(0).split()

R = int(info[0])
C = int(info[1])
F = int(info[2])
N = int(info[3])
B = int(info[4])
T = int(info[5])


print N

for i in range(N):
    rideInfo = lines[i].split()
    ride = Ride(rideInfo[0], rideInfo[1], rideInfo[2], rideInfo[3], rideInfo[4], rideInfo[5])
    print ride
