def share_ball(balls, share):
    
    def pactorial(n):
        pactorial = 1
        for i in range(n):
            pactorial *= (n-i)
        return pactorial

    result = int(pactorial(balls) / (pactorial(balls - share) * pactorial(share)))
    return result

print(share_ball(5,3))

class Share():
    balls = 0
    share = 0

    def pactorial(self, n):
        pactorial = 1
        for i in range(n):
            pactorial *= (n-i)
        return pactorial
    
    def share_balls(self, balls, share):
        result = int(self.pactorial(balls) / (self.pactorial(balls - share) * self.pactorial(share)))
        return result

a = Share()
print(a. share_balls(5,3))