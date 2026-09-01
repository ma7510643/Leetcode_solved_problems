class Solution(object):
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles

        while numBottles >= numExchange:
            totalBottles += numBottles //numExchange
            numBottles = numBottles //numExchange + numBottles % numExchange

        return totalBottles






# Big O (n)
class Solution(object):
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Every time you exchange bottles, you lose (numExchange - 1) empty bottles net.
        # This formula calculates the total maximum full bottles directly.
        return numBottles + (numBottles - 1) // (numExchange - 1)
