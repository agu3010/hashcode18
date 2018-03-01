lines = [line.rstrip('\n') for line in open('a_example.in')]
print lines
info = lines.pop(0).split()

R = int(info[0])
C = int(info[1])
F = int(info[2])
N = int(info[3])
B = int(info[4])
T = int(info[5])

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

    def getNFV(self, freepool):
        global R, C
        min_distance = R+C
        nfv = None
        for car in freepool:
            l = car.location
            d = abs(l[0]-self.startPoint[0]) + abs(l[1]-self.startPoint[1])
            if d<min_distance:
                min_distance = d
                nfv = car
        return [nfv, min_distance]

    def getBAQ(self, freepool, now):
        [nfv, distance] = self.getNFV(freepool)
        baq = self.minStart - now - distance
        return baq


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



rideList = []

for i in range(N):
    rideInfo = lines[i].split()
    ride = Ride(i+1, rideInfo[0], rideInfo[1], rideInfo[2], rideInfo[3], rideInfo[4], rideInfo[5])
    rideList.append(ride)



carList = []

for i in range(F):
    car = Car()
    carList.append(car)


freePool = carList
print freePool


i = 0
while(i<=1):
    print i
    #sorted_rides = sortRides(rideList, freePool, i)
    #print sorted_rides
    i+=1
