class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """ Method -1 """
        outgoing_count = {}
        for path in paths:
            city_a, city_b = path
            # checking if city_a is in outgoing_count then set to 1
            # if city_b(destination point) is in outgoing_count then set to 0, we don't want to increase.
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)
            
        # iter on the outgoing_count- > outgoing_count[city] == "0"
        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city

# Code Complexity :- O(n)
            
        """ Method -2 """
        A = []
        B = []
        
        for path in paths:
            city_a, city_b = path
            A.append(city_a)
            B.append(city_b)
        print(A)
        print(B)
        for city in B:
            if city not in A:
                return city
        