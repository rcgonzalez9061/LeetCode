class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda box: box[1], reverse=True)
        total_units = 0
        while truckSize and boxTypes:
            num_boxes, units_per_box = boxTypes.pop(0)
            units_to_take = min((num_boxes, truckSize))
            total_units += units_per_box * units_to_take
            truckSize -= units_to_take
        return total_units
