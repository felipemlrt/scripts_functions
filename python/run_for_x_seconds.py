import time as t
# quick, easy, not very precise way to create a loop that runs for a fixed time
# forma rapida, simples e nao muito precisa de criar um loop que roda por um tempo definido
# + 60 = runs 1 minute, + 60 * 5 = 5 minutes, + 60 * 30 = 30 minutes, + 10 = 10 seconds, and so on
end_time = t.time() + 60
while t.time() < end_time:
    print ("not yet done")
print ("done")
#Be carefull, the time counted by the system in this manner is not precise and should not be trsted for critical time keeping.
#Cuidado a contagem de tempo desta forma não é precisa e não deve ser usada para situações onde a temporização é crítica.
