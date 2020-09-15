import time as t
# quick easy way to create a loop that runs for a fixed time
# + 60 = runs 1 minute, + 60 * 5 = 5 minutes, + 60 * 30 = 30 minutes, + 10 = 10 seconds, and so on
end_time = t.time() + 60
while t.time() < end_time:
    print ("not yet done")
print ("done")
