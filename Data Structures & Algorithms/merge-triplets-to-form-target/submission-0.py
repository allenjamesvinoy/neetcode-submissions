class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x_bool = False
        y_bool = False
        z_bool = False

        #xyz_dict = defaultdict(list)

        for triplet in triplets:
            if triplet[0] == target[0] and not x_bool:
                #xyz_dict[target[0]].append(triplet)
                x_bool = target[1] >= triplet[1] and target[2] >= triplet[2]
            if triplet[1] == target[1] and not y_bool:
                #xyz_dict[target[0]].append(triplet)
                y_bool = target[0] >= triplet[0] and target[2] >= triplet[2]
            if triplet[2] == target[2] and not z_bool:
                #xyz_dict[target[0]].append(triplet)
                z_bool = target[1] >= triplet[1] and target[0] >= triplet[0]
        

        return x_bool and y_bool and z_bool