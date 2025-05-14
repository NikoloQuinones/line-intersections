# Suppose you are given two sets of n points, one set {p1, p2, . . . , pn} on the line y = 0 and the other
# set {q1, q2, . . . , qn} on the line y = 1. Create a set of n line segments by connecting each point pi to
# the corresponding point qi. Your goal is to develop an algorithm to determine how many pairs of these
# line segments intersect. Your algorithm should take the 2n points as input, and return the number of
# intersections. Using divide-and-conquer, your code needs to run in O(n log n) time.
# Hint: How does this problem relate to counting inversions in a list?
#
# Input should be read in from stdin. The first line will be the number of instances. For each instance,
# the first line will contain the number of pairs of points (n). The next n lines each contain the location x
# of a point qi on the top line. Followed by the final n lines of the instance each containing the location x
# of the corresponding point pi on the bottom line. 

if __name__ == "__main__":
    
    print("Please enter the number of instances: ", end = "")
    instance_num = int(input(""))

    ### Acquire input
    instances = [] # list of instances
    for x in range(instance_num):
        print("Please enter the number of pairs in instance "+ str(x + 1)+": ", end = "")
        pair_num = int(input(""))

        qs = [] # list position of points on top line
        for i in range(pair_num):  
            print("Please enter point " + str(i+1) + " on top line: ", end = "")
            qs.append(int(input("")))

        ps = [] # list of position of points on bottom line
        for i in range(pair_num):
            print("Please enter point " + str(i+1) + " on bottom line: ", end = "")
            ps.append(int(input("")))

        instances.append((qs, ps))

    ### process each instance
    count = 1 # counter for instances
    for instance in instances:
        
        qs = instance[0] # get list position of points on top line
        ps = instance[1] # get list position of points on bottom line

        pairs = sorted(list(zip(qs, ps))) # list of pairs sorted by q value| O(n log n)
        
        # recursive algorithm which uses divide and conquer to count intersections
        def IntersectionCount(pairs): 
            # base case: only one pair
            if len(pairs) == 1: 
                return 0, pairs
            
            # divide
            left = pairs[0:len(pairs)//2]
            right = pairs[len(pairs)//2:]

            ints_left, left = IntersectionCount(left)
            ints_right, right = IntersectionCount(right)

            # merge two counts
            ints_between, merged = IntersectionMergeCount(left, right)

            return (ints_left + ints_between + ints_right, merged)
        
        # helper function to count intersections between two sorted lists of line segments
        def IntersectionMergeCount(left, right): 
            Lidx = 0
            Ridx = 0
            intersections = 0
            sortedPairs = []
            # compare front of list count intersection when the bottom point is greater than 
            while Lidx < len(left) or Ridx < len(right):
                if  Ridx >= len(right) or (Lidx < len(left) and left[Lidx][1] < right[Ridx][1]):
                    sortedPairs.append(left[Lidx])
                    Lidx += 1
                else:
                    sortedPairs.append(right[Ridx])
                    Ridx += 1
                    intersections += (len(left) - Lidx)
            return intersections, sortedPairs
        
        # sort by p value, basically count inversions of q values
        intersections, _  = IntersectionCount(pairs)
        print("Intersections in instance " + str(count) + ": " + str(intersections))
        count += 1
        


        