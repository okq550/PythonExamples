# O(n * d) Time | O(n) Space -> Where n/d are the size of of the inputs.
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for x in range(n + 1)]
    ways[0] = 1
	
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
	
    return ways[n]

result = numberOfWaysToMakeChange(6, [1, 5])

print(result)