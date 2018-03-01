class Ride:
    def __init__(self, n, a, b, x, y, s, f):
        self.rideNumber = n
        self.startPoint = [int(a),int(b)]
        self.finishPoint = [int(x),int(y)]
        self.minStart = int(s)
        self.maxFinish = int(f)
        self.distance = abs(int(y)-int(b)) + abs(int(x)-int(a))
        self.completed = False
        self.possible = self.isPossible()

    def __repr__(self):
        return """Ride no. {}
        Start: ({},{}) on or after {} | End: ({},{}) on or before {}
        Distance: {} | Possible : {}""".\
            format(self.rideNumber, self.startPoint[0], self.startPoint[1],
            self.minStart, self.finishPoint[0], self.finishPoint[1],
            self.maxFinish, self.distance, self.possible)

    def isPossible(self):
        if self.maxFinish - self.minStart > self.distance:
            return True
        return False

    def complete(self):
        self.completed = True



class Car:
    def __init__(self):
        self.location = [0,0]
        self.ridesDone = []
        self.currentRide = 0
        self.assignedRide = 0

    def __repr__(self):
        if self.currentRide:
            return "Car currently on Ride <Ride no. {}>".format(self.currentRide)
        elif self.assignedRide:
            return "Car assigned to Ride <Ride no. {}>".format(self.assignedRide)
        return "Car available at {}".format(self.location)


lines = [line.rstrip('\n') for line in open('a_example.in')]
print lines
info = lines.pop(0).split()

R = int(info[0])
C = int(info[1])
F = int(info[2])
N = int(info[3])
B = int(info[4])
T = int(info[5])



for i in range(F):
    car = Car()
    print car

for i in range(N):
    rideInfo = lines[i].split()
    ride = Ride(i+1, rideInfo[0], rideInfo[1], rideInfo[2], rideInfo[3], rideInfo[4], rideInfo[5])
    print ride
